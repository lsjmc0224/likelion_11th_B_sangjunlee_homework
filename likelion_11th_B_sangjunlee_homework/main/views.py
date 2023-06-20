from django.shortcuts import render, redirect, get_object_or_404 # Render : 템플릿을 불러옴, Redirect : URL로 이동, get_object_or_404 : 가져올 객체가 있으면 가져오고 없으면 404에러를 띄움
from .models import Post, Comment # 아깐 admin창에서 보이기 위해 불러왔다면, 여기는 views에 보여주기 위해 불러옴
from django.utils import timezone # 장고에서 제공하는 시간 관련 기능 사용
# Create your views here.
def mainpage(request):
    posts = Post.objects.all() #변수 posts에 Post의 모든 객체를 저장 즉, posts에 모든 게시물이 담긴다.
    return render(request, 'main/mainpage.html', {'posts':posts}) # mainpage.html을 띄우는 함수

def secondpage(request):
    return render(request, 'main/secondpage.html') # secondpage.html을 띄우는 함수
#=================================================================================================
def create(request):
    if request.user.is_authenticated:
        new_post = Post() # 새 Post 정의
        new_post.title = request.POST['title'] # 새 Post의 타이틀 정의 
        new_post.writer = request.user # 새 Post의 작성자 정의
        new_post.pub_date = timezone.now() # 새 Post의 시간 (작성하는 현재시간) 정의
        new_post.body = request.POST['body'] # 새 Post의 내용 정의
        new_post.mood = request.POST['mood'] # 새 Post에 내 기분 정의
        new_post.weather = request.POST['weather'] # 새 Post에 오늘 날씨 정의
        new_post.image = request.FILES.get('image')
        new_post.save()
        # 본문의 내용을 띄어쓰기로 잘라낸다.
        words = new_post.body.split(' ')
        # 만약 단어가 공백이 아니고 #로 시작하면, #를 뗀 후 tag_list에 저장한다.
        return redirect('main:detail', new_post.id)
    #로그인 안했냐 로그인하러 가라
    else:
        return redirect('accounts:login')
# new.html에서 넘어옴. new.html을 띄우는 함수
def new(request):
    return render(request, 'main/new.html') # 경로 설정, Render : 템플릿을 불러옴
#=================================================================================================
def detail(request, id):
    # id 있나 확인하고 있으면 post에 넣어서 보내주고, 없으면 404
    post = get_object_or_404(Post, pk = id)
    # ??? pk ??? : primary key. 각 객체를 구분해주는 키 값.
    if request.method =='GET':
        comments = Comment.objects.filter(post=post)
        return render(request, 'main/detail.html',{
            'post':post,
            'comments':comments,
            })
    elif request.method=="POST":
        new_comment = Comment()
        # foreignkey > blog 객체 직접 넣어주기
        new_comment.post = post
        # foreignkey > reqeust.user 직접 넣어주기
        new_comment.writer = request.user
        new_comment.content = request.POST['content']
        new_comment.pub_date = timezone.now()
        new_comment.save()
        return redirect('main:detail', id)
    return render(request, 'main/detail.html',{'post':post})
#=================================================================================================
def update(request, id):
    if request.user.is_authenticated:
        update_post = Post.objects.get(id=id)
        if request.user ==  update_post.writer:
            update_post.title = request.POST['title']
            update_post.writer = request.user
            update_post.pub_date = timezone.now()
            update_post.body = request.POST['body']
            update_post.mood = request.POST['mood'] # 새 Post에 내 기분 정의
            update_post.weather = request.POST['weather'] # 새 Post에 오늘 날씨 정의
            update_post.image = request.FILES.get('image', update_post.image)

            update_post.save()
            return redirect('main:detail', update_post.id)
    return redirect('accounts:login')

def edit(request, id):
    edit_post = Post.objects.get(id=id)
    return render(request, 'main/edit.html', {'post' : edit_post})
#=================================================================================================
def delete(request, id):
    delete_post = Post.objects.get(id=id)
    delete_post.delete()
    return redirect('main:mainpage')

def delete_comment(request, id, com_id):
    delete_com = Comment.objects.get(id = com_id)
    delete_com.delete()
    return redirect('main:detail', id)

def pic_delete(request, id):
    post_pic_delete = Post.objects.get(id=id)
    post_pic_delete.image.delete()
    return redirect('main:edit',post_pic_delete.id)
#================================================================================================
def likes(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.like.all():
        post.like.remove(request.user)
        post.like_count -= 1
        post.save()
    else:
        post.like.add(request.user)
        post.like_count += 1
        post.save()
    return redirect('main:detail', post_id)