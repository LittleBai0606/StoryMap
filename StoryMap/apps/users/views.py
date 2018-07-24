from django.shortcuts import render
from django.views.generic import View
from .models import UserProfile, EmailVerifyRecord
from .forms import RegisterForm, LoginForm, ActiveForm, UserCenterForm, ChangePasswordForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q
from utils.email_send import send_register_email
from django.contrib.auth.hashers import make_password
from django.contrib import auth
import os, base64, datetime


class RegisterView(View):
    """
    用户注册功能
    """
    def get(self, request):
        """
        如果已登录就跳转到首页
        """
        user = request.user
        if user.is_authenticated:
            return HttpResponseRedirect('/')
        return render(request, 'login.html')

    def post(self, request):

        register_form = RegisterForm(request.POST)
        user_email = request.POST.get('email', '')
        is_email_exist = UserProfile.objects.filter(email=user_email)

        if is_email_exist:
            return HttpResponse('{"status": "fail", "msg": "邮箱已注册，请更换邮箱注册"}', content_type='application/json')
        elif register_form.is_valid():
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            e_mail = request.POST.get('email', '')

            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.password = make_password(pass_word)
            user_profile.email = e_mail
            user_profile.is_active = False

            user_profile.save()

            send_register_email(e_mail, 'register')

            return HttpResponse('{"status": "success", "url":"/"}', content_type='application/json')
        else:
            return HttpResponse('{"status": "fail", "msg": "注册失败，请重新注册"}', content_type='application/json')

class UserLoginView(View):
        """
        用户登录功能
        """
        def get(self, request):
            """
            如果已登录就跳转到首页
            """
            user = request.user
            if user.is_authenticated:
                return HttpResponseRedirect('/')
            register_form = RegisterForm()
            return render(request, 'login.html', context={'register_form': register_form})

        def post(self, request):
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)

                    return HttpResponse('{"status": "success", "url": "/"}', content_type='application/json')
                else:
                    return HttpResponse('{"status": "fail", "msg": "用户未激活, 请先激活用户"}',
                                        content_type='application/json')
            else:
                return HttpResponse('{"status": "fail", "msg": "用户或密码错误!"}', content_type='application/json')



class UserLogoutView(View):
        """
        用户注销功能
        """
        def get(self, request):
            auth.logout(request)
            return HttpResponseRedirect("/")

        def post(self, request):
            auth.logout(request)
            return HttpResponseRedirect("/")


class ActiveUserView(View):
    """
    激活用户
    """
    def get(self, request, active_code):
        # 查询邮箱验证记录是否存在
        all_record = EmailVerifyRecord.objects.filter(code = active_code)
        # 激活form负责给激活跳转进来的人加验证码
        # 如果不为空也就是有用户
        register_form = RegisterForm()
        if all_record:
            for record in all_record:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
                login(request, user)
                # 激活成功跳转到登录页面
                return render(request, 'index.html')
        else:
            return render(request, 'login.html', context={'register_form': register_form})

    def post(self, request):
        user = request.user
        if user.is_authenticated:
            return HttpResponseRedirect('/')
        register_form = RegisterForm()
        return render(request, 'login.html', context={'register_form': register_form})







