def geometry(sekil):
    if len(sekil) ==3:
        a =sekil[0]
        b =sekil[1]
        c =sekil[2]

        if(a+b) > c and (a+c) > b and (b+c) > a:
            if(a==b) and (a==c) and (b==c):
                print("Bu bir ESKENAR UCGEN")
            elif ((a==b) or (a==c) or (b==c)):
                print("Bu bir IKIZKENAR UCGEN")
            else:
                print("Bu bir CESITKENAR UCGEN")

        else:
            print("Ucgen olma koşulu saglanmiyor.")



    elif len(sekil)==4:
        a = sekil[0]
        b = sekil[1]
        c = sekil[2]
        d = sekil[3]

        if (a==b) and (a==c) and (a==d):
            print("Bu bir KAREDİR")
        elif (a==c) and (b==d):
            print("Bu bir DIKDORTGENDIR")
        else:
            print("Normal Dörtgen")

    else:
        print("Herhangi bir sekil degil...")

while True:
    eleman_sayisi=int(input("Eleman sayınızı giriniz"))
    if(eleman_sayisi ==3):
        a = int(input("a:"))
        b = int(input("b:"))
        c = int(input("c:"))
        geometry([a,b,c])


    elif(eleman_sayisi==4):
        a = int(input("a:"))
        b = int(input("b:"))
        c = int(input("c:"))
        d = int(input("d:"))
        geometry([a,b,c,d])


    else:
        print("Lutfen tekrar deneyiniz")