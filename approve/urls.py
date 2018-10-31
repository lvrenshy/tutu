from django.conf.urls import url
from django.urls import path,include
from . import views
app_name='user'
#user子路由
urlpatterns = [
    url(r'^$',views.show,name='show'),
    url(r'^login/', views.login, name='login'),
    url(r'^maxtip/', views.maxtip, name='maxtip'),
    url(r'^maxsh/', views.maxsh, name='maxsh'),
    url(r'^showApproveShare/', views.showApproveShare, name='showApproveShare'),
    url(r'^showshare/', views.showshare, name='showshare'),
    url(r'^showApproveTips/', views.showApproveTips, name='showApproveTips'),
    url(r'^show/', views.show, name='show'),
    url(r'^showtip/', views.showtip, name='showtip'),
    url(r'^showshareReview/', views.showshareReview, name='showshareReview'),
    url(r'^showtipReview/', views.showtipReview, name='showtipReview'),
    url(r'^reviewinfotip/', views.reviewinfotip, name='reviewinfotip'),
    url(r'^approveshare/', views.approveshare, name='approveshare'),
    url(r'^approvetip/', views.approvetip, name='approvetip'),
    url(r'^reviewinfoshare/', views.reviewinfoshare, name='reviewinfoshare'),

]