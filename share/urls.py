from django.conf.urls import url
from django.urls import path,include
from . import views
app_name='share'
#share子路由
urlpatterns = [
    # url(r'^$',views.show,name='null_show'),
    url(r'^search/', views.search, name='search'),
    url(r'^write/', views.write, name='write'),
    # url('limit/', views.limit, name='limit'),
    url(r'^limit/(?P<con>.*)/', views.limit, name='limit'),
    # url(r'^limit/', views.limit, name='limit'),
    url(r'^approve/', views.approve, name='approve'),
    url(r'^approvenunm/', views.approvenunm, name='approvenunm'),
    url(r'^review/', views.review, name='review'),
    url(r'^showreview/', views.showreview, name='showreview'),
    url(r'^writereview/', views.writereview, name='writereview'),
    url(r'^show/', views.show, name='show')
]