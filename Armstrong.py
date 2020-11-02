#armstrong no: A number which is equivalent to sum of its each digits cube.
def armstrong(num):
    sum = 0
    temp = num
    while temp > 0:
        mod = temp % 10
        sum = sum + mod ** 3
        temp = temp // 10

    if(num == sum):
        print(num,"Is an armstrong no.")
    else:
        print(num,"Is not an armstrong no")

num = int(input("Enter no:"))
armstrong(num)


