import time


def gen(name, interval):
    while True:
        print(f'Hello {name}')
        initial_time = time.time()
        while time.time()-initial_time < interval:
            yield