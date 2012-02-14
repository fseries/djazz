from djazz.core.models import Config

def sitenv(request):
    try:
        title = Config.objects.get(key='site_title').value
    except Config.DoesNotExist:
        title = None
    try:
        slogan = Config.objects.get(key='site_slogan').value
    except Config.DoesNotExist:
        slogan = None
    
    return {
        'site_title': title,
        'site_slogan': slogan,
    }
