import datetime

from django.core.cache import cache

from CKG import cfg
from Social.models import Swiped, Friend
from User.models import User
from common import err, keys


def rcmds(user):
    '''推荐用户'''
    today = datetime.date.today()

    min_birthday = today - datetime.timedelta(user.profile.max_dating_age * 365)
    max_birthday = today - datetime.timedelta(user.profile.min_dating_age * 365)

    users = User.objects.filter(
        sex = user.profile.dating_sex,
        location=user.profile.dating_location,
        birthday__gte=min_birthday,
        birthday__lte=max_birthday
    )[:20]

    return users


def like_someone(user, sid):
    '''喜欢某人'''
    Swiped.swipe(user.id,sid,'like')
    if Swiped.is_liked(sid,user.id):
        Friend.make_friends(sid,user.id)
        return True
    else:
        return False

def superlike_someone(user, sid):
    '''喜欢某人'''
    Swiped.swipe(user.id,sid,'superlike')
    if Swiped.is_liked(sid,user.id):
        Friend.make_friends(sid,user.id)
        return True
    else:
        return False


def rewind_swiped(user):
    latest_swpied = Swiped.objects.filter(uid=user.id).latest('stime')
    tzinfo = latest_swpied.stime.tzinfo
    now = datetime.datetime.now(tzinfo)
    time_diff = (now - latest_swpied.stime).total_seconds()

    if time_diff > cfg.REWIND_TIME:
        raise err.RewindTimeErr

    rewind_key = keys.REWIND_KEY.format(user.id)
    curr_times = cache.get(rewind_key,0)

    if curr_times >= cfg.REWIND_TIMES:
        raise err.RewindTimesLimit

    next_day = datetime.datetime(now.year,now.month,now.day+1,tzinfo)
    remain_seconds = (next_day-now).total_seconds()

    cache.set(rewind_key,curr_times+1,remain_seconds)

    Friend.break_off(user.id,latest_swpied.sid)

    latest_swpied.delete()