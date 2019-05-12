import functools


def my_decorator(func):
    @functools.wraps(func)
    def function_that_runs_func():
        print('In the decorator.')
        func()
        print('After the decorator.')
    return function_that_runs_func


@my_decorator
def say_hello():
    print('Hello!')


def decorator_with_arguments(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_that_runs_func(*args, **kwargs):
            print('In the decorator.')
            if number == 56:
                print('Not running the func')
            else:
                func(*args, **kwargs)
            print('After the decorator.')
        return function_that_runs_func
    return my_decorator


@decorator_with_arguments(57)
def say_hello_two(a, b):
    print(a * b)


if __name__ == '__main__':
    say_hello()
    say_hello_two(1, 2)
