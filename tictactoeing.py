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


def propose_turn(field, cu_pointer, gamers_symbol):
    """ Ф: Рекурсивная функция предположения (псевдо)рандомного хода одного игрока Sym с выводом в качестве значения
    количества выигрышей и ничьих при следующих ходах.
     - field - строка из клеток поля
     - cu_pointer - 'указатель' на то, чей ход следующий - игрока 0 или игрока 1
     - gamers_symbols - список символов этих игроков (список из двух однобуквенных строк) ['a', 'b']
    """
    winner_is = who_wins(field, gamers_symbol[0], gamers_symbol[1])
    available_cell = get_available_cells(field)
    if winner_is == gamers_symbol[0]:
        return [1,0,0]
    elif winner_is == gamers_symbol[1]:
        return [0,1,0]
    elif not available_cell:
        return [0,0,1]
    else: # никто не выиграл еще и поле незаполнено - можно предположить следующий ход
        cu_pointer = (cu_pointer + 1) % 2
        for cell in available_cell:
            ai_turn_result = propose_turn(field.replace(str(cell), ai_symbol))
            winner_is = who_wins(field, user_symbol, ai_symbol)
            if winner_is ==

    return [user, ai, draw]

def main ():
    field = "123456789"
    user_symbol = "O"
    ai_symbol = "X"
    symbols = [user_symbol, ai_symbol]
    cu_pointer = 0  # current user pointer - индекс игрока для совершения хода. 0 - ходит игрок, 1 - ходит компьютер
    game_is_on = True
    winner_is = ""

    # ход игры
    while game_is_on:
        draw_field(field)
        if cu_pointer == 0: # ход живого юзера
            while True:
                user_turn_cell_num = int(input("Ваш ход (введите номер клетки 1-9):"))
                if field[user_turn_cell_num] in "123456789":
                    field = field.replace(str(user_turn_cell_num), user_symbol)
                    break
                else:
                    print("ой, не туда! там уже кто-то побывал. еще разок")
        else: # ход искусственного интеллекта
            available_cells = get_available_cells(field)
            if len(available_cells) > 1:
                available_cell_win_ratio = []
                max_ratio = 0
                max_ratio_cell_index = 0
                for cell in available_cells:
                    ai_turn_result = propose_turn(field.replace(str(cell), ai_symbol), 0, symbols)
                    # главный алгоритм для определения клетки для хода - процент побед ИИ от всех возможных исходов
                    available_cell_win_ratio.append(ai_turn_result[1] / sum (ai_turn_result))
                    if available_cell_win_ratio[-1] > max_ratio:
                        max_ratio = available_cell_win_ratio[-1]
                        max_ratio_cell_index = cell
            else: # len(available_cells) = 1
                max_ratio_cell_index = available_cells
            field = field.replace(max_ratio_cell_index, ai_symbol)
        cu_pointer = (cu_pointer + 1) % 2
        winner_is = who_wins(field, user_symbol, ai_symbol)
        game_is_on = get_available_cells(field) and not winner_is
    # игра окончена
    if winner_is == user_symbol:
        print("you wins!")
    elif winner_is == ai_symbol:
        print("AI wins!")
    elif not get_available_cells(field):
        print("ничья, свободных клеток нет")
    else:
        print("свободные клетки есть (" +
              str(get_available_cells(field)) +
              "), но игра закончена и никто не выиграл. Чудеса! еррор конечно")

main()