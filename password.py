import string
import random
print("PASSWORD GENERATOR")
length=int(input("Enter Length of your Password: "))
l=input("Include Letters(y/n): ").lower()=='y'
n=input("Include Numbers(y/n): ").lower()=='y'
s=input("Include Symbols(y/n): ").lower()=='y'
c=""
if l:
    c += string.ascii_letters
if n:
    c += string.digits
if s:
    c += string.punctuation
password = ''.join(random.choice(c) for _ in range(length))
print("Generated Password: ",password)
 