import sys

def hello_world_local():
    print("hello world local")

def hello_world_k8s():
    # set up k8s 
    print("hello world k8s")

if __name__ == '__main__':
    if len(sys.argv)<2:
        hello_world_local()
    elif sys.argv[1] == "local":
        hello_world_local()
    elif sys.argv[1] == "k8s":
        hello_world_k8s()