from kfp import dsl,components
import kfp
def my_decorator(device):
    def decorate(func):
        if device == "local":
            def wrapper():
                func()
        elif device == "k8s":
            def wrapper():
                @dsl.pipeline(name='pipeline_hello_world')
                def my_pipeline():
                    task = components.create_component_from_func(func)()
                kfp.compiler.Compiler().compile(my_pipeline, __file__ + '.yaml')
        return wrapper
    return decorate
