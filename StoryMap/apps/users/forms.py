#!/usr/bin/env python
# encoding: utf-8

from django import forms
from .models import UserProfile
from captcha.fields import CaptchaField

class RegisterForm(forms.Form):

    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    #前端添加再次输入密码的功能
    password1 = forms.CharField(required=True, widget=forms.PasswordInput, min_length=6)
    password2 = forms.CharField(required=True, widget=forms.PasswordInput, min_length=6)

class LoginForm(forms.Form):

    username = forms.CharField(required=True)
    password= forms.CharField(required=True, widget=forms.PasswordInput, min_length=6)


class ActiveForm(forms.Form):
    # 激活时不对邮箱密码做验证
    # 应用验证码， 自定义错误输出key必须与异常一样
    captcha = CaptchaField(error_messages={'invalid': u'验证码错误'})


class ChangePasswordForm(forms.Form):

    previousPassword = forms.CharField(required=True, widget=forms.PasswordInput, min_length=6)
    newPassword1 = forms.CharField(required=True, widget=forms.PasswordInput, min_length=6)
    newPassword2 = forms.CharField(required=True, widget=forms.PasswordInput, min_length=6)



class UserCenterForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['nickname', 'gender', 'birthday']