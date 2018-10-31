"""tutu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url

urlpatterns = [
    url('approve/', include('approve.urls', namespace='tutu.approve')),

    path('admin/', admin.site.urls),
    #子路由部分：
    url('user/',include('user.urls',namespace='tutu.user')),
    url('travelteam/',include('travelteam.urls',namespace='tutu.travelteam')),
    url('tips/',include('tips.urls',namespace='tutu.tips')),
    url('share/',include('share.urls',namespace='tutu.share')),
    url('question/',include('question.urls',namespace='tutu.question')),
    url('endteam/',include('endteam.urls',namespace='tutu.endteam')),
]
