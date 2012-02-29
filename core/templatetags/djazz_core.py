from django import template

register = template.Library()


class BlockNode(template.Node):
	def __init__(self, block_name):
		self.block = block_name
	
	def render(self, context):
		from djazz.core.models import Block
		try:
			b = Block.objects.get(name=self.block)
		except Block.DoesNotExist:
			pass
		return ""

def do_djazz_block(parser, token):
	try:
		tag_name, block_name = token.split_contents()
	except ValueError:
		raise template.TemplateSyntaxError("%r tag requires a single argument" % token.contents.split()[0])
	if not (block_name[0] == block_name[-1] and block_name[0] in ('"', "'")):
		raise template.TemplateSyntaxError("%r tag's argument should be in quotes" % tag_name)
	return BlockNode(block_name[1:-1])

register.tag('djazz_block', do_djazz_block)
