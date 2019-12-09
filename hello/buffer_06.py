with open("samet.txt","r+") as file:
    data=file.readlines()
    data.insert(2,"Stratocaster\n")
    file.seek(0)
    file.writelines(data)
