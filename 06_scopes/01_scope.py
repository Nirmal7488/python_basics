x=99

# def func():
#     global x
#     x=12

# func()
# print(x)

def fun1():
    x=88
    def fun2():
        print(x)
    return fun2

res=fun1()
res()
print(res)