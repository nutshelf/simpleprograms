board = "123456789"
ai_symbol = "X"
user_symbol = "O"
x = 0
while True:
    x = int(input("Введи число в десятичной системе счисления: "))
    base = int(input("Введи основание системы счисления в десятичной системе счисления: "))
    number_string = "=" + str(bin(x))
    while x > 0:
        number_string = str(x % base) + number_string
        x = x // base
    print(number_string)