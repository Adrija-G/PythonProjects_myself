import re 
#RegEx, or Regular Expression, is a sequence of characters that forms a search pattern. 
#RegEx can be used to check if a string contains the specified search pattern.
#Regular expressions contain a series of characters (such as alphabets/number ranges, etc) that are required in correspondence with program input or some other data.

p= input("Input your password:   ")
x = True
while x== True:  
    if (len(p)<6):
        print("Password is too short") 
        break
    elif  (len(p)>20):
        print("Password is too long")
        break
    elif not re.search("[a-z]",p):
        print("Pwd must contain atleast one lowercase letter!")
        break
    elif not re.search("[0-9]",p):
        print("Pwd must contain atleast one numerical value!")
        break
    elif not re.search("[A-Z]",p):
        print("Pwd must contain atleast one uppercase letter!")
        break
    elif not re.search("[!@#$%^&*|\;':/,.?<>]",p):
        print("Pwd must contain atleast one special character!")
        break
    else:
        print("Valid Password")
        x=False
        break

















