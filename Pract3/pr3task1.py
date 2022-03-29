with open ('file.dat') as f: # whitespace before '('
    contents = f.read()

age=0   # missing whitespace around operator
if age>15:  # missing whitespace around operator
    print('Can drive')

my_tuple = 1,2,3 # missing whitespace after ','

def func(key1 = 'val1', # unexpected spaces around keyword / parameter equals;  expected 2 blank lines, found 1 (выше)
         key2 = 'val2'):
    return key1, key2


x = 0
if x > 5: y = 10 # Multiple statements on one line (colon)

from gevent import monkey; monkey.patch_all()   # Multiple statements on one line (semicolon)

var = None
if var != True:   # comparison to True should be 'if cond is True:' or 'if cond:'
    print("var is not equal to True")
if var == None:  # Comparison to None should be 'cond is None:'
    print("var is equal to None")



