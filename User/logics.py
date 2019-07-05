import random

import requests
from django.core.cache import cache
from common import keys
from CKG import cfg



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

if __name__ == '__main__':
    vcode = rand_vcode(6)
    print(vcode)
    send_vcode('13783615776')