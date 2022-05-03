# Язык HTML-тегов с помощью менеджера контекста.
# Реализовать классы для выполнения примера.

import contextlib


class HTML:
    def __init__(self):
        self.data = ''

    @contextlib.contextmanager
    def body(self):
        self.data += '<body>\n'
        yield
        self.data += '</body>\n'

    @contextlib.contextmanager
    def div(self):
        self.data += '<div>\n'
        yield
        self.data += '</div>\n'

    def p(self, content):
        self.data += '<p>{}</p>\n'.format(content)


def test():
    html = HTML()
    with html.body():
        with html.div():
            with html.div():
                html.p('Первая строка.')
                html.p('Вторая строка.')
            with html.div():
                html.p('Третья строка.')
    print(html.data)


test()