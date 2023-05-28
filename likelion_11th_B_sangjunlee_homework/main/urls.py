from django.urls import path
from .views import *

app_name = "main"
urlpatterns = [
    path('', mainpage, name="mainpage"),
    path('second/', secondpage, name="secondpage"),
    # app의 views.py에서 넘어옴
    # 새로 만든 views.py의 new함수와 create 함수 연결 (url만들기)
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    # mainpage.html detail부분에서 넘어옴
    # url에 post의 id 값을 넣어서 전달 -> 전달받은 id값을 통해 특정 게시글의 detail 띄우기
    path('<int:id>', detail, name="detail"),
    path('edit/<int:id>', edit, name = "edit"),
    path('update/<int:id>', update, name = "update"),
    path('delete/<int:id>', delete, name = "delete"),
    path('pic_delete/<int:id>', pic_delete, name = "pic_delete"),
    path('delete_comment/<int:id>/<int:com_id>', delete_comment, name="delete_comment"),

]