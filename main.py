import sys
import kfp
from kfp import components, dsl


@dsl.component
def get_op1():
    print('hello world')


@components.create_component_from_func
def get_op2():
    print("complete task")


# locally
def hello_world_local():
    get_op1()
    get_op2()


# with k8s
def hello_world_k8s():
    @dsl.pipeline(name='pipeline_hello_world')
    def my_pipeline():
        task1 = get_op1()
        task2 = get_op2()
        task2.after(task1)

    kfp.compiler.Compiler().compile(my_pipeline, __file__ + '.yaml')


if __name__ == '__main__':
    device = sys.argv[1]
    if device == "k8s":
        hello_world_k8s()
    elif device == "local":
        hello_world_local()
