word = input("enter a word: ")
if word == word[::-1]:
    print(word,"is a palindrome")
else:
    print(word,"not a palindrome")
