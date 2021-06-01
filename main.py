import sys
from new_decorator import my_decorator

global dev 
if len(sys.argv)<2:
    dev = "local"
else:
    dev = sys.argv[1]
# dev = "k8s"

flist = []

@my_decorator(device = dev, funcs = flist, flag = 0)
def op1():
    print("hello world")

@my_decorator(device = dev, funcs = flist, flag = 1)
def op2():
    print("complete task")

if __name__ == '__main__':
    op1()
    op2(dev)
