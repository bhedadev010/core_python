
file=open("tops1.txt","w")
file.write("this is demo for W in file_m")
file.close()
print("*****************************************")

file=open("tops1.txt","r")
print(file.read())
file.close()
print("*****************************************")

file=open("tops1.txt","a")
file.write("\n This is appended part")
file.close()
print("*****************************************")

file=open("tops1.txt","r")
print(file.read())
file.close()
print("*****************************************")

#in w+ you can write and read in existing file and if file doesnt exist then it will create NEW FILE

file=open("tops2.txt","w+")
file.write("this is file writing through w+ in new file ")
file.seek(0)
print(file.read())
file.close()
print("*****************************************")

#in r+ mode you can read and write in EXISTING file. if file doesnt exist it wont perform
