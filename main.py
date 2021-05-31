import sys

def hello_world_local():
    print("hello world local")


if __name__ == '__main__':
    if len(sys.argv)<2:
        hello_world_local()
    # elif sys.argv[1] == "k8s":