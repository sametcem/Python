# REGULAR EXPRESSIONS
# ALLOW US TO SEARCH FOR PATTERNS IN PYTHON STRINGS

import re

patterns = ['term1','term2']
split_term = '@'

email = "user@gmail.com"
# email = "user@gmail.com".split('@') so it comes from the re lib.

print(re.split(split_term,email))


text = 'This is a string with term1, but not the other!'

"""
for pattern in patterns:
    print("I am searching for: " + pattern)

    if re.search(pattern, text):
        print("MATCH!!!")
    else:
        print("NO MATCH")
"""

match = re.search('term1',text)
print(match.start()) # it starts at 22nd index.

print(re.findall('match', 'test phrase match in match match mat'))


def multi_re_find(patterns, phrase):
    for pat in patterns:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat,phrase))
        print('\n')

test_phrase = 'sdsd..sssddd..sdddsddd...dsds....dssssss...sddddd'
test_patterns = ['sd*'] # s followed by zero or more d
# test_patterns = ['sd+'] # s followed by one or more d
# test_patterns = ['sd?'] # s followed by zero or one d
#test_patterns = ['sd{2,3}'] # s followed by TWO or THREE d
# test_patterns = ['s[sd]*'] # s followed by EITHER one or more s OR one or more d


multi_re_find(test_patterns,test_phrase)


test_phrase2 = 'This is a string! But it has punctuation. How can we remove it?'
test_patterns2 = ['[^!.?]+']

multi_re_find(test_patterns2,test_phrase2)

test_patterns3 = ['[a-zA-Z]+'] # All the lower case and upper case.
multi_re_find(test_patterns3,test_phrase2)

test_phrase4 = 'Rhis is a string with numbers 12312 and a symbol #hashtag'
test_patterns4 = [r'\d+'] #sequence of digits
# test_patterns4 = [r'\D+'] #sequence of NONdigits

#test_patterns4 = [r'\s+'] #sequence of whitespaces, capital S with non whitespace
#test_patterns4 = [r'\w+'] #sequence of alphanumeric(NUMBERS AND LETTERS), W non alphanumberic. spaces are also non alphanumeric.

multi_re_find(test_patterns4,test_phrase4)

