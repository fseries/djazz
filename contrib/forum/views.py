from django.http import HttpResponseRedirect
from django.shortcuts import render



def index(request,parent=None):
    from djazz.forum.models import Forum
    from djazz.posts.models import Post
    
    if not parent:
        forums = Forum.objects.filter(parent = None)
        return render(request,'forum/index.html',{'forums':forums})
    else:
        forums = Forum.objects.filter(parent__id = parent)
        for forum in forums:
            forum.topics = Post.objects.filter(postvar_post__key='forum',postvar_post__value=forum.id,parent=None)
        
    return render(request,'forum/forums.html',{'forums':forums})


def topic(request, topic):
    from django.db.models import Q
    from djazz.posts.models import Post
    
    posts = Post.objects.filter(type__name='forum')
    posts = posts.filter(Q(id=topic)|Q(parent=topic))
    posts = posts.order_by('date')
    
    return render(request,'forum/topic.html',{'posts': posts} )



def create(request,forum=None,topic=None):
    from django.core.urlresolvers import reverse
    from djazz.posts.models import Post,PostVar,Type
    from djazz.forum.models import Forum
    from djazz.forum.forms import PostForm,PostFormAnonymous
    
    init = {}
    posts = None
    preview = None
    
    if forum:
        forum = Forum.objects.get(id=forum)
        topic = None
    
    if topic:
        topic = Post.objects.get(id=topic)
        forum = Forum.objects.get(id=topic.postvar_post.get(key='forum').value)
    
    if topic:
        posts = Post.objects.filter(parent=topic).order_by('-date')
        init['parent'] = topic
        init['title'] = '[RE] ' + topic.title
    
    # Le formulaire a ete soumis
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
                post.parent = topic
                post.save()
                PostVar(post=post,key='forum',value=forum.id).save()
                return HttpResponseRedirect( reverse('djazz.forum.views.index') )
    else:
        if request.user.is_authenticated():
            form = PostForm(initial=init)
        else:
            form = PostFormAnonymous(initial=init)
    
    return render(request,'forum/create.html', {
        'form': form,
        'posts': posts,
        'preview': preview,
        'topic': topic,
        'forum' : forum
    })

def edit(request,post):
    
    return render(request,'forum/edit.html')
