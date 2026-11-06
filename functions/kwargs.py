# In Python, **kwargs stands for "keyword arguments." It allows a function to accept any number of named (key-value) arguments without explicitly defining them in advance.

# Inside the function, Python packs all these extra named arguments into a standard dictionary.

def print_user(**kwargs):
    print(kwargs)        # kwargs is a regular Python dictionary
    print(type(kwargs))  # <class 'dict'>

print_user(name="Dhananjay", role="Developer", age=20)

