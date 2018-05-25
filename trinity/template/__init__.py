import re
from jinja2 import Environment, PackageLoader

class Jinja2:
    """
    Jinja2 templating wrapper
    """
    def __init__(self, tpls_dir):
        self.jinja2_env = Environment(
            loader=PackageLoader("app", tpls_dir),
            autoescape=True)

    def render(self, name, **ctx):
        t = self.jinja2_env.get_template(name)
        return t.render(ctx)

def to_regex(template):
    """
    Converts string to templated regex
    """
    regex = ''
    var_regex = re.compile(r'''\{(\w+)(?::([^}]+))? \}''', re.VERBOSE)
    last_pos = 0
    for match in var_regex.finditer(template):
        regex += re.escape(template[last_pos:match.start()])
        var_name = match.group(1)
        expr = match.group(2) or '[^/]+'
        expr = '(?P<%s>%s)' % (var_name, expr)
        regex += expr
        last_pos = match.end()
    regex += re.escape(template[last_pos:])
    regex = '^%s$' % regex
    return regex
