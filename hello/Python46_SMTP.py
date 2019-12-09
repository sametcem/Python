# Gmail mail server'ına baglanarak baska birine mail atacagız.

import smtplib

content ="............."

#Gmail'in mail server'ına baglanıyoruz #GMAIL HESABINA SAHİP OLMAN GEREK
mail = smtplib.SMTP("smtp.gmail.com",587) #1. Hangi mail serverina baglanmak istiyorsun 2.parameter bu mail serverı hangi portu kullaniyor.

mail.ehlo() # üzerinden mail gönderecegim.

mail.starttls()# Birazdan girecegimiz kullanici adı ve şifremizi encrypt eder bu bilgileri gizleyerek mail serverına gönderir.

mail.login("------------------------------@gmail.com","-")


i=0
for i in range(1,10):
    mail.sendmail("-------------------lu@gmail.com", "-.com",content)  #  kimden gidiyor  kime gidiyor  ne gidiyor.