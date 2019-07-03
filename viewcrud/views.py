from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Blog
from .forms import NewBlog

def welcome(req):
    return render(req, 'viewcrud/index.html')

def read(req):
    blogs = Blog.objects.all()
    return render(req, 'viewcrud/funccrud.html', {'blogs':blogs})

def create(req):
    # 새로운 데이터 새로운 블로그 글 저장하는 역할 == POST
    if req.method == 'POST':
        # 입력된 글 저장하기
        form = NewBlog(req.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')

    #  글쓰기 페이지를 띄워주기 == GET
    else:
        # 단순히 입력받을 수 있는 form을 띄워준다.
        form = NewBlog()
        return render(req, 'viewcrud/new.html', {'form':form})

def update(req, pk):
    # 어떤 블로그를 수정할지 블로그 객체를 가지고 온다.
    blog = get_object_or_404(Blog, pk = pk)

    # 해당하는 블로그 객체(instance) pk에 맞는 입력공간
    form = NewBlog(req.POST, instance=blog)
    
    if form.is_valid():
        form.save()
        return redirect('home')

    return render(req, 'viewcrud/new.html', {'form':form})

def delete(req, pk):
    blog = get_object_or_404(Blog, pk = pk)
    blog.delete()
    return redirect('home')