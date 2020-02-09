#Given a list of integers, return True if the sequence of numbers 1,2,3,
#appers in the list somewhere

#For example:
#arrayCheck([1,1,2,3,1]) -> True
#arrayCheck([1,1,2,4,1]) -> False

def arrayCheck(nums):
    for i in range(len(nums)-2):
        if(nums[i]== 1 and nums[i+1] ==2 and nums[i+2]==3):
            print("Matched")
            return True
    print("Unmatched")
    return False

print(arrayCheck([1,1,2,3,1]))
print(arrayCheck([1,1,2,4,1]))


def stringBits(mystring):
    result =""
    for i in range(len(mystring)):
        if i%2==0:
            result = result + mystring[i]
    return result

print(stringBits("Hello"))
print(stringBits('Hi'))
print(stringBits('Heeololeo'))

def end_other(a,b):
    a = a.lower()
    b = b.lower()

    #return (b.endswith(a) or a.endswith(b))
    return a[-(len(b)):] == b or b[-(len(a))] == a

print(end_other('Hiabc','abc'))
print(end_other('AbC','HiaBc'))

def doubleChar(myString):
    result= ''
    for char in myString:
        result += char*2
    return result

print(doubleChar('The'))

def fix_teen(n):
    if n [13,14,17,18,19]:
        return 0
    return n

def no_teen_sum(a,b,c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)
