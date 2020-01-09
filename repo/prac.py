
print(bin(4))
print(bin(19))
print(bin(521))
print(hex(20))
print(hex(512))
print(abs(-1.4)) #mutlak deger
print(round(3.7))
print(round(3.2229,3))
print(round(3.2224,3))
print(max(3,4))
print(min(3,4))
print(max([12,1,13]))
print(sum([1,2,3,4]))
print(pow(2,3))
print(2**3)
print(pow(64,0.5))

p = "python".upper()
print(p)

p2 = "PYTHON".lower()
print(p2)

p3 = "ALALALALA".replace("A","E")
print(p3)

p4 = "Python Programlama Dili".replace(" ","-")
print(p4)

p5 = "Python".startswith("Py")
print(p5)
p6 = "Python".endswith("on")
print(p6)

list = "Python-PHP-Java".split("-")
print(list)

"""
strip(x) -> Stringin başında va sonunda bulunan x degerlerini siler
lstrip(x) -> Stringin sadece başında bulunan x degerlerini siler
rstrip(x) -> Stringin sadece sonunda bulunan x degerlerini siler
"""


list2 = ["21","12","1998"]
a = "/".join(list2)
print(a)

p7 = "aaaaaaaaaaaaaaaaaaaaa".count("a")
print(p7)

d = "araba".find("a")
print(d)

e = "araba".find("s")
print(e)

k = "araba".find("b")
print(k)