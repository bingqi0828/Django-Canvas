import xadmin

from .models import EmailVerifyRecord
from .models import Banner
from xadmin import views

class BaseSettings(object):
    enable_themes=True
    use_bootswatch=True

class GlobalSettings(object):
    site_title='后台管理页面'
    site_footer='Bing的公司'
    menu_style='accordion'

class EmailVerifyRecordAdmin(object):
    # 显示的列
    list_display = ['code', 'email', 'send_type', 'send_time']
    # 搜索的字段，不要添加时间搜索
    search_fields = ['code', 'email', 'send_type']
    # 过滤
    list_filter = ['code', 'email', 'send_type', 'send_time']

xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)

class BannerAdmin(object):
    list_display = ['title', 'image', 'url','index', 'add_time']
    search_fields = ['title', 'image', 'url','index']
    list_filter = ['title', 'image', 'url','index', 'add_time']

xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(Banner,BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSettings)



