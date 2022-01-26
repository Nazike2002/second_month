class Buble_sort:
    def __init__(self, array):
        if isinstance(array, list):
            self.array = array
        else:
            raise ValueError("Array shuld be list")

    def buble_sort(self):
        self.swap = False
        for number_1 in range(len(self.array) - 1, 0, -1):
            for number_2 in range(number_1):
                if self.array[number_2] > self.array[number_2 + 1]:
                    self.array[number_2], self.array[number_2 + 1] = self.array[number_2 + 1], self.array[number_2]
                    self.swap = True
            if self.swap:
                self.swap = False
            else:
                break
        return self.array


Sort1 = Buble_sort(array=[64, 23, 89, 6, 1, 12, 33])
print(Sort1.buble_sort())


class QuickSort:
    def __init__(self, array):
        if isinstance(array, list):
            self.array = array
        else:
            raise ValueError("Array shuld be list")

    def speed_sort(self, array=None):
        if array is None:
            array = self.array
        if len(array) <= 1:
            return array
        else:
            self.element = array[0]
            left = self.left = [elem for elem in array if elem < self.element]
            middle = self.middle = [nums for nums in array if nums == self.element]
            right = self.right = [elem for elem in array if elem > self.element]

            return self.speed_sort(left) + middle + self.speed_sort(right)


quik = QuickSort(array=[64, 23, 89, 6, 1, 12, 33])
print(quik.speed_sort())


class Binar_sort:
    def __init__(self, des_n):
        if isinstance(des_n, int):
            self.des_n = des_n
        else:
            raise ValueError("Des_n should be int")

    def b_tree(self):
        self.array = [64, 23, 89, 6, 1, 12, 33, 77]
        self.array.sort()
        print(self.array)
        self.mid = len(self.array) // 2
        self.low = 0
        self.high = len(self.array) - 1

        while self.array[self.mid] != self.des_n and self.low <= self.high:
            if self.des_n > self.array[self.mid]:
                self.low = self.mid + 1
            else:
                self.high = self.mid - 1
            self.mid = (self.low + self.high) // 2
        if self.low > self.high:
            return f'no value'
        else:
            return f'Index: {self.mid}'


bin = Binar_sort(des_n=77)
print(bin.b_tree())


class Algoritm():
    def __init__(self, numbers):
        if isinstance(numbers, int) and numbers < 1000 and numbers >= 100:
            self.numbers = numbers
        else:
            raise ValueError("Numbers should be int and numbers < 1000 and numbers >=100")

    def metod(self):
        self.razdel = {}
        if self.numbers >= 0 and str(self.numbers) == str(self.numbers)[::-1]:
            self.razdel['Universal'] = self.numbers
            for i, k in self.razdel.items():
                return f'{i}:{k}'
        else:
            self.razdel['Neniversal'] = self.numbers
            for i, k in self.razdel.items():
                return f'{i}:{k}'


algoritm1 = Algoritm(numbers=343)
print(algoritm1.metod())