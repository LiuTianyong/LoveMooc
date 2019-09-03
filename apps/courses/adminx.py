__author__ = 'LiuTianyong'
__date__ = '2019/8/15 19:19'

import xadmin

from .models import Course, Lesson
from .models import CourseResource, Video


class LessonInline(object):
    model = Lesson
    extra = 0


class CourseResourceInline(object):
    model = CourseResource
    extra = 0


class CourseAdmin(object):
    # 默认显示列
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums',
                    'add_time']
    # 可搜索列
    search_fields = ['name', 'desc', 'detail', 'degree', 'students', 'fav_nums', 'image', 'click_nums']
    # 可筛选字段
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'click_nums',
                   'add_time']
    # 只读
    readonly_fields = ['click_nums', 'fav_nums']
    inlines = [LessonInline, CourseResourceInline]

    style_fields = {"detail":"ueditor"}
    # import_excel = True


class LessonAdmin(object):
    # 默认显示列
    list_display = ['course', 'name', 'add_time']
    # 可搜索列
    search_fields = ['course', 'name']
    # 可筛选字段
    list_filter = ['course__name', 'name', 'add_time']


class CourseResourceAdmin(object):
    # 默认显示列
    list_display = ['course', 'name', 'download', 'add_time']
    # 可搜索列
    search_fields = ['course', 'name']
    # 可筛选字段
    list_filter = ['course', 'name', 'download', 'add_time']


class VideoAdmin(object):
    # 默认显示列
    list_display = ['lesson', 'name', 'add_time']
    # 可搜索列
    search_fields = ['lesson', 'name']
    # 可筛选字段
    list_filter = ['lesson', 'name', 'add_time']


# 注册课程
xadmin.site.register(Course, CourseAdmin)
# 注册章节
xadmin.site.register(Lesson, LessonAdmin)
# 章节视频
xadmin.site.register(Video, VideoAdmin)
# 注册章节资源
xadmin.site.register(CourseResource, CourseResourceAdmin)
