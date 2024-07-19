n="Tops Technology"

print(n.isprintable()) #Checks if all input are printable \n and break page are non-printable
print(n.isspace()) #Checks if all input are blankspace if yes then TRUE
print(n.isupper()) #Checks if all input are in uppercase if yes then TRUE
print(n.islower()) #Checks if all input are in lowercase if yes then TRUE
print(n.isalpha()) #Checks if all input are alphabets if yes then TRUE
print(n.isnumeric()) #Checks if all input are in numbers if yes then TRUE
print(n.isalnum()) #Checks if all input are in (alphabets OR numbers) if yes then TRUE
print(n.istitle()) #Checks if all the first word of a title are in uppercase if yes then TRUE
print(n.isascii()) #Checks if all input are between a-z
print(n.capitalize()) #Make the first alphabet of whole string uppercase
#difference between (capitalize and upper) is upper turns all input upper and capitalize turns first aplhabet of whole input
print(n.casefold()) #Turns all oinput words into lowercase (CASEFOLD and LOWER)do the same job
print(n.center(40,"#")) #first parameter WIDTH and second parameter FILL CHAR/SYMBOL
print(n.count("ops",1,11)) #First parameter number/alphabet/string, Second paramter start from and Third end from
print(n.endswith(" Technology",4,15)) #Checks if a input ends with a particular string
print(n.expandtabs(3)) #Used to expand size of tab in the input to a specified value
print(n.find("o",11,15)) #Finds first occucrance of a sting in the string
print(n.index("o",2,15)) #Same as FIND but (FIND returns -1 if not found and INDEX raises a error)
a="My name is {}, I am {}".format("Dev",17) #can insert any string/number in blank or pre-occupied variables
print(a)