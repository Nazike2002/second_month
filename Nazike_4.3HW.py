from random import choice
class Casino: # Казино
    def __init__(self, money,bill) -> None: # Получаем банк
        if isinstance(money, int):
            self.money = money
            self.bill = bill
        else:
            raise ValueError("Should be int")
    def game(self, slot, summa_stavki):
        random_list = list(range(1,30))
        random = choice(random_list)
        print(f"Вы поставили на {slot}, ставку в {summa_stavki} ")
        if random == slot:
            self.bill+= summa_stavki
            print(f"Выпало: {random}")
            print(f"Вы победили {summa_stavki}$!")
            return True
        elif random != slot:
            self.money -= summa_stavki
            self.bill -= summa_stavki
            print(f"Выпало: {random}")
            print(f"Вы проиграли {summa_stavki}$")
            return True
        else:
            print("Ошибка!")
            return True
