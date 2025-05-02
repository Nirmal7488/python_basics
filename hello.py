import dis

def loop_example():
    for i in [10, 20, 30]:
        print(i)

dis.dis(loop_example)

