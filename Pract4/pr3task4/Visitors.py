# Реализовать класс-посетитель PrintVisitor для печати выражения.
# Обойтись без операторов ветвления.
class PrintVisitor:
    def visit(self, expression):
        return expression


# Реализовать класс-посетитель CalcVisitor для вычисления выражения.
# Обойтись без операторов ветвления.
class CalcVisitor:
    def visit(self, expression):
        return expression.count()


# Реализовать класс-посетитель StackVisitor для порождения кода стековой машины по выражению.
# Обойтись без операторов ветвления.
class StackVisitor:
    def visit(self, expression):
        expression.stack()
