try:
    with open ("c:/write.txt") as f:
        print(f.read())
        print(1/0)
except:
    print("ERROR")

try:
    print(1)
    assert 2+2==5
except AssertionError:
    print(3)
except:
    print(4)