try:
    print(0)
    num=5/0
    print(1)
except (ValueError,TypeError,ZeroDivisionError):
    print("An ValueERROR occurred")
except ZeroDivisionError:
    print("2An ZeroDivisionERROR occurred")
v = 10
b=20
print(b/2)
print(v/2)
