__author__ = 'LiuTianyong'
__date__ = '2019/8/15 21:20'

import xadmin


from .models import UserAsk,UserCourse
from .models import UserFavorite,UserMessage


class UserAskAdmin(object):
    # 默认显示列
    list_display = ['name', 'moblie', 'course_name', 'add_time']
    # 可搜索列
    search_fields = ['name', 'moblie', 'course_name']
    # 可筛选字段
    list_filter = ['name', 'moblie', 'course_name', 'add_time']


class UserCourseAdmin(object):
    # 默认显示列
    list_display = ['user', 'course', 'add_time']
    # 可搜索列
    search_fields = ['user', 'course']
    # 可筛选字段
    list_filter = ['user', 'course', 'add_time']


class UserFavoriteAdmin(object):
    # 默认显示列
    list_display = ['user', 'fav_id', 'fav_type','add_time']
    # 可搜索列
    search_fields = ['user', 'fav_id', 'fav_type']
    # 可筛选字段
    list_filter = ['user', 'fav_id', 'fav_type','add_time']


class UserMessageAdmin(object):
    # 默认显示列
    list_display = ['user', 'message', 'has_read','add_time']
    # 可搜索列
    search_fields = ['user', 'message', 'has_read','add_time']
    # 可筛选字段
    list_filter = ['user', 'message', 'has_read','add_time']


# 注册用户咨询
xadmin.site.register(UserAsk,UserAskAdmin)
# 注册用户课程
xadmin.site.register(UserCourse,UserCourseAdmin)
# 注册用户收藏
xadmin.site.register(UserFavorite,UserFavoriteAdmin)
# 注册用户消息
xadmin.site.register(UserMessage,UserMessageAdmin)









