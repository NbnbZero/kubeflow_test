from kfp import dsl,components
import kfp
from functools import wraps
def my_decorator(device, funcs, flag):
    def decorate(func):
        if device == "local":
            @wraps(func)
            def wrapper(*args):
                func(*args)
        elif device == "k8s":
            if flag == 0:
                @wraps(func)
                def wrapper(*args):
                    funcs.append(func)
            else:
                @wraps(func)
                def wrapper(*args):
                    funcs.append(func)
                    @dsl.pipeline(name='pipeline_hello_world')
                    def my_pipeline():
                        tasks = []
                        i = 0
                        for f in funcs:
                            tasks.append(components.create_component_from_func(f)())
                            if i > 0:
                                tasks[i].after(tasks[i-1])
                            i += 1
                    kfp.compiler.Compiler().compile(my_pipeline, __file__ + '.yaml')
        return wrapper
    return decorate
