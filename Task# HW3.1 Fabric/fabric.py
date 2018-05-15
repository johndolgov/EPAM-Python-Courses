"""
This module presents decorators fabric
"""
import functools


def decorator_with_args(decorator):
    """
    Decorator which creates decorator with args
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


@on_of_switcher
@decorator_with_args
def fabric(decorator, lambda_function):
    """
    Creates decorator which modify a decorator from args
    :param decorator: decorator which will be modified
    :param lambda_function: lambda function which can modify decorator
    :return: decorator which return modified decorator
    """
    def lambda_function_mod(*args, **kwargs):
        def inner_decorator(func):
            @functools.wraps(func)
            def inner_function(*args_2, **kwargs_2):
                if fabric.is_on:
                    res = decorator(func, *args, **kwargs)
                else:
                    res = func
                return lambda_function(res(*args_2, **kwargs_2))
            return inner_function
        return inner_decorator
    return lambda_function_mod


@fabric(lambda x: x**2)
def repeat(func, times):
    """
    This function repeat and calculate avarage value
    :param func: function
    :param times: qauntity of repeation times
    :return: sum of decorator result
    """
    @functools.wraps(func)
    def inner(*args, **kwargs):
        value = 0
        for i in range(times):
            value += func(*args, **kwargs)
        return value/times
    return inner


@repeat(3)
def spam(*args, **kwargs):
    """Function for test"""
    print("Spam here!")
    return 3


if __name__ == '__main__':
    print(spam([1, 3, 5]))
    fabric.off()
    print(spam([1, 3, 5]))