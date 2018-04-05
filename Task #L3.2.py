import time

def shiny_decorator(func_to_decorate):
    """This program allow to count runtime
    of programm
    :param - function
    :type - function"""
    def wrapper():
        t1 = time.time()
        func_to_decorate()
        t2 = time.time()
        dt = t2 - t1
        print('А вот сколько!')
        print(dt)
    return wrapper

@shiny_decorator
def alone_function():
    l = []
    print('Сколько, по твоему, я работаю?')
    for i in range(10000000):
        l.append(i)

if __name__ == "__main__":
   alone_function()