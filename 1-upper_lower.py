bella=input("Enter a character:")
if ord(bella)>=65 and ord(bella)<=90:
   print(bella,"is an upper case")
elif ord(bella)>=97 and ord(bella)<=122:
     print(bella,"is lower case")
else:
    print(bella,"is not a letter.")
