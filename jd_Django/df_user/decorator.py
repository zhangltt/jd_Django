# coding=utf-8
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from constant import DECIRATPR_URL

def user_login(function):

    def function_in(request,*args,**kwargs):
        # 如果session中有user_id这个key,表示登陆

        if request.session.has_key('user_id'):

            # 执行传进来的函数
            return function(request,*args,**kwargs)

        #否则返回登陆页面
        else:


            return redirect(DECIRATPR_URL['user_login'])

    return function_in