# x=99

# def func():
#     global x
#     x=12

# func()
# print(x)

# def fun1():
#     x=88
#     def fun2():
#         print(x)
#     return fun2

# res=fun1()
# res()
# print(res)

def chaicoder(num):
    def actual(x):
        return x**num
    return actual

f=chaicoder(2)
g=chaicoder(3)

print(f(4))
print(g(5))