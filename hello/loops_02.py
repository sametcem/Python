# Kullanici Adi ve Parola Kontrolü
#break deyimi - döngünün içinde break çalıştırıldığı zaman döngü sona erer.

defkullanici ="yazilimcibebe"
defparola = "1234"

while(True):
    kullanici = input("Kullanıcı Adı: ")
    parola = input("Parolanız: ")

    if ((kullanici == defkullanici) and (parola==defparola)):
        print( "Hosgeldiiz",kullanici)
        break
    elif ((kullanici != defkullanici) and (parola == defparola)):
        print("Kullanıcı adınızı yanlıs girdiniz")
    elif ((kullanici == defkullanici) and (parola != defparola)):
        print("Sifrenizi mi unuttunuz?")
        print("Sifreyi degistirmek ister misiniz? (E/H))")
        cevap = input()
        if(cevap =="E"):

            yeniparola=input("Yeni Parola")
            print("Lütfen Bekleyin")
            defparola= yeniparola
            print("Sifre basarıyla degistirildi")
    else:
        print("Tekrar deneyiniz.....")