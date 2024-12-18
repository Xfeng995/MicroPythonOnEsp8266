# decorator 函数
def add_exclamation(func):
    def wrapper(name):
        return func(name) + '!'
    return wrapper

# 被装饰的函数

def hello(name):
    return 'hello' + name

#
hello = add_exclamation(hello)


print(hello('tom'))

