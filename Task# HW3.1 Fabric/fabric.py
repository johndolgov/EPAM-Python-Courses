"""
This module presents decorators fabric
"""
import functools


def on_of_switcher(func):
    """
    Function which switch on and off
    :param func: function with on/off switch
    :return: func
    """
    func.is_on = True

    def on():
        func.is_on = True

    def off():
        func.is_on = False

    func.on = on
    func.off = off
    return func


def decorator_with_args(decorator):
    """

    :param decorator:
    :return:
    """
    @functools.wraps(decorator)
    def wrapper(*args, **kwargs):
        def inner_decorator(func):
            result = decorator(func, *args, **kwargs)
            functools.update_wrapper(result, func)
            return result
        return inner_decorator
    return wrapper


@on_of_switcher
@decorator_with_args
def fabric(decorator, lambda_function):
    def lambda_function_mod(*args,**kwargs):
        def inner_decorator(func):
            @functools.wraps(func)
            def inner_function(*args_2, **kwargs_2):
                if fabric.is_on:
                    res = decorator(func, *args, **kwargs)
                else:
                    result = func
                return lambda_function(result(*args_2, **kwargs_2))
            return inner_function
        return inner_decorator
    return lambda_function_mod


@fabric(lambda x: x**2)
def repeat(func, times):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        value = 0
        for i in range(times):
            value += func(*args, **kwargs)
        return value/times
    return inner

