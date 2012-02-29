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
		name = self.__class__.__name__
		_widget = Widget.Tpl()
		for field in self._fields:
			setattr(_widget,field,self._fields[field])
		setattr(_widget,'__name__',self.__class__.__name__)
		self.template = "djazz/widgets/"+_widget.__name__+".html"
		self._widget = _widget
	
	def render(self):
		t = loader.get_template(self.template)
		c = Context({'widget' : self._widget })
		return t.render(c)
		

class HelloWorld(Widget):
	name = "HelloWorld Widget"
	version = "0.1"
