from django.conf import settings
from djazz.core.models import Config


def getConfigVar(var,section=None,**options):
	""" getConfigVar
	 
	 Options: site_id, default_value
	 
	 Return the config var defined by var,section, and site_id
	 If no config var is defined by the requested site_id, this function
	return the default config var, which is associated with no site
	 If no config var is found, this function return a Config object,
	with value = default_value defined by user
	"""
	
	for key in ('site_id','default_value'):
		if key not in options:
			options[key] = None
	
	if options['site_id'] == None:
		if 'SITE_ID' in dir(settings):
			options['site_id'] = settings.SITE_ID
	
	globalconf = Config.objects.filter(key=var,section=section)
	
	## Site filter
	if options['site_id']:
		conf = globalconf.filter(site__id__exact=options['site_id'])
	else:
		conf = globalconf.filter(site = None)
	
	if conf.count() == 0 and options['site_id']:
		conf = globalconf.filter(site = None)
	
	if conf.count() > 0:
		conf = conf[0]
	else:
		conf = Config(
			key=var,
			section=section,
			site=None,
			value=options['default_value']
		)
	return conf
