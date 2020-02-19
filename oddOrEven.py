number = int(input("Enter an interger? "))
if number % 2 == 0 and number % 4 != 0:
    print("the number you chose is even")

elif number % 2 == 1:
    print("the number you chose is odd")

elif number % 4 == 0:
    print("the number you chose is a multiple of 4 and is even")

num = int(input("enter another number? "))
check = int(input("enter this number to check "))
if num % check == 0:
    print(f"{num} can be evenly divided by {check}")

else:
    print(f"{num} can be oddly divided by {check}")
