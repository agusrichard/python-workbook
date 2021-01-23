import random

PLUGINS = dict()


def register(func):
    PLUGINS[func.__name__] = func
    return func


@register
def say_hi():
    print("Hii!")


@register
def say_hello():
    print("Hello")


@register
def say_bye():
    print("Bye!")


def say_randomly():
    chosen, chosen_func = random.choice(list(PLUGINS.items()))
    print(f"Running {chosen}")
    chosen_func()


say_randomly()