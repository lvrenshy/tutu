from django.conf.urls import url
from django.urls import path,include
from . import views
app_name='question'
#question子路由
urlpatterns = [
    url(r'^$',views.showQuestion,name='showQuestion'),
    url('search/', views.search, name='search'),
    url('showQuestion/', views.showQuestion, name='showQuestion'),
    url('waitquestion/', views.waitquestion, name='waitquestion'),
    url('showAnswer/', views.showAnswer, name='showAnswer'),
    url('queLimit/', views.queLimit, name='queLimit'),
    url('ansLimit/', views.ansLimit, name='ansLimit'),
    url('ask/', views.ask, name='ask'),
    url('answer/', views.answer, name='answer'),
    url('jianbiao/', views.jianbiao, name='jianbiao'),
    url('questioninfo/', views.questioninfo, name='questioninfo'),
    url('show/', views.show, name='show')
]