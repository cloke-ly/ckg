from django.core.cache import cache
from django.http import HttpResponse

# Create your views here.
from User import logics
from User.forms import UserForm, ProfileForm
from User.logics import save_avatar
from User.models import User
from common import keys
from common.err import ERR
from libs.http import render_json


def index(request):
    return HttpResponse('ok')


def getcode(request):
    '''用户获取验证码'''
    phonenum = request.GET.get('phonenum')
    if logics.send_vcode(phonenum):
        return render_json(code=ERR['OK'])
    else:
        return render_json(code=ERR['SMSErr'])

def check_vcode(request):
    '''检查验证码'''
    phonenum = request.POST.get('phonenum')
    vcode = request.POST.get('vcode')
    cache_vcode = cache.get(keys.VCODE_KEY.format(phonenum))
    if cache_vcode == vcode:
        try:
            user = User.objects.get(phonenum=phonenum)
        except User.DoesNotExist:
            user = User.objects.create(phonenum=phonenum,nickname=phonenum)
        request.session['uid'] = user.id
        return render_json(data=user.to_dict())
    else:
        return render_json(code=ERR['VcodeErr'])


def get_profile(request):
    '''获取交友资料结口'''
    result = request.user.profile.to_dict()
    return render_json(result)


def set_profile(request):
    '''修改个人/交友资料结口'''
    user = request.user

    # 更新用户信息
    user_form = UserForm(request.POST)
    if user_form.is_valid():
        user.__dict__.update(user_form.cleaned_data)
        user.save()
    else:
        return render_json(user_form.errors,ERR['UserInfoErr'])

    # 跟新个人资料
    profile_form = ProfileForm(request.POST)
    if profile_form.is_valid():
        profile = profile_form.save(commit=False)
        profile.id = user.id
        profile.save()
    else:
        return render_json(profile_form.errors,ERR['ProfileErr'])
    return render_json()


def upload_avatar(request):
    '''上传个人头像'''
    avatar = request.FILES.get('avatar')
    logics.upload_file.delay(request.user,avatar)
    return render_json()










