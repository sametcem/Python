#break ve continue

defkullanici="yazilimci"
defparola="gollum"

while True:
    kullanici=input("Kullanıcı ismi giriniz.")
    parola=input("Parola giriniz.")

    if((kullanici!=defkullanici) or (parola!=defparola)):
        print("Yanlıs giris")

    else:
        print("HOSGELDINIZ...")
        break

