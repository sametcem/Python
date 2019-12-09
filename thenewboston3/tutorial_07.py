# How to Read and Write Files

#Writing
FileWrite = open("sample.txt","w") #Open and file and write it,if its not available create it
FileWrite.write("Writing some stuff in my text file\n")
FileWrite.write("I like tuna fish\n")
FileWrite.close()

#Reading
FileRead = open("sample.txt","r") # This file and read
text = FileRead.read()
print(text)
FileRead.close()