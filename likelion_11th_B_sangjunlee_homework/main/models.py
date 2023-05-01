from django.db import models

# Create your models here.
# 사용할 class 생성하기

class Blog(models.Model):
    title = models.CharField(max_length=200) # title : 최대 길이 200
    writer = models.CharField(max_length=100) # writer : 최대 길이 100
    pub_date = models.DateTimeField() # pub_date : 게시날짜
    body = models.TextField() # body : blog의 body
    # 이후 termianl에 python manage.py makemigrations 입력 (앱 내에 migrations 폴더를 생성해 models.py의 변경사항을 저장)
    # 아마 이시점에 python manage.py migrate 를 안했을 수도 있음. 하기.

    # Blog 내용이 호출되면 데이터의 title이 '대표값'으로 나오게 함. ??? 의것의 의도 ???
    def __str__(self):
        return self.title 
    
    # 내용이 너무 많으면 앞부분만 보이도록 body의 내용 앞부분을 자르기
    def summary(self):
        return self.body[:20] #body의 20번째 인덱스까지를 리턴
    