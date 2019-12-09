# Bu yöntem de kullanılabilir

#with open("languages.txt","r") as dosya:
    #print(dosya.read())


with open("languages.txt","r") as okunacakdosya:
    #okunacakdosya.seek(10) #sonrasını okur.
    # print(okunacakdosya.read())
    # okunacakdosya.seek(5) # En basa döner
    # print(okunacakdosya.read())

    okunacakdosya.seek(10)
    str1 = okunacakdosya.read(5)
    okunacakdosya.seek(15)
    str2= okunacakdosya.read(5)

    print(str1,str2)