import sys

# locally
def hello_world_local():
    print("hello world local")
    print('complete task')

# with k8s
def hello_world_k8s():
    # set up k8s
    import kfp
    from kfp import components, dsl

    @components.create_component_from_func
    def get_op1():
        print('hello world k8s')

    @components.create_component_from_func
    def get_op2():
        print("complete task")

    @dsl.pipeline(name='pipeline_hello_world')
    def my_pipeline():
        task1 = get_op1()
        task2 = get_op2()
        task2.after(task1)

    kfp.compiler.Compiler().compile(my_pipeline, __file__ + '.yaml')

if __name__ == '__main__':
    if sys.argv[1] == "local":
        hello_world_local()
    elif sys.argv[1] == "k8s":
        hello_world_k8s()