from django.http import HttpResponse

# Create your views here.
from User import logics
from common.err import ERR
from libs.http import render_json


def index(request):
    return HttpResponse('ok')


def getcode(request):
    phonenum = request.GET.get('phonenum')
    if logics.send_vcode(phonenum):
        return render_json(code=ERR['OK'])
    else:
        return render_json(code=ERR['SMSErr'])








