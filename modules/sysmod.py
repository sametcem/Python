import sys

"""""
print(dir(sys))

a = int(input("a: "))
b = int(input("b: "))

sys.exit()

c = int(input("c: "))
"""""
#Input -> stdin
#output -> stdout
#err -> stderr

sys.stderr.write("It is an error message!\n")
sys.stderr.flush()

sys.stdout.write("It is an normal text!\n")

print(sys.argv)

print("/////////")

for i in sys.argv: # python sysmod.py 1 2 3 in terminal alt f12
    print(i)