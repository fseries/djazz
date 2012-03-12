from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import password_change
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from djazz.contrib.profiles.forms import ProfileChangeForm

@login_required
def index(request):
    return render(request,'djazz/profiles/view.html',{})


def edit(request):
    if request.method == 'POST':
        form = ProfileChangeForm(request.POST,instance=request.user)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('djazz.contrib.profiles.views.index'))
    else:
        form = ProfileChangeForm(instance=request.user)
    
    return render(request,'djazz/profiles/edit.html',{'form':form})

