x=input()
if x.isalpha():
    print("alphabet")
elif x.isdigit():
    print("digit")
elif x.isalnum():
    print("both")
else:
    print("Invalid input") 
