__author__ = 'LiuTianyong'
__date__ = '2019/8/17 20:18'

from django.urls import path

try:
    from django.conf.urls import include, url
except ImportError:
    from django.conf.urls.defaults import include, url

from .views import OrgView, AddUserAskView, OrgHomeView
from .views import OrgCourseView, OrgDescView, OrgTeacherView
from .views import AddFavView, TeacherListView, TeacherDetailView

'''课程机构列表页'''
urlpatterns = [
    # include 自动拼接 org/list
    url('^list/$', OrgView.as_view(), name="org_list"),
    # 课程咨询
    url('^add_ask/$', AddUserAskView.as_view(), name="add_ask"),
    # 机构首页
    url('^home/(?P<org_id>\d+)/$', OrgHomeView.as_view(), name="org_home"),
    # 机构课程列表
    url('^course/(?P<org_id>\d+)/$', OrgCourseView.as_view(), name="org_course"),
    # 机构介绍
    url('^desc/(?P<org_id>\d+)/$', OrgDescView.as_view(), name="org_desc"),
    #  机构讲师
    url('^org_teacher/(?P<org_id>\d+)/$', OrgTeacherView.as_view(), name="org_teacher"),
    # 机构收藏
    url('^add_fav/$', AddFavView.as_view(), name="add_fav"),
    # 讲师列表
    url('^teacher/list/', TeacherListView.as_view(), name="teacher_list"),
    # 讲师详细
    url('^teacher/detail(?P<teacher_id>\d+)/$', TeacherDetailView.as_view(), name="teacher_detail"),

]
