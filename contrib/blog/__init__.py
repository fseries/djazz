from djazz.contrib.posts.signals import types_choice
from django.dispatch import receiver


@receiver(types_choice)
def type_blog(sender,**kwargs):
    types = kwargs['types_list']
    types.append(['blog','Blog'])
