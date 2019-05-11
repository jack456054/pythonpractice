import functools


def my_decorator(func):
    @functools.wraps(func)
    def function_that_runs_func():
        print('In the decorator.')
        func()
        print('After thr decorator.')
    return function_that_runs_func


@my_decorator
def say_hello():
    print('Hello!')


if __name__ == '__main__':
    say_hello()
