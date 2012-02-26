# Create your views here.
from django.shortcuts import render
from djazz.contrib.posts.models import Post,PostVar

def index(request):
	
	posts = Post.objects.all().order_by('date')
	cats = PostVar.objects.filter(
			key='category').order_by(
			'key').only(
			'value').distinct()
	return render(request,'djazz/blog/index.html',{'posts':posts,'categories':cats})

def article(request,post_id):
	
	article = Post.objects.get(id=post_id)
	return render(request,'djazz/blog/article.html',{'article':article})
