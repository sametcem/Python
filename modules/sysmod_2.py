import sys

def findRoot(a,b,c):
    delta = (b ** 2)- 4 * a * c

    if(delta < 0):
        print("Reel Kök Yok")
    else:
        x1 = (-b - delta ** 0.5) / (2*a)
        x2 = (-b + delta ** 0.5) / (2*a)
        return x1,x2

if len(sys.argv) == 4:
    print("Kök bulma", findRoot(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])))
else:
    sys.stderr.write("Please input true valueas.")
    sys.stderr.flush()