#A number is said to be a palindrome if its reverse is same as the original number 

numb = int(input("Enter no. to check palindrome: "))
temp = numb
reverse = 0
while numb > 0:
    d = numb %10
    reverse = reverse * 10 + d
    numb = numb // 10

if (temp == reverse):
    print("Its a palindrome")
else:
    print("Not a Palindrome")
