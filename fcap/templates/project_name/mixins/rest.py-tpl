from flask import jsonify
from flask_login import current_user


class RestMixin(object):

    def get_user(self):
        """ 获取当前登录用户"""
        user = current_user._get_current_object()
        return user
    
    def ok(self, **kw):
        dic = {'status': 200}
        dic.update(kw)
        return jsonify(**dic)
    
    def no(self, **kw):
        dic = {'status': 500}
        dic.update(kw)
        return jsonify(**dic)