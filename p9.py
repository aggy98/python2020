num = int(input("Enter an int number: "))
num *=3
num +=1
def add_digit(num):
    if num > 0:
         return (num - 1) % 9 + 1
    elif num < 0:
         num *= -1
         return ((num - 1) % 9 + 1) * -1
    else:
         return 0 
print(add_digit(num))
