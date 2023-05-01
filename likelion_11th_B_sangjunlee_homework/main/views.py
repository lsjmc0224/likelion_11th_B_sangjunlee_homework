from django.shortcuts import render, redirect, get_object_or_404 # Render : 템플릿을 불러옴, Redirect : URL로 이동, get_object_or_404 : 가져올 객체가 있으면 가져오고 없으면 404에러를 띄움
from .models import Post # 아깐 admin창에서 보이기 위해 불러왔다면, 여기는 views에 보여주기 위해 불러옴
from django.utils import timezone # 장고에서 제공하는 시간 관련 기능 사용
# Create your views here.

def detail(request, id): # input에 원하는 id값을 넣어서 detail 함수를 실행
    post = get_object_or_404(Post, pk = id) # id 있나 확인하고 있으면 post에 넣어서 보내주고, 없으면 404
    # ??? pk ??? : primary key. 각 객체를 구분해주는 키 값.
    return render(request, 'main/detail.html',{'post':post})

def mainpage(request):
    posts = Post.objects.all() #변수 posts에 Post의 모든 객체를 저장 즉, posts에 모든 게시물이 담긴다.
    return render(request, 'main/mainpage.html', {'posts':posts}) # mainpage.html을 띄우는 함수

def secondpage(request):
    return render(request, 'main/secondpage.html') # secondpage.html을 띄우는 함수

def create(request): # 게시글 작성 요청
    new_post = Post() # 새 Post 정의
    new_post.title = request.POST['title'] # 새 Post의 타이틀 정의 
    new_post.writer = request.POST['writer'] # 새 Post의 작성자 정의
    new_post.pub_date = timezone.now() # 새 Post의 시간 (작성하는 현재시간) 정의
    new_post.body = request.POST['body'] # 새 Post의 내용 정의
    new_post.mood = request.POST['mood'] # 새 Post에 내 기분 정의
    new_post.weather = request.POST['weather'] # 새 Post에 오늘 날씨 정의

    new_post.save()
    return redirect('detail', new_post.id) # 게시글 작성이 끝나면 게시글의 detail을 볼 수 있도록 이동 -> read 파트에서 작성

# new.html에서 넘어옴. new.html을 띄우는 함수
def new(request):
    return render(request, 'main/new.html') # 경로 설정, Render : 템플릿을 불러옴
