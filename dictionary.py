try:
    ages = {"1": 111,
            "2": 231123,
            "4": 4213441,
            "9": 90123138,
            "11": 11111,
            "1": [1111],
            "1":[2222222],
            "orange":[2,3,4,5]}
    print(ages["9"])
    print(ages["4"])
    # print(ages["5"])
    print(ages["a"])
except:
    print(1)

#为key "1" 和 1 赋值
ages[1]=212121
#ages["1"]="啊"
print(ages)
#判断key是否存在于dictionary中
print("判断1是否在dictionary中",'1' in ages)
print('3' in ages)
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
print(ages["1"])
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
print(ages.get("orange"))
print(ages.get("4"))
print(ages.get("orang"))
print(ages.get("orang","Here is No value"))
#print(ages.get("1",0)+ages.get("21","a"))
my_tuple=("111","222","333","444")
print(my_tuple[::-1])


#string formatting
nums=[4,50,"asc"]
msg="Numbers:{0}{2}{1}".format(nums[0],nums[2],nums[1])
print(msg)

a="{x},{y},{a}".format(x=2,a=10,y=5)
_a_="{x}{y}{a}".format(x=2,a=10,y=5)
print(a)
print(_a_)