# Decorator using Return statements

def make_bold(func):
    def inner(text):
        # add some additional behavior to decorated function
        result = func(text)
        # wrap the result in bold tags
        return f"<b>{result}</b>"
    return inner

@make_bold
def greet(name):
    return f"Hello, {name}!"

# calling the decorated function
decorated_greet = greet("John")
print(decorated_greet) 