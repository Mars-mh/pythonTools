from functools import singledispatch
from collections import abc
import numbers
import html


@singledispatch
def htmlize(obj):
    escape = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(escape)


@htmlize.register(str)
def _(text):
    escape = html.escape(text).replace('\n', '<br>\n')
    return '<p>{}</p>'.format(escape)


@htmlize.register(numbers.Integral)
def _(n):
    return '<pre>{0} (0x{0:x})</pre>'.format(n)


@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n</ul>'


if __name__ == '__main__':
    print(htmlize({1, 2, 3}))
    print(htmlize(abs))
    print(htmlize(42))
    print(htmlize('mars!'))
    print(htmlize([1, 3, 'cat', 'dog']))


