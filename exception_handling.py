try:
    num1=7
    num2=0
    print(num1/num2)
    print("Done caculation")
except ZeroDivisionError:
    print("An error occurred")
    print("due to zero division")

try:
    num1=7
    num2=0
    print(num1/num2)
    print("Done caculation")
except :
    print("An error occurred")
    print("due to zero division")

try:
    print(10/2)
except ZeroDivisionError:
    print("ERROR")
print("Finished")

variable=10
print(variable+12)
print(type(variable))
print(variable/2)

print("finally","**"*23)
try:
    print("hello")
    print(1/0)
except ZeroDivisionError:
    print("Devided by Zero")
finally:
    print("this code will run no matter what")

print("finally","************************************************************************"*2)

try:
    print(1)
    print(10/0)
except ZeroDivisionError:
    print(unknown_var)
finally:
    print("this is excecuted last")

print("**raise","************************************************************************"*2)

print(111)
raise  ValueError
print(2)