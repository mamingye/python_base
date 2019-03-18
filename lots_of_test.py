x=3
if x==4:
    print("yes")
else :
    print("No")

print(x)


print('---if-else','---'*25)

y=5
if y==123:
    print("number is 123")
else:
    if y==3:
        print("number is 3")
    else:
            if y==5:
                print("number is 5")
            else:
                print('number isn`t 123,3,or 7')

print('---if','---'*25)
##if 和elif区别实验
num=7
if num==5:
    print("number is 5")
if num==11:
    print("number is 11")
if num==7:
    print("number is 7")
if num==7:
    print("number is 7 again")
if num==7:
    print("number is 7 third times")
else:
    print("number isn't 5,11 or 7")


print('---elif','---'*23)

num=7
if num==5:
    print("number is 5")
elif num==11:
    print("number is 11")
elif num==7:
    print("number is 7")
elif num==7:
    print("number is 7 again")
elif num==7:
    print("number is 7 third times")
else:
    print("number isn't 5,11 or 7")

print("---while",23*"---")

i=1
while i<=5:
    print(i)
    i=i+1
print("Finished")

print("---break","---"*23)
i=0
while 1==1:
    print(i)
    i=i+1
    if i>=5:
        print('it`s time to have a break')
        break
print("---list","---"*23)
words=['w','o','l']
print(words[0])
print(words[1])
print(words[2])
print("---","---"*23)
nums=[5,4,3,2,1,]
print(nums[4])
print("---","---"*23)
nums_2=[]
print(nums_2)

print("---","---"*23)

number=3
things=["thins",0,[1,2,number,[number*3]],4]
print(things[2])
print([things[2][2]])
print([things[2][3]])

print("---","---"*23)

number=3
things=["thins",0,[1,2,number,],4]
print(things[2])
print([things[2][2]])

print("---lis","---"*23)

string="hello world"
print(string)
print(string[4],string[5],string[6])

print("---","---"*23)

nums=[2,3,4,5,6,7,]
nums[3]=100
nums[4]=nums[5]
print(nums)
print(nums[4])

print("---","---"*23)

nums=[1,2,3,]
print(nums+[4,5,6])
print(nums*3)

print("---","---"*23)

words=["spam","egg","spam","sausage"]
if "spam" in words:
    print("spam" in words)
    print ("sapm in words")

print("---","---"*23)

nums=[1,2,3]
print(not 4 in nums)
print(4 not in nums)
print(not 3 in nums)
print(3 not in nums)
nums.append(4)
print(nums)
print(len(nums))

print("---","---"*23)
words=["python","fun"]
index=1
words.insert(index,"is")
print(words)


print("---","---"*23)
for i in range(10):
    if not i%2==0:
        print(i+1)
print("---","---"*23)


def my_func():
    print(input("please input the number:"))
    print(input("please input the number:"))
    print(input("please input the number:"))
print("---","---"*23)
my_func()

print("---def_func","---"*23)
def print_with_exclamation(word):
    print(word+"!")
print_with_exclamation("spam")
print_with_exclamation("eggs")
print_with_exclamation("python")
print("---def_func-two-arguments","---"*23)
def print_sum_twice(x,y):
    print(x+y)
    print(x+y)
print_sum_twice(5,8)
print("---variable_out_of_func","---"*23)
def function(variable):
    variable+=1
    print(variable)
function(8)

print("---variable_out_of_func","---"*23)
def even(x):
    if x%2==0:
        print("Yes")
    else:
        print("No")
even(10)

print("---func_name_","---"*23)
def multiply(x,y):
    return x*y
a=4
b=7
operation=multiply
print(operation(a,b))

print("---func_name_","---"*23)
def add(x,y):
    return x+y
def do_twice(func,x,y):
    return func(func(x,y),func(x,y))
a=5
b=10
print(do_twice(add,a,b))

print("---func_as_an_arguments","---"*23)
def square(x):
    return x*x
'''
引用函数square作为参数
'''
#引用函数squa作为test函数参数
def test(function,x):
    print(function(x))

test(square,5)
print("---module","---"*23)
import random
for i in range(10):  #这里不熟悉
     value = random.randint(1,600) #这里不熟悉
     print(value)
print("---review-for-loop","---"*23)
for i in range(3):
    print (1)
print("--import-module-function","---"*23)
import math
num=10
print(math.sqrt(num))
print(math.pi)
print("---from-module-import","---"*23)
from math import pi,sqrt
print(pi,math.tan(10))

print("---module-function","---"*23)
import math
print(math.cos)

print("---import-mod4ule-function-as","---"*23)
from math import sqrt as square_root
print(square_root(100))
print(math.sqrt(100))
print("---import-mod4ule-function-as","---"*23)
import math as m
print(math.sqrt(25))
print("---","---"*23)

DOWN=float(input("请输入下行流量(GB):"))
UP=float(input("请输入上行流量(GB):"))
mins=float(input("请输入时间段(分钟):"))
DOWN_SPEED=float((DOWN*8*10**9)/(mins*60*10**6))
UP_SPEED=float((UP*8*10**9)/(mins*60*10**6))
print("**"*23)
print("下行速率(Mbps):",DOWN_SPEED)
print("上行速率(Mbps):",UP_SPEED)
print("**"*23)