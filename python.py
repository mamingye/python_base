print('hello world')

print('I"ll go to bed soon')  #comment on
print("I'll go to bed soon")  #comment on

#print("hello"      "   world")

#print ('2+2')
#10%3


#def apply_twice(func, arg):
#   return func(func(arg))

#def add_five(x):
#   return x + 5

#print(apply_twice(add_five, 10))


def add_five(x):
    return x+5

def apply_twice(func,arg):
    return func(func(arg))

print(apply_twice(add_five,10))

print(10**100)
print(100**10)
print(10**20)

#named function
def polynomial(x):
    return x**2+5*x+4
print(polynomial(-4))

#lambda
print((lambda x:x**2+5*x+4)(-4))


def add(x,y):
    return x+y
print(add(100,4))
print((lambda x,y,z,a:x+y+z+a)("1","1","zz","aaa"))

double=lambda x:x*2
print(double("xx:"))