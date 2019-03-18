print("**raise","************************************************************************"*2)
try:
    print(1/0)
except ZeroDivisionError:
    raise ValueError
#**raise ***命令输出如下，很遗憾忘记了多行注释如何操作*********************************************************************************************************************************************
#    print(1/0)
#ZeroDivisionError: division by zero#

#During handling of the above exception, another exception occurred:

#Traceback (most recent call last):
#  File "C:/Users/Administrator/PycharmProjects/pythonpractise/raise.py", line 12, in <module>
#    raise ValueError
#ValueError
