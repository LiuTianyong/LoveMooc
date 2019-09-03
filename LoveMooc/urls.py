"""LoveMooc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.views.generic import TemplateView
from django.views.static import serve
import xadmin
from django.urls import path
from users import views
try:
    from django.conf.urls import include, url,re_path
except ImportError:
    from django.conf.urls.defaults import include, url,re_path

from users.views import LoginView, RegisterView, ActiveUserView,IndexView
from users.views import ForgetPwdView, ResetView, ModifyPwdView,LogoutView
from LoveMooc.settings import MEDIA_ROOT

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    # 增加主页
    url('^$', IndexView.as_view(), name="index"),
    # 登陆
    url('^login/$', LoginView.as_view(), name="login"),
    # 登出
    url('^logout/$', LogoutView.as_view(), name="logout"),
    # 注册
    url('^register/$', RegisterView.as_view(), name="register"),
    # 验证码图片路径
    url(r'^captcha/', include('captcha.urls')),
    # 找回密码
    url('^forget/$', ForgetPwdView.as_view(), name="forget_pwd"),
    # 处理修改密码 提交密码请求
    url('^modify_pwd/$', ModifyPwdView.as_view(), name="modify_pwd"),
    # 重置密码
    url(r'^reset/(?P<reset_code>.*)/$', ResetView.as_view(), name="reset_pwd"),
    # 激活用户
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name="user_active"),
    # 处理上传文件访问路径
    url('^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

    # url('^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}, name='static'),

    # 课程机构url配置
    url('^org/', include(('organization.urls', 'organization'), namespace='org')),
    # 课程相关url配置
    url('^course/', include(('courses.urls', 'courses'), namespace='course')),
    # 个人中心
    url('^users/', include(('users.urls', 'users'), namespace='users')),
    # 富文本
    url(r'^ueditor/',include('DjangoUeditor.urls',)),
]

# 全局404页面
handler404 = views.page_not_found
# 全局500页面
handler500 = views.page_error