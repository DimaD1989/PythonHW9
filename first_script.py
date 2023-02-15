import emoji

# Крестики-нолики

print("*" * 10, " Игра Крестики-нолики  ", "*" * 10)
print(emoji.emojize(":hand_with_fingers_splayed:")) 
board = list(range(1,10))                                                           #cоздаем список,для создания поля

def draw_board(board):                                                              # заводим функцию для рисования
   print("-" * 13)                                                                  # выводим 13 "-"
   for i in range(3):                                                               # создаем цикл,поле на 3 клетки
      print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")           # создаем 3 клетки в строке
      print("-" * 13)

def input_user(player):                                                             # создаем функцию для коректности ввода пользователя
   valid = False
   while not valid:                                                                 # меняет результат, если не верно или наоборот
      player_answer = input("Куда поставим " + player+"? ")                         # задаем вопрос пользователю о +
      try:
         player_answer = int(player_answer)
      except:                                                                       #  обработка корректности ввода
         print("Некорректный ввод. Вы уверены, что ввели число?")
         print(emoji.emojize(":cross_mark:"))
         continue
      if player_answer >= 1 and player_answer <= 9:                                 # двойная проверка корректности хода
         if(str(board[player_answer-1]) not in "XO"):                               # защита от дурака
            board[player_answer-1] = player
            valid = True
         else:
            print("Эта клетка  занята!")                                         
      else:
        print("Некорректный ввод. Введите число от 1 до 9.")
        print(emoji.emojize(":cross_mark:"))


def check_win(board):                                                              # функция проверки игрового поля, проверяет, выиграл ли игрок
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)) # кортеж выйгрышных кобминации
   for each in win_coord:                                                          
       if board[each[0]] == board[each[1]] == board[each[2]]:                       # провекра на выйгрыш
          return board[each[0]]
   return False

def main(board):                                                                    # основная функция игры, которая будет запускать все ранее описанные функции. Данная функция запускает и управляет игровым процессом.
    count = 0                                                                       # счетчик
    win = False
    while not win:
        draw_board(board)
        if count % 2 == 0:
           input_user("X") 
           print(emoji.emojize(":face_savoring_food:"))
                                                        # 1 пользователь
        else:
           input_user("O")  
           print(emoji.emojize(":face_exhaling:"))                                                        # 2 пользователь
        count += 1
        if count > 4:
           tmp = check_win(board)                                                   # создаем переменную,чтобы не обращаться к чек вину
           if tmp:
              print(tmp, "выиграл!")
              print(emoji.emojize(":1st_place_medal:"))
              win = True
              break
        if count == 9:
            print("Ничья!")
            print(emoji.emojize(":handshake:"))
            break
    draw_board(board)                                                               # вызов функции
main(board)   
                                                                      # вызов функции
print(emoji.emojize(":door:"))
input("Нажмите Enter для выхода!")

