# def demo_decorator(func):
#     def wrapper():
#         print("before execution")
#         func()
#         print("after execution")
#     return wrapper

# @demo_decorator # hello = demodecorator(hello) we are passing function hello as a argument to demo decorator function
# def hello():
#     print("hello world")

# hello()


# decorator with argument
def demo_decorator(func):
    def wrapper(name):
        print("before execution")
        func(name)
        print("after execution")
    return wrapper

@demo_decorator # hello = demodecorator(hello) we are passing function hello as a argument to demo decorator function
def hello(name):
    print(f"hello {name}")

hello("Ashish")
