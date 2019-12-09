#Kullanıcı ismi ve Parola Kontrolü Programi
# and or not
# bool true false

defkullanici="yazilimcibebe"
defparola="1234"

kullanici = input("Kullanıcı Adı: ")
parola = input("Parolanız: ")

if((defkullanici == kullanici) and (parola == defparola)):
    print("Yazılım bilimi sitesine HOSGELDINIZ!")
elif ((defkullanici != kullanici) and (parola == defparola)):
    print("Kullanıcı adinizi yanlıs girdiniz")
elif ((defkullanici == kullanici) and (parola != defparola)):
    print("Sifrenizi mi unuttunuz?")
else:
    print("Tekrar deneyiniz.........")






