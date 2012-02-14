from django.conf import settings

def init():
	p = 'djazz.core.context_processors.sitenv'
	sp = settings.TEMPLATE_CONTEXT_PROCESSORS
	if p not in sp:
		sp = sp + (p,)
