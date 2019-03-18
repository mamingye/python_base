nums=[55,44,33,22,11]
if all([i>5 for i in nums]):
    print("all is larger than 5")


if any([i%2==0 for i in nums]):
    print("At least one is even")

for v in enumerate(nums):
    print(v)

print(enumerate(nums))



###########################################################

def count_char(text,char): #定义函数
    count=0
    for c in text: #循环取值
        #print(c)
        if c ==char:#进行判断
            count+=1 #处理
    return count  #返回值

filename=input("输入一个文件名:")
with open(filename) as f:   #处理文件
    text = f.read()
print(count_char(text,"b"))   #print(count_char(filename,"b"))写成filename

###########################################################
for char in "abcdefghijklmnopqrstuvwxyz ":
    perc=100*count_char(text,char)/len(text)
    print("{0}-{1}".format(char,round(perc,2)))
