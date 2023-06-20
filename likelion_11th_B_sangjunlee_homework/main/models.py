from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# 사용할 class 생성하기

class Post(models.Model): # 모델 class 명을 Blog에서 Post로 바꾸기
    title = models.CharField(max_length=200) # title : 최대 길이 200
    writer = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE) # writer : 최대 길이 100
    mood = models.CharField(max_length=20) # mood : 기분
    weather = models.CharField(max_length=20) # weather : 오늘 날씨
    pub_date = models.DateTimeField() # pub_date : 게시날짜
    body = models.TextField() # body : post의 body
    image = models.ImageField(upload_to="post/", blank=True, null=True)
    like = models.ManyToManyField(User, related_name='likes', blank=True)
    like_count = models.PositiveIntegerField(default=0)

    
    # 이후 termianl에 python manage.py makemigrations 입력 (앱 내에 migrations 폴더를 생성해 models.py의 변경사항을 저장)
    # 아마 이시점에 python manage.py migrate 를 안했을 수도 있음. 하기.

    # Post 내용이 호출되면 데이터의 title이 '대표값'으로 나오게 함. ??? 의것의 의도 ???
    def __str__(self):
        return self.title 
    
    # 내용이 너무 많으면 앞부분만 보이도록 body의 내용 앞부분을 자르기
    def summary(self):
        return self.body[:20] #body의 20번째 인덱스까지를 리턴

class Comment(models.Model):
    content = models.TextField()
    pub_date = models.DateTimeField()
    writer = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.post.title+" : "+self.content[:20]