x = input("enter a number: ")
number = str(x)

if number[0] == '-':
    print('-', end='') 
    number = number[1:]

print(number[::-1])
