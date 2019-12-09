groceries ={'cereal','milk','starcrunch','beer','duct tape','lotion','beer'}
print(groceries) #Sets have just unique elements

if 'milk' in groceries:
    print("You already have milk hoss!")
else:
    print("Oh yes, you need milk!")


# Dictionary keys and values

classmates = {"Tom":"cool but smells","Frank":"sits behind me","Lucy":"asks too many questions"}
print(classmates)
print(classmates["Frank"])

for k,v in classmates.items():
    print(k + " -> "+ v)