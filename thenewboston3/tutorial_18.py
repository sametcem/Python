first = ["Bucky","Tom","Taylor"]
last =["Roberts","Hanks","Swift"]

# Making a list of tuples.
names = zip(first,last)
for name,surname in names:
    print(name,surname)

