# Decorators are an advanced tool in Python
"""
s = "GLOBAL VARIABLE!"
def func():
    global s
    s = 50
    print(s)
    mylocal = 10
    print(locals()) # dictionary call
    #print(globals())
    #print(globals()['s']) s - key value pair

func()
print(s)
"""
"""
def hello(name="Jsoe"):
    print("THE HELLO() FUNCTION HAS BEEN RUN!")
    def greet():
        return "THIS STRING IS INSIDE OF THE GREET()"
    def welcome():
        return "THIS STRING IS INSIDE OF THE WELCOME()"
    
    if name == "Jsoe":
        return greet
    else:
        return welcome

x = hello()
print(x())
"""
"""
def hello():
    return "Hi JOSE!"

def other(func):
    print("HELLO")
    print(func())

other(hello)
"""

# So decorator

def new_decorator(func):

    def wrap_func():
        print("CODE HERE BEFORE EXECUTING FUNC")
        func()
        print("FUNC() HAS BEEN CALLED")

    return wrap_func

@new_decorator
def func_needs_decorator():
    print("THIS FUNCTION IS IN NEED OF A DECORATOR!")

#func_needs_decorator = new_decorator(func_needs_decorator)

func_needs_decorator()
