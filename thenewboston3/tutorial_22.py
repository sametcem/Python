#Finding Most Frequent Items

from collections import Counter

text = "The company began as Fender's Radio Service in late 1938 in Fullerton, " \
       "California. As a qualified electronics technician, Fender had repaired radios, " \
       "phonographs, home audio amplifiers, public address systems and musical instrument amplifiers, " \
       "all designs based on research developed and released to the public domain by Western Electric in the 1930s using vacuum tubes for amplification. " \
       "The business also sidelined in carrying records for sale and the in rental of company-designed PA systems. " \
       "Leo became intrigued by design flaws in contemporary musical instrument amplifiers and began building amplifiers based on his own designs or modifications to designs."



# Pass it into a list and then configure it

words = text.split()
print(words)

counter = Counter(words)
topThree= counter.most_common(3) # it will return list of tuples.
print(topThree)






