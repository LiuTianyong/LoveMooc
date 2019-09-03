__author__ = 'LiuTianyong'
__date__ = '2019/8/18 21:50'

try:
    from django.conf.urls import include, url
except ImportError:
    from django.conf.urls.defaults import include, url

from .views import CourseListView, CourseDetailView, CourseInfoView, CommentsView
from .views import AddCommentsView, VideoPlayView

'''课程'''
urlpatterns = [
    # include 自动拼接 org/list
    url('^list/$', CourseListView.as_view(), name="course_list"),
    # 课程详情页
    url('^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name="course_detail"),
    # 课程视频
    url('^info/(?P<course_id>\d+)/$', CourseInfoView.as_view(), name="course_info"),
    # 课程评论
    url('^comment/(?P<course_id>\d+)/$', CommentsView.as_view(), name="course_comments"),
    # 添加课程评论
    url('^add_comment/$', AddCommentsView.as_view(), name="add_comment"),
    # 视频
    url('^video/(?P<video_id>\d+)/$', VideoPlayView.as_view(), name="video_play"),

]
