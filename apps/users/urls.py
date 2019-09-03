__author__ = 'LiuTianyong'
__date__ = '2019/8/20 21:37'

__author__ = 'LiuTianyong'
__date__ = '2019/8/18 21:50'

try:
    from django.conf.urls import include, url
except ImportError:
    from django.conf.urls.defaults import include, url
from .views import UserInfoView, UploadImageView, UpdatePwdView
from .views import SendEmailCodeView, UpdateEmailView, MyCourseView
from .views import MyFavOrgView,MyFavTeacherView,MyFavCourseView
from .views import MymessageView

'''个人中心'''
urlpatterns = [
    # 用户信息
    url('^info/$', UserInfoView.as_view(), name="user_info"),
    # 用户头像上传
    url('^image/upload/$', UploadImageView.as_view(), name="image_upload"),
    # 个人中心修改密码
    url('^update/pwd/$', UpdatePwdView.as_view(), name="update_pwd"),
    # 发送验证码
    url('^sendemail_code/$', SendEmailCodeView.as_view(), name="sendemail_code"),
    # 修改邮箱
    url('^update_email/$', UpdateEmailView.as_view(), name="update_email"),
    # 我的课程
    url('^mycourse/$', MyCourseView.as_view(), name="mycourse"),

    # 我收藏课程机构
    url('^myfav/org/$', MyFavOrgView.as_view(), name="myfav_org"),
    # 我收藏授课教师
    url('^myfav/teacher/$', MyFavTeacherView.as_view(), name="myfav_teacher"),
    # 我收藏课程
    url('^myfav/course/$', MyFavCourseView.as_view(), name="myfav_course"),
    # 我的消息
    url('^mymessage/$', MymessageView.as_view(), name="mymessage"),


]
