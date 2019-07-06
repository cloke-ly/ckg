import time

from django.utils.deprecation import MiddlewareMixin

from User.models import User
from common.err import ERR
from libs.http import render_json


def timer(func):
    '''检查函数执行时间'''
    def inner(*args,**kwargs):
        t1 = time.time()
        result = func(*args,**kwargs)
        t2 = time.time()
        print('当前函数耗时:',(t2-t1)*1000,'ms')
        return result
    return inner

class AuthMiddleware(MiddlewareMixin):
    API_WHITE_LIST = [
        '/app/user/index/',
        '/app/user/getcode/'
    ]

    def process_request(self,request):
        if request.path in self.API_WHITE_LIST:
            return
        else:
            uid = request.session.get('uid')
            if uid is None:
                return render_json(code=ERR['LoginRequired'])
            else:
                request.user  = User.objects.get(id=uid)