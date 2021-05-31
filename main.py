import sys

# @components.create_component_from_func
def op1():
    print("hello world")

# @components.create_component_from_func
def op2(device):
    print("complete " + device + " task") 

# locally
def hello_world_local():
    op1()
    op2("local")


# with k8s
def hello_world_k8s():
    # @dsl.pipeline(name='pipeline_hello_world')
    import kfp
    from kfp import components, dsl
    @components.create_component_from_func
    def get_op1():
        op1()

    @components.create_component_from_func
    def get_op2():
        op2("k8s")

    @dsl.pipeline(name='pipeline_hello_world')
    def my_pipeline():
        # get_op1 = components.create_component_from_func(op1)
        # get_op2 = components.create_component_from_func(op2)
        task1 = get_op1()
        task2 = get_op2()
        # get_op2.after(get_op1)
        task2.after(task1)

    kfp.compiler.Compiler().compile(my_pipeline, __file__ + '.yaml')


if __name__ == '__main__':
    if len(sys.argv)<2:
        hello_world_local()
    else:
        device = sys.argv[1]
        if device == "k8s":
            hello_world_k8s()
        elif device == "local":
            hello_world_local()
