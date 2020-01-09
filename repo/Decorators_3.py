# Decorator functions are popular in Flask

def ekstra(fonk):
    def wrapper(sayılar):
        çift_toplamı = 0
        çift_sayılar = 0
        tek_toplamı = 0
        tek_sayılar = 0
        for sayı in sayılar:
            if (sayı % 2 == 0 ):
                çift_sayılar +=1
                çift_toplamı += sayı
            else:
                tek_sayılar += 1
                tek_toplamı += sayı
        print("Even Number Avg:", çift_toplamı/çift_sayılar)
        print("Odd Number Avg:", tek_toplamı / tek_sayılar)
        fonk(sayılar)
    return wrapper

@ekstra
def ortalama(sayılar):
    toplam = 0
    for i in sayılar:
        toplam += i
    print("General Avg:",toplam/len(sayılar))

ortalama([1,2,3,4,34,60,63,32,100,105])
