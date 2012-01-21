from django.http import HttpResponseRedirect
from django.shortcuts import render



def index(request):
    from djazz.posts.models import Post
    
    posts = Post.objects.filter(type__name='forum',parent=None).order_by('-date')
    
    return render(request,'forum/index.html',{'posts':posts})


def topic(request, topic):
    from django.db.models import Q
    from djazz.posts.models import Post
    
    posts = Post.objects.filter(type__name='forum')
    posts = posts.filter(Q(uid=topic)|Q(parent__uid=topic))
    posts = posts.order_by('date')
    
    return render(request,'forum/view.html',{'posts': posts} )


def new(request,topic=None):
    from django.db.models import Q
    from django.core.urlresolvers import reverse
    from djazz.posts.models import Post,Type
    from djazz.forum.forms import PostForm,PostFormAnonymous
    

    init = {}
    parent = None
    posts = None
    preview = None
    
    if topic:
        parent = Post.objects.get(uid=topic)
        init['parent'] = parent
        init['title'] = '[RE] ' + parent.title
        
        posts = Post.objects.filter(type__name='forum')
        posts = posts.filter(Q(uid=topic)|Q(parent__uid=topic))
        posts = posts.order_by('-date')
    
    if request.method == 'POST':
        if request.user.is_authenticated():
            form = PostForm(request.POST)
        else:
            form = PostFormAnonymous(request.POST)
        
        if form.is_valid():
            
            if request.POST['submit'] == 'Preview':
                preview = form.save(commit=False)
            else:
                post = form.save(commit=False)
                post.author = request.user
                post.last_editor = request.user
                post.status = 'public'
                post.type = Type.objects.get(name='forum')
                post.parent = parent
                post.save()
                return HttpResponseRedirect( reverse('djazz.forum.views.index') )
    else:
        if request.user.is_authenticated():
            form = PostForm(initial=init)
        else:
            form = PostFormAnonymous(initial=init)
    
    return render(request,'forum/new.html', {
        'form': form,
        'posts': posts,
        'preview': preview,
        'topic': topic
    })
