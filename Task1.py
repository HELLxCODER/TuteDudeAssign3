def fact():
    num = input("Enter the number you want the factorial of: ")
    num = int(num)
    factorial = 1
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print(f"The factorial of {num} is 1 ")
    else:
        for i in range(1, num + 1):
            factorial = factorial * i
        print(f"The factorial of {num} is {factorial}")
        

fact()