# Basa Ortaya ve Sona ekleme.
# mod r+ hem yazmak hem de okumak icin

with open("languages.txt","r+") as dosya:
   # dosya.write("\nPhp: Rasmus Lerdorf") # Automatically at the end
    data =dosya.read()
    dosya.seek(0)
    data = "Php: Rasmus Lerdorf\n"+ data
    dosya.write(data)


