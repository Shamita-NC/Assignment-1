#Assignment 1 question 2- Reversal of name
#Accepts fisrst name of the user
firstname=input("Input your first name:")
#Accepts lastname of the user
lastname=input("Input your last name:")
#Revese the first name and last name using reversed() functin
rev1=''.join(reversed(firstname))
rev2=''.join(reversed(lastname))
#Display reverse order of the name
print(rev1,"",rev2)