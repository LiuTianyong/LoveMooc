__author__ = 'LiuTianyong'
__date__ = '2019/8/15 19:54'

import xadmin

from .models import Teacher, CourseOrg, CityDict


class CityDictAdmin(object):
    # 默认显示列
    list_display = ['name', 'desc', 'add_time']
    # 可搜索列
    search_fields = ['name', 'desc']
    # 可筛选字段
    list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):
    # 默认显示列
    list_display = ['name', 'desc', 'category', 'click_nums', 'fav_nums', 'image', 'address', 'city', 'add_time']
    # 可搜索列
    search_fields = ['name', 'desc', 'category', 'click_nums', 'fav_nums', 'address', 'city']
    # 可筛选字段
    list_filter = ['name', 'desc', 'category', 'click_nums', 'fav_nums', 'address', 'city', 'add_time']
    relfield_style = 'fk-ajax'

class TeacherAdmin(object):
    # 默认显示列
    list_display = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums',
                    'add_time']
    # 可搜索列
    search_fields = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums']
    # 可筛选字段
    list_filter = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums',
                   'add_time']


# 注册城市
xadmin.site.register(CityDict, CityDictAdmin)
# 注册课程机构
xadmin.site.register(CourseOrg, CourseOrgAdmin)
# 注册授课老师
xadmin.site.register(Teacher, TeacherAdmin)
