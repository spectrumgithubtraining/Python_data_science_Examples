# Decorators allow you to make simple modifications to 
# callable objects like functions, methods, or classes (Functions and methods 
# are called callable as they can be called). That is, a decorator is just 
# another function which takes a functions and returns one.

def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

def ordinary():
    print("I am ordinary")
    

# let's decorate this ordinary function
pretty = make_pretty(ordinary)
pretty()

#We can use the @ symbol along with the name of the decorator function and place it above the definition
# of the function to be decorated.
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty
def ordinary():
    print("I am ordinary")



ordinary()