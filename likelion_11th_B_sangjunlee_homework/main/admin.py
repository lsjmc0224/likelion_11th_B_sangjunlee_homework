from django.contrib import admin
# view.py의 함수를 연결해주는 url을 생성
from django.urls import path # 장고에서 path라는 메서드를 가져옴
from main import views # main(자기 상위폴더)에서 views.py를 가져옴


# models.py에서 Post class 불러오고 admin 사이트에 등록 (이래야 사이트에서 확인가능)
from .models import Post
admin.site.register(Post)

urlpatterns = [
    path('admin/', admin.site.urls), #어드민 url admin으로 생성
    path('', views.mainpage, name="mainpage"), # mainpage url 공란으로 설정
]

# Register your models here.
