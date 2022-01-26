# ДОП Задание :
# 1. Создать многомодульную игру Казино
# 2. Сам запуск игры в отдельном файле
# 3. Логика выигрыша или проигрыша в отдельном файле
# 4. Логика Фортуны также в отдельном файле

import homework4_4
import homework4_2

bank = 1000
bill = 0
print("Добро пожаловать!")
while True:
    slot = int(input("Выберите слот: "))
    summa_stavki = int(input("Ваша ставка: "))
    play = homework4_4.Casino(bank, bill)
    play.game(slot,summa_stavki)
    bill = play.bill
    choose = input("Хотите продолжить: да или нет ")
    if choose == "да":
        continue
    else:
        if play.bill > 0:
            print(f"Вы выиграли {play.bill}$")
        else:
            print(f"Вы проиграли {play.bill}$")
        _choose_ = input("Хотите сыграть в Фортуну? ")
        if _choose_ == "да":
            print("Отвечайте только верю и не верю")
            play_2 = homework4_2.Fortune()
            play_2.game(play.plus_or_minus)
            bank += play_2.result 
            print(f"Теперь у вас {bank}$")
            break
        else:
            bank += play.bill
            print(f"Теперь у вас {bank}$")
            break