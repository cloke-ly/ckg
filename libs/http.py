import json

from django.http import HttpResponse

from CKG import settings


def render_json(data=None,code=0):
    result = {
        'code':code,
        'data':data
    }
    if settings.DEBUG:
        json_str = json.dumps(result,ensure_ascii=False,indent=4,sort_keys=True)
    else:
        json_str = json.dumps(result,ensure_ascii=False,separators=(',',':'))

    return HttpResponse(json_str)



if __name__ == '__main__':
    result = render_json('你好',0)
    print(result)