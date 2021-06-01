import sys


# define 1st function
def func1():
    print("hello world")


# define 2nd function
def func2(device):
    print("complete " + device + " task")


# locally
def hello_world_local():
    func1()
    func2("local")


# with k8s
def hello_world_k8s(filename):

    import kfp
    from kfp import components, dsl

    # get containerOps from functions
    @components.create_component_from_func
    def get_op1():
        func1()

    @components.create_component_from_func
    def get_op2():
        func2("k8s")

    @dsl.pipeline(name='pipeline_hello_world')
    def my_pipeline():
        task1 = get_op1()
        task2 = get_op2()
        task2.after(task1)

    kfp.compiler.Compiler().compile(my_pipeline, filename + '.yaml')


# can be used as decorator for user to switch between local / k8s
def helper(func):
    def wrapper(*args, **kwargs):
        device = sys.argv[1]
        if device == "k8s":
            hello_world_k8s(*args, **kwargs)
        elif device == "local":
            hello_world_local()
        return func(*args, **kwargs)
    return wrapper
