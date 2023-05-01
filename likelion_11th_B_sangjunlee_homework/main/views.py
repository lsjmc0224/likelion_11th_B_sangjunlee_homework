from django.shortcuts import render, redirect, get_object_or_404 # Render : 템플릿을 불러옴, Redirect : URL로 이동, get_object_or_404 : 가져올 객체가 있으면 가져오고 없으면 404에러를 띄움
from .models import Blog # 아깐 admin창에서 보이기 위해 불러왔다면, 여기는 views에 보여주기 위해 불러옴
from django.utils import timezone # 장고에서 제공하는 시간 관련 기능 사용
# Create your views here.

def detail(request, id): # input에 원하는 id값을 넣어서 detail 함수를 실행
    blog = get_object_or_404(Blog, pk = id) # id 있나 확인하고 있으면 blog에 넣어서 보내주고, 없으면 404
    # ??? pk ??? : primary key. 각 객체를 구분해주는 키 값.
    return render(request, 'main/detail.html',{'blog':blog})

def mainpage(request):
    blogs = Blog.objects.all() #변수 blogs에 Blog의 모든 객체를 저장 즉, blogs에 모든 게시물이 담긴다.
    return render(request, 'main/mainpage.html') # mainpage.html을 띄우는 함수

def secondpage(request):
    return render(request, 'main/secondpage.html') # secondpage.html을 띄우는 함수

def create(request): # 게시글 작성 요청
    new_blog = Blog() # 새 Blog 정의
    new_blog.title = request.POST['title'] # 새 Blog의 타이틀 정의 
    new_blog.writer = request.POST['writer'] # 새 Blog의 작성자 정의
    new_blog.pub_date = timezone.now() # 새 Blog의 시간 (작성하는 현재시간) 정의
    new_blog.body = request.POST['body'] # 새 Blog의 내용 정의

    new_blog.save()
    return redirect('detail', new_blog.id) # 게시글 작성이 끝나면 게시글의 detail을 볼 수 있도록 이동 -> read 파트에서 작성

# new.html에서 넘어옴. new.html을 띄우는 함수
def new(request):
    return render(request, 'main/new.html') # 경로 설정, Render : 템플릿을 불러옴
