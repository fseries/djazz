from django import forms
from djazz.posts.models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		exclude = ('author','type','last_editor','uid','status','parent')


class PostFormAnonymous(PostForm):
	name = forms.CharField(max_length=50)
	captcha	= forms.CharField(max_length=10)