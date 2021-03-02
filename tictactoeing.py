field_state = "123456789"
user_symbol = "O"
ai_symbol = "X"
current_user = [user_symbol, ai_symbol]  # список для определения, чей ход
cu_pointer = 0  # current user pointer - индекс для списка. 0 - ходит игрок, 1 - ходит компьютер
game_is_on = True


def draw_field(field):
    """ ПР: Замещение цифр 0-9 на пробел и вывод поля  """
    for i in range(10):
        field = field.replace(str(i), " ")
    print(field[0] + "|" + field[1] + "|" + field[2])
    print("-+-+-")
    print(field[3] + "|" + field[4] + "|" + field[5])
    print("-+-+-")
    print(field[6] + "|" + field[7] + "|" + field[8])
    return


def get_available_cells(field):
    """ Ф: Результат - список из номеров "пустых" ячеек. """
    list_of_cells = []
    for cell in field:
        if cell in "123456789":
            list_of_cells.append(cell)
    return list_of_cells


def who_wins(f: str, sym1: str, sym2: str):
    """ Ф: Результат - один из поданных на вход символов sym (предполагается,
    что подаются user_symbol и ai_symbol), обозначающие игроков. В случае отсутствия
    победителя выводится пустая строка. """
    for s in [sym1 * 3, sym2 * 3]:
        if (f[0] + f[1] + f[2] == s) or (f[3] + f[4] + f[5] == s) or (f[6] + f[7] + f[8] == s) or \
                (f[0] + f[3] + f[6] == s) or (f[1] + f[4] + f[7] == s) or (f[2] + f[5] + f[8] == s) or \
                (f[0] + f[4] + f[8] == s) or (f[2] + f[4] + f[6] == s):
            return s[0]
    return ""


def make_ai_turn(field, sym):
    """ Ф: Рекурсивная функция рандомного хода игрока sym с выводом количества выигрышей
     в нижней части дерева"""
    # получили field
    # выбрали одну из доступных для хода клеток
    # + поставили sym
    # проверили на выигрыш
    # -
    # вышли
    return [user, ai, draw]


# ход игры
while game_is_on:
    draw_field(field_state)
    if cu_pointer == 0:
        while True:
            user_turn_cell_num = int(input("Ваш ход (введите номер клетки 1-9):"))
            if field_state[user_turn_cell_num] in "123456789":
                field_state = field_state.replace(str(user_turn_cell_num), user_symbol)
                break
            else:
                print("ой, не туда! еще разок")
    else:
        available_cells = get_available_cells(field_state)
        available_cell_probability = []
        max_prob = 0
        for cell in available_cells:
            available_cell_probability = (
                make_ai_turn(field_state.replace(str(cell), ai_symbol))[1] -
                make_ai_turn(field_state.replace(str(cell), ai_symbol))[0])
            if available_cell_probability > max_prob:
                max_prob = available_cell_probability
                max_i = cell
        field_state = field_state.replace(max_i, ai_symbol)
    cu_pointer = (cu_pointer + 1) % 2
    winner_is = who_wins(field_state, user_symbol, ai_symbol)
    game_is_on = get_available_cells(field_state) and (winner_is == "")

# игра окончена
if winner_is == user_symbol:
    print("you wins!")
elif winner_is == ai_symbol:
    print("AI wins!")
elif not get_available_cells(field_state):
    print("ничья, свободных клеток нет")
else:
    print("свободные клетки есть (" +
          str(get_available_cells(field_state)) +
          "), но никто не выиграл. Чудеса! еррор конечно")
