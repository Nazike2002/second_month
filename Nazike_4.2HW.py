from random import choice
class Fortune:
    def game(self,summa_stavki):
        self.result = 0
        mythical = ["Зевс", "Аид", "Посейдон"]
        random = choice(mythical)
        mystery = choice(mythical)
        answer = input(f"За дверью стоит {mystery}?")
        if summa_stavki > 0: 
            if answer == "верю" and random == mystery or answer == "не верю" and random != mystery:
                print(f"За дверью стоял {random}")
                self.result = summa_stavki  * 2
                print(f"Вы победили! Ваш выигрыш : {self.result}$")
            if answer == "верю" and random != mystery or answer == "не верю" and random == mystery:
                print(f"За дверью стоял {random}")
                self.result = 0
                print(f"Вы победили! Ваш выигрыш: {self.result}$")
        elif summa_stavki < 0: # если проигрывали и вы в минусе
            if answer == "верю" and random == mystery or answer == "не верю" and random != mystery:
                print(f"За дверью стоял {random}")
                self.result = 0
                print(f"Вы победили! Ваш проигрыш : {self.result}$")
            if answer == "верю" and random != mystery or answer == "не верю" and random == mystery:
                print(f"За дверью стоял {random}")
                self.result = summa_stavki * 2
                print(f"Вы проиграли! Ваш проигрыш: {self.result}$")
