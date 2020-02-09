try:
    f = open("simplle.txt","r")
    f.write("Test write to simple text!")
except IOError:
    print("ERROR: COULD NOT FIND FILE OR READ DATA!")
else:
    print("SUCCESS")
    f.close()
#finally: print("I always work no matter what!")