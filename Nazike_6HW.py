class Algoritm:
    def __init__(self, numbers, desired_sum):
        if isinstance(numbers, list):
            self.numbers = numbers
        else:
            raise ValueError("numbers should be list")
        if isinstance(desired_sum, int):
            self.desired_sum = desired_sum
        else:
            raise ValueError("desi  red_sum should be int")

    def metod(self):
        self.c = 0
        self.x = 0
        while self.c != 1:
            self.x = self.x - 1
            self.chisla = self.numbers[self.x]
            self.chisla = int(self.chisla)
            for i in self.numbers:
                if self.desired_sum - (i + self.chisla) == 0:
                    return f'{self.numbers.index(i)},{self.numbers.index(self.chisla)}'
algoritm = Algoritm(numbers=[2, 7, 11, 15], desired_sum=26)
print(algoritm.metod())