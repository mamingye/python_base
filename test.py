#def print_nums(x):
#    for i in range(x):
#        print(i)
#        return i
#print_nums(10)


def func(x):
    res=0
    for i in range(x):
        print("qian",res)
        res+=i
        #print("hou",res)
    return i,res,x
print(func(4)) #reurn返回函数体中引用的多个变量的值

mmylist=[1,2,3,4] #方括号
mmytuple=(0,2,4,3,5,2) #圆括号tuple类型，数据处理快速，tuple中数据不能变化
mmyset={0,2,4,3,5,2} #花括号
print(type(mmylist))
print(type(mmytuple))
print(type(mmyset))
print(mmytuple[0])
print(mmylist[3])
print("******")
mmylist.remove(5)
print(mmylist)
mmytuple.remove(2)
print(mmytuple)