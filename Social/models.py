from django.db import models

# Create your models here.
from django.db.models import Q

from common.err import SwipeTypeErr


class Swiped(models.Model):
    STYPR = (
        ('like','喜欢'),
        ('superlike','超级喜欢'),
        ('dislike','不喜欢'),
    )

    uid = models.IntegerField(verbose_name='滑动者 id')
    sid = models.IntegerField(verbose_name='被滑动者 id')
    stype = models.CharField(max_length=10,choices=STYPR,verbose_name='滑动的类型')
    stime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'swiped'


    @classmethod
    def swipe(cls,uid,sid,stype):
        if stype not in ['like','superlike','dislike']:
            raise SwipeTypeErr
        if not cls.objects.filter(uid=uid,sid=sid).exists():
            cls.objects.create(uid=uid,sid=sid,stype=stype)

    @classmethod
    def is_liked(cls,uid,sid):
        '''检查是否喜欢过某人'''
        like_styles = ['like','superlike']
        return cls.objects.filter(uid=uid,sid=sid,stype__in=like_styles).exists()

    @classmethod
    def all_like_me(cls,uid):
        like_styles = ['like','usperlike']
        return cls.objects.filter(uid=uid,stype__in=like_styles).values_list('sid',flat=True)

class Friend(models.Model):
    uid1 = models.IntegerField(verbose_name='用户 id')
    uid2 = models.IntegerField(verbose_name='用户 id')

    class Meta:
        db_table = 'friend'
    @classmethod
    def make_friends(cls,uid,sid):
        uid1,uid2 = (sid,uid) if uid > sid else (uid,sid)
        cls.objects.create(uid1=uid1,uid2=uid2)

    @classmethod
    def is_friends(cls,uid,sid):
        uid1,uid2 = (sid,uid) if uid > sid else (uid,sid)
        return cls.objects.filter(uid1=uid1,uid2=uid2)
    @classmethod
    def my_friends_ids(cls,uid):
        friend_ids = []
        condition = Q(uid1=uid) | Q(uid2=uid)
        for frd in cls.objects.filter(condition):
            fid = frd.uid2 if frd.uid1==uid else frd.uid1
            friend_ids.append(fid)
        return friend_ids

    @classmethod
    def break_off(cls, id, sid):
        uid1,uid2 = (id,sid) if id < sid else (sid,id)
        cls.objects.filter(uid1=uid1,uid2=uid2).delete()

