__author__ = 'LiuTianyong'
__date__ = '2019/8/16 16:09'

from django import forms
from captcha.fields import CaptchaField

from .models import UserProfile



# 个人信息
class UploadInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfile()
        fields = ['nick_name','gender','birthday','address','mobile']


# 头像修改
class UploadImageForm(forms.ModelForm):
    class Meta:
        model = UserProfile()
        fields = ['image']


# 登陆表单验证
class LoginForm(forms.Form):
    # required是否为必填字段 —— 能否为空
    # 字段必须和 html中提交的字段名相同
    username = forms.CharField(required=True,min_length=6)
    password = forms.CharField(required=True,min_length=8)


# 注册验证
class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True,min_length=8,max_length=16)
    # 验证码校验 invalid异常别名为 验证码错误
    captcha = CaptchaField(error_messages={"invalid":"验证码错误"})


# 找回密码验证码校验
class ForgetForm(forms.Form):
    email = forms.EmailField(required=True)
    # 验证码校验 invalid异常别名为 验证码错误
    captcha = CaptchaField(error_messages={"invalid":"验证码错误"})


# 密码修改
class ModifyPwdForm(forms.Form):
    password1 = forms.CharField(required=True,min_length=8)
    password2 = forms.CharField(required=True,min_length=8)