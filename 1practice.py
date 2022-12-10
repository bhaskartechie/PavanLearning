#to print the #,35,F with the ascii
a=35
print(chr(a))
str='#'
print(ord(str))
a=70
print(chr(a))
#to print ascii value to a string
print( "Enter a string: " , end="")
text =input()
textlength = len(text)
for char in text :
    ascii = ord(char)
    print(char, "\t", ascii)
