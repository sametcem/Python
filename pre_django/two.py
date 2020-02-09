import one

print("TOP LEVEL TWO.PY")
one.func()

if __name__ == '__main__':
    print("Two.py being run directly")
else:
    print("two.py has been imported")




# __name __
"""
This is a built-in variable
which evaluates the name
of current module

"""