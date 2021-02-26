field_state = "123456789"
user_symbol = "O"
ai_symbol = "X"
current_user = [user_symbol, ai_symbol]  # список для определения, чей ход
current_user_pointer = 0  # индекс для списка
game_is_on = True

# ход игры
while game_is_on:
    # делают ходы

    # завершение хода
    current_user_pointer = (current_user_pointer + 1) % 2
    there_is_winner = someone_wins_detection(field_state)
    game_is_on = available_cells(field_state) and not there_is_winner

# игра окончена
if there_is_winner == user_symbol:
    print("you wins!")
elif there_is_winner == ai_symbol:
    print("AI wins!")
else:
    print("some error ocures! winning detection error. Winner is ", winner, ". Exiting")
