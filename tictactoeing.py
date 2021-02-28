field_state = "123456789"
user_symbol = "O"
ai_symbol = "X"
current_user = [user_symbol, ai_symbol]  # список для определения, чей ход
cu_pointer = 0  # индекс для списка. 0 - начинает игрок, 1 - ИИ
game_is_on = True

def draw_field (field):
    """ Результат - замещение цифр на пробел и вывод поля  """
    for i in range(10):
        if field[i] in "123456789":
            field[i] = " "
    print(field[0] + "|" + field[1] + "|" + field[2])
    print("-+-+-")
    print(field[3] + "|" + field[4] + "|" + field[5])
    print("-+-+-")
    print(field[6] + "|" + field[7] + "|" + field[8])
    return

def available_cells(field):
    """ Результат - список из номеров "пустых" ячеек. """
    list_of_cells = []
    for cell in field:
        if cell in "123456789":
            list_of_cells.append(cell)
    return list_of_cells

def who_wins(f:str, sym1:str, sym2:str):
    """ Результат - символ "X" или "O" того, кто выиграл. Иначе пустая строка. """
    for s in [sym1*3, sym2*3]:
        if (f[0] + f[1] + f[2] == s) or (f[3] + f[4] + f[5] == s) or (f[6] + f[7] + f[8] == s) or \
           (f[0] + f[3] + f[6] == s) or (f[1] + f[4] + f[7] == s) or (f[2] + f[5] + f[8] == s) or \
           (f[0] + f[4] + f[8] == s) or (f[2] + f[4] + f[6] == s):
            return s[0]
    return ""

# ход игры
while game_is_on:
    draw_field(field_state)
    if cu_pointer == 0:
        while True:
            user_turn = int(input("Ваш ход (введите номер клетки 1-9):"))
            if field_state[user_turn] in "123456789":
                field_state[user_turn] = user_symbol
                break
            else:
                print("ой, не туда! еще разок")
    else:
        field_state[proposed_turn(field_state,ai_symbol)] = ai_symbol
    cu_pointer = (cu_pointer + 1) % 2
    winner_is = who_wins(field_state,ai_symbol,user_symbol)
    game_is_on = available_cells(field_state) and (winner_is == "")

# игра окончена
if winner_is == user_symbol:
    print("you wins!")
elif winner_is == ai_symbol:
    print("AI wins!")
elif available_cells(field_state) == []:
    print("ничья, свободных клеток нет")
else:
    print("свободные клетки есть (" + available_cells(field_state) + "), но никто не выиграл. Чудеса! еррор конечно")