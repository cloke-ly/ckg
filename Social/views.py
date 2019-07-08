from django.shortcuts import render

# Create your views here.
from Social import logics
from Social.models import Swiped
from libs.http import render_json


def rcmd_user(request):
    user_list = logics.rcmds(request.user)
    result = [user.to_dict() for user in user_list]
    return render_json(result)

def like(request):
    '''喜欢'''
    sid = int(request.POST.get('sid'))
    is_matched = logics.like_someone(request.user,sid)
    return render_json({'is_matched': is_matched})

def super_like(request):
    sid = int(request.POST.get('sid'))
    is_matched = logics.superlike_someone(request.user, sid)
    return render_json({'is_matched': is_matched})

def dislike(request):
    '''不喜欢'''
    sid = int(request.POST.get('sid'))
    Swiped.swipe(request.user.id, sid, 'dislike')
    return render_json()

def rewind(request):
    logics.rewind_swiped(request.user)
    return render_json()

def show_liked_me(request):
    return render_json()

def friend_list(request):
    '''个人的好友列表'''
    result = [frd.to_dict() for frd in request.user.friends]
    return render_json(result)
