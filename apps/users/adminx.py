__author__ = 'LiuTianyong'
__date__ = '2019/8/15 17:47'

import xadmin
from xadmin import views
from xadmin.plugins.auth import UserAdmin
from .models import EmailVerifyRecord, Banner, UserProfile





# 配置后台主题
class BaseSetting(object):
    '''打开主题功能'''
    enable_themes = True
    use_bootswatch = True


# 全局变量设置
class GlobalSettings(object):
    # 页面左上角字符
    site_title = "LoveMooc后台管理"
    # 底部字符
    site_footer = "LoveMooc在线"
    # 左侧菜单折叠
    menu_style = "accordion"


class EmailVerifyRecordAdmin(object):
    # 默认显示列
    list_display = ['email', 'code', 'send_type', 'send_time']
    # 可搜索列
    search_fields = ['email', 'code', 'send_type']
    # 可筛选字段
    list_filter = ['email', 'code', 'send_type', 'send_time']


class BannerAdmin(object):
    # 默认显示列
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    # 可搜索列
    search_fields = ['title', 'image', 'url', 'index']
    # 可筛选字段
    list_filter = ['title', 'image', 'url', 'index', 'add_time']



# 注册邮箱验证码 功能
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)

# 注册轮播图 功能
xadmin.site.register(Banner, BannerAdmin)

# 注册主题
xadmin.site.register(views.BaseAdminView, BaseSetting)

# 注册全局变量
xadmin.site.register(views.CommAdminView, GlobalSettings)
