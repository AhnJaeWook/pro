from django.shortcuts import render
from .models import Blog
from django.shortcuts import render, get_object_or_404, redirect # redirect를 쓰기 위해 소환!
from django.utils import timezone # timezone을 쓰기 위해 소환!
# Create your views here.
def home(request):
    blog = Blog.objects.all()

    return render(request, 'home.html', {'blog':blog})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog() # 이렇게하면 class의 틀이 들어간다
    blog.title = request.GET['title'] # class 틀에 title 제목에 썼던 데이터를 넣는다
    blog.body = request.GET['body'] # class 틀에 body 본문에 썼던 데이터를 넣는다
    blog.pub_date = timezone.datetime.now() # 현재 시간을 넣는다.
    blog.save() # DB에 저장
    return redirect('/') # 바로 출력