import random
import string

print("PASSWORD GENERATOR")

length=int(input("\n\nEnter the length of password:"))

#storing predefined constants in variables ()
lower=string.ascii_lowercase
print(type(lower))
upper =string.ascii_uppercase
num=string.digits
symbols=string.punctuation


#merge the value in a variable
all=lower + upper + num + symbols

#shuffling and creating random length of password  defined by user
a =random.sample(all,length)

#combining the list values of "a" & contenating in string
password= "".join(a)

#printing  password
print(password)