field_state = "123456789"
user_symbol = "O"
ai_symbol = "X"
current_user = [user_symbol, ai_symbol]  # список для определения, чей ход
current_user_pointer = 0  # индекс для списка

# ход игры
while (available_cells(field_state) and not someone_wins(field_state)):
    # делают ходы
    current_user_pointer = (current_user_pointer + 1) % 2
# игра окончена
winner = someone_wins(field_state)
if winner == user_symbol:
    print("you wins!")
elif winner == ai_symbol:
    print("AI wins!")
else:
    print("some error ocures! winning detection error. Winner is ", winner, ". Exiting")
