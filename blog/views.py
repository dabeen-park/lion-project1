from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .forms import BlogForm 
# Create your views here.
#all get order_by exclude  이밖에도 여러가지 메소드가 있다.
def home(request):
    blogs = Blog.objects.order_by('-pub_date')
    search = request.GET.get('search')
    if search == 'true': #서치라는 정보가 오면
        author = request.GET.get('writer')
        blogs = Blog.objects.filter(writer=author).order_by('-pub_date') #작성자와 author이 같은것만 가져오게 한다.
        return render(request, 'home.html', {'blogs':blogs})

    paginator = Paginator(blogs, 3) #3개씩 쪼개서 보낼 것임
    page = request.GET.get('page') #get방식이 없을떄도 페이지가 넘어가도록  
    blogs = paginator.get_page(page) #그 페이지에 해당하는 내용을 보여주는 것
    return render(request, 'home.html',{'blogs':blogs})


def detail(request, id):
    blog = get_object_or_404(Blog, pk = id)
    return render(request, 'detail.html', {'blog':blog})

def new(request):
    form =BlogForm()
    return render(request,'new.html', {'form':form})

def create(request):
    form= BlogForm(request.POST, request.FILES)
    if form.is_valid():
        new_blog =form.save(commit=False)
        new_blog.pub_date = timezone.now()
        new_blog.save()
        return redirect('detail', new_blog.id)
    return redirect('home')

def edit(request, id):
    edit_blog = Blog.objects.get(id=id)
    return render(request, 'edit.html', {'blog':edit_blog})


def update(request, id):
    update_blog = Blog.objects.get(id=id)
    update_blog.title = request.POST['title']
    update_blog.writer = request.POST['writer']
    update_blog.body = request.POST['body']
    update_blog.pub_date = timezone.now()
    update_blog.save()
    return redirect('detail', update_blog.id)


def delete(request, id):
    delete_blog = Blog.objects.get(id=id)
    delete_blog.delete()
    return redirect('home')
