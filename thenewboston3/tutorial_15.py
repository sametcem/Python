# Multiple Inheritance

class Mario():
    def move(self):
        print("I am moving around")

class Shroom():
    def eat_shroom(self):
        print("Now I am big!")


class BigMario(Mario,Shroom): # It has all the functionality from Mario and Shroom...
    pass #eger icine hir bir sey yazmak istemezsen -> pass


bm = BigMario()
bm.move()
bm.eat_shroom()
