"""
URL configuration for likelion_11th_B_sangjunlee_homework project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.mainpage, name="mainpage"),
    path('second/', views.secondpage, name="secondpage"),
    # app의 views.py에서 넘어옴
    # 새로 만든 views.py의 new함수와 create 함수 연결 (url만들기)
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
    # mainpage.html detail부분에서 넘어옴
    # url에 post의 id 값을 넣어서 전달 -> 전달받은 id값을 통해 특정 게시글의 detail 띄우기
    path('<int:id>', views.detail, name="detail"),
]

