from djazz.core.widgets.base import Widget

class WidgetManager(object):
    
    def __init__(self):
        self.w_reg = {}
    
    def register(self,widget):
        if not issubclass(widget, Widget):
            raise TypeError("Not a Widget object")
        
        if widget.__name__ in self.w_reg:
            raise Exception("Widget "+widget.__name__+" is already register")
        
        self.w_reg[widget.__name__] = widget

manager = WidgetManager()