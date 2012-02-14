# Create your views here.
from django.shortcuts import render
from djazz.posts.models import Post

def index(request):
	
	posts = Post.objects.all().order_by('date')
	return render(request,'blog/index.html',{'posts':posts})

def article(request,post_id):
	
	article = Post.objects.get(id=post_id)
	return render(request,'blog/article.html',{'article':article})
