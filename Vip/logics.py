from common import err


def need_perm(perm_name):
    def deco(view_func):
        def wrap(request):
            user = request.user
            if user.vip.has_perm(perm_name):
                return view_func(request)
            else:
                raise err.PermRequired
        return wrap
    return deco
