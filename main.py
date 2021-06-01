import sys
from new_decorator import my_decorator

global dev 
if len(sys.argv)<2:
    dev = "local"
else:
    dev = sys.argv[1]
# dev = "k8s"

@my_decorator(device = dev)
def op1():
    print("hello world")
    print(op1.__name__)

def op2(dev):
    print("complete " + dev + " task")

if __name__ == '__main__':
    op1()
