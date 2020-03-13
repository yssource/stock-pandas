from .parser import Parser
from .factory import create_by_node

def parse(directive_str: str, cache):
    directive_str = directive_str.strip()

    cached = cache.get(directive_str)
    if cached:
        return cached

    ast = Parser(directive_str).parse()

    directive, _ = create_by_node(ast, directive_str, cache)

    cache.set(directive_str, directive)

    return directive

