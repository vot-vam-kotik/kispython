from Pract4.pr3task4.Add import Add
from Pract4.pr3task4.Mul import Mul
from Pract4.pr3task4.Num import Num
from Pract4.pr3task4.Visitors import PrintVisitor, CalcVisitor, StackVisitor

ast = Add(Num(7), Mul(Num(3), Num(2)))
pv = PrintVisitor()
cv = CalcVisitor()
sv = StackVisitor()
print(pv.visit(ast))
print(cv.visit(ast))
sv.visit(ast)
