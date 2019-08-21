from django import template
import datetime

from sekizai.helpers import get_varname

register = template.Library()


class SekizaiContextNode(template.Node):
    def __init__(self, block_name):
        self.block_name = block_name

    def render(self, context):
        print(context[get_varname()])

        seq = context[get_varname()][self.block_name]
        return seq.data


def sekizai_context(parser, token):
    tag_name, block_name = token.split_contents()
    return SekizaiContextNode(block_name[1:-1])


register.tag('sekizai_context', sekizai_context)


class SekizaiContextInsertNode(template.Node):
    def __init__(self, block_name, thingie):
        self.block_name = block_name
        self.thingie = thingie

    def render(self, context):
        seq = context[get_varname()][self.block_name]
        seq.data += [self.thingie]
        return ""


def sekizai_context_insert(parser, token):
    tag_name, block_name, thingie = token.split_contents()
    # to strip quotes
    # just a test don't kill meh
    return SekizaiContextInsertNode(block_name[1:-1], thingie[1:-1])

register.tag('sekizai_context_insert', sekizai_context_insert)