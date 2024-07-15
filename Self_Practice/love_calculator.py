print("The Love Calculator is calculating your score...")
name1 = input("Enter first name :") # What is your name?
name2 = input("Enter second name :") # What is their name?


name= name1+name2
name= name.lower()

t= name.count('t')
r= name.count('r')
u= name.count('u')
e= name.count('e')
true=t+r+u+e

l= name.count('l')
o= name.count('o')
v= name.count('v')
e= name.count('e')
love=l+o+v+e
tl=str(true)+str(love)
tl=int(tl)

if tl<10 or tl>90:
  print(f"Your score is {tl}, you go together like coke and mentos.")
elif tl>40 and tl<50:
  print(f"Your score is {tl}, you are alright together.")
else:
  print(f"Your score is {tl}.")
