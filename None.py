def func1():
    print("Hi")
var=func1()
print(var)


foo=print()
if foo == None:
    print(1)
else:
    print(2)


def test(func,arg):
    return func(func(arg))
def mult(x):
    return x*x
print(test(mult,2))
mult(mult(2))