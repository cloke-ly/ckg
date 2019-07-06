import os
import random
from urllib.parse import urljoin

import requests

from django.core.cache import cache
from common import keys
from CKG import cfg, settings
from libs.qn_cloud import upload_to_qn
from tasks import celery_app


def rand_vcode(length):
    return ''.join([str(random.randint(0,9)) for i in range(length)])


def send_vcode(phonenum):
    vcode = rand_vcode(4)
    cache.set(keys.VCODE_KEY.format(phonenum),vcode,180)
    params = cfg.YZX_SMS_PARAMS.copy()
    params['mobile'] = phonenum
    params['param'] = vcode
    resp = requests.post(cfg.YZX_SMS_API,json=params)
    if resp.status_code == 200:
        return True
    else:
        return False


def save_avatar(user,upload_file):
    filename = 'Avaatar-{}'.format(user.id)
    filepath = os.path.join(settings.MEDIA_ROOT,filename)

    with open(filepath,'wb')as fp:
        for chunk in upload_file.chunks():
            fp.write(chunk)
    return filepath,filename

@celery_app
def upload_file(user,upload_file):
    '''上传文件'''
    filepath,filename = save_avatar(user,upload_file)
    upload_to_qn(filepath,filename)

    avatar_url = urljoin(cfg.QN_BASE_URL,filename)
    user.avatar = avatar_url
    user.save()

    os.remove(filepath)

if __name__ == '__main__':
    vcode = rand_vcode(6)
    print(vcode)
    send_vcode('13783615776')