x = 0
while True:
    x = int(input("Введи число в десятичной системе счисления: "))
    base = int(input('Введи основание системы счисления в десятичной системе счисления: '))
    number_string = ""
    # обрамления каждого разряда скобочками для систем счисления с основанием, большим 10
    br1 = "(" * (base > 10)
    br2 = ")" * (base > 10)
    while x > 0:
        number_string = br1 + str(x % base) + br2 + number_string
        x = x // base
    print(number_string)
