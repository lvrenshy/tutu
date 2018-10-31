from django.conf.urls import url
from django.urls import path,include
from . import views
app_name='endteam'
#endteam子路由
urlpatterns = [
    # 不输入内容时显示内容
    # url(r'^$',views.show,name='null_show'),
    # 书写结团信息
    url('write/', views.write, name='write'),
    # # 结团信息展示
    # # url('show/', views.show, name='show_end'),
    # # 搜索结束的团
    # # url('search/', views.search, name='search_end'),
    # # 分页接口
    # url('limit/', views.limit, name='limit_end'),
    # # 点赞
    # url('approve/', views.approve, name='approve_end'),
    # # 评论
    # url('review/', views.review, name='review_end')

]