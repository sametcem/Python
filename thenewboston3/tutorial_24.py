#  Dictionary Multiple Key Sort

from operator import itemgetter

#bunch of dictionary // first name and last name

users = [
    {'fname': 'Bucky', 'lname': 'Roberts'},
    {'fname': 'Tom', 'lname': 'Roberts'},
    {'fname': 'Bernie', 'lname': 'Zunks'},
    {'fname': 'Jenna', 'lname': 'Hayes'},
    {'fname': 'Sally', 'lname': 'Jones'},
    {'fname': 'Amanda', 'lname': 'Roberts'},
    {'fname': 'Tom', 'lname': 'Williams'},
    {'fname': 'Dean', 'lname': 'Hayes'},
    {'fname': 'Bernie', 'lname': 'Barbie'},
    {'fname': 'Tom', 'lname': 'Jones'},
]

for x in sorted(users,key=itemgetter("fname")):
    print(x)

print("----------------")
# True alphebatical sorting
for x in sorted(users,key=itemgetter("fname","lname")): #first sort them by their first name and then their last name
    print(x)


    
