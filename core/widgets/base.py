from django.template import Context, loader


class WidgetBase(type):
	def __new__(cls,name,bases,attrs):
		super_new = super(WidgetBase,cls).__new__
		parents = [b for b in bases if isinstance(b, WidgetBase)]
		if not parents:
			return super_new(cls, name, bases, attrs)
		module = attrs.pop('__module__')
		new_cls = super_new(cls,name,bases,{'__module__':module})
		fields = {}
		for attr in attrs:
			fields[attr] = attrs[attr]
		
		setattr(new_cls,'_fields',fields)
		
		return new_cls

class Widget(object):
	__metaclass__ = WidgetBase
	
	class Tpl:
		pass
	
	def __init__(self,*args,**kwargs):
		self.uid = self.__class__.__name__
		self.vars = {}
		widget = Widget.Tpl()
		for field in self._fields:
			setattr(widget,field,self._fields[field])
		setattr(widget,'__name__',self.uid)
		self.template = "djazz/widgets/"+self.uid+".html"
		self.widget = widget
	
	def add_var(self,var,value):
		self.vars[var] = value
	
	def pre_render(self):
		pass
	
	def render(self):
		self.pre_render()
		t = loader.get_template(self.template)
		self.add_var('widget', self.widget )
		c = Context(self.vars)
		return t.render(c)
