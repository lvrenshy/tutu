from django.conf.urls import url
from django.urls import path,include
from . import views
app_name='travelteam'
#tips子路由
urlpatterns = [
    url(r'^show/',views.show,name='show'),
    url(r'^$',views.show,name='null_show'),
    url(r'^search/', views.search, name='search'),
    url(r'^abcd/', views.abcd, name='abcd'),

    url(r'^write/', views.write, name='write'),
    url(r'^teaminfo/', views.teaminfo, name='teaminfo'),
    url(r'^inpartTeam/', views.inpartTeam, name='inpartTeam'),
    url(r'^startTeam/((?P<content>.*)/)*', views.startTeam, name='startTeam'),
    url(r'^limit/', views.limit, name='limit'),
    url(r'^approve/', views.approve, name='approve'),
    url(r'^teamers/', views.teamers, name='teamers'),
    url(r'^guanliteam/', views.guanliteam, name='guanliteam'),
    url(r'^jianbiao/', views.jianbiao, name='jianbiao'),
    url(r'^review/', views.review, name='review'),
    url(r'^statusteam/', views.statusteam, name='statusteam')
]