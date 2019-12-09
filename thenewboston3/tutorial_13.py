class Girl:
    gender = "Female" # "class variable" so its a default value for a classs

    def __init__(self,name):
        self.name = name # This is unique "instance variable"

r = Girl("Rachel")
s = Girl("Monica")

print(r.gender)
print(s.gender)
print(r.name)
print(s.name)