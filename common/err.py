ERR = {
    'OK':0,
    'SMSErr':1000,
    'VcodeErr':1001,
    'LoginRequired':1002,
    'UserInfoErr':1003,
    'ProfileErr':1004,
}


class LogidaErr(Exception):
    code = 0
    data = None

    def __init__(self,data=None):
        if data is None:
            self.data = self.__class__.__name__
        else:
            self.data = data

def gen_logic_err(name,code):
    '''生成一个逻辑异常类'''
    return type(name,(LogidaErr,),{'code':code})

OK = gen_logic_err('OK', 0)                           # 正常
SMSErr = gen_logic_err('SMSErr', 1000)                # 短信错误
VcodeErr = gen_logic_err('VcodeErr', 1001)            # 验证码错误
LoginRequired = gen_logic_err('LoginRequired', 1002)  # 用户未登录
UserInfoErr = gen_logic_err('UserInfoErr', 1003)      # 用户信息错误
ProfileErr = gen_logic_err('ProfileErr', 1004)        # 个人资料错误
SwipeTypeErr = gen_logic_err('SwipeTypeErr', 1005)    # 滑动错误

RewindTimeErr = gen_logic_err('RewindTimeErr', 1006)  # 反悔时间超过限制
RewindTimesLimit = gen_logic_err('RewindTimesLimit', 1007)  # 反悔次数达到上限
PermRequired = gen_logic_err('PermRequired', 1008)    # 权限不足








