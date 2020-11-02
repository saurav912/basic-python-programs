a = input("Enter a string to check palindrome: ")
a = a.lower() #for lowercase or uppercase similarity 
b = a[::-1]

if (a == b):
    print("String is palindrome")
else:
    print("String is not a palindrome")
