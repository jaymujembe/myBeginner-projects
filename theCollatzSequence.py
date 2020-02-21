# This is the collatz sequence
def collatz(number):
    if number % 2 == 0:
        #print("The number is even.")
        num1 = number // 2
        return num1



    elif number % 2 == 1:
        #print("The number is odd.")
        return 3 * number + 1

print("Enter an integer\n and number great or equal to  1")
print("Enter number.")
try:
    number = int(input())
except ValueError:
    print("please enter number")



while collatz(number) > 0:
    print(collatz(number))
    number = collatz(number)
    if number == 1:
        break
