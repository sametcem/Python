#   FUNCTIONS

#Default values for Arguments

def get_gender(sex='Unknown'):
    if sex is 'm':
        sex="Male"
    elif sex is 'f':
        sex="Female"

    return sex

print(get_gender())

# Keyword Arguments

def dumb_sentence(name="Samet",action="ate",item="tuna"):
    print(name,action,item)

dumb_sentence()
dumb_sentence("Sally","farts","gently")
dumb_sentence(item="awesome",action="is")