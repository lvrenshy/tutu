from django.conf.urls import url
from django.urls import path,include
from . import views
app_name='user'
#user子路由
urlpatterns = [
    url(r'^$',views.show,name='show'),
    url(r'^login/', views.login, name='login'),
    url(r'^show/', views.show, name='show'),
    url(r'^regist/', views.regist, name='regist'),
    url(r'^createteam/', views.createteam, name='createteam'),
    url(r'^jointeam/', views.jointeam, name='jointeam'),
    url(r'^changepassword/', views.changepassword, name='changepassword'),
    # url('updateusername/', views.updateusername, name='updateusername'),
    url(r'^updateInfo/', views.updateInfo, name='updateInfo'),
    url(r'^showInpart/', views.showInpart, name='showInpart'),
    url(r'^panduan/', views.panduan, name='panduan'),
    url(r'^showmyteaminfo/', views.showmyteaminfo, name='showmyteaminfo'),
    url(r'^showmyshareinfo/', views.showmyshareinfo, name='showmyshareinfo'),
    # url('startTeam/', views.startTeam, name='startTeam'),
    # url('endTeam/', views.endTeam, name='endTeam'),
    url(r'^showShare/', views.showShare, name='showShare'),
    url(r'^deleteShare/', views.deleteShare, name='deleteShare'),
    url(r'^showTips/', views.showTips, name='showTips'),
    url(r'^deleteTips/', views.deleteTips, name='deleteTips'),
    url(r'^showAsk/', views.showAsk, name='showAsk'),
    url(r'^sixin/', views.sixin, name='sixin'),
    url(r'^checksixin/', views.checksixin, name='checksixin'),
    url(r'^qiniu/', views.qiniu, name='qiniu'),

    url(r'^showAnswer/', views.showAnswer, name='showAnswer'),

    # url('showApprove/', views.showapprove, name='showApprove'),
    url('showReview/', views.showReview, name='showReview'),
    url('ceshi/', views.ceshi, name='ceshi'),
    url('yezheng/', views.yezheng, name='yezheng'),
    url('sendcode/', views.sendcode, name='sendcode')

]