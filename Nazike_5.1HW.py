import re


class Name:
    def __init__(self):
        self.text = 'MOCK_DATA.txt'
        self.file_read = open(self.text, mode='r', encoding='Latin-1')
        self.class_text = self.file_read.read()

    def metod_name(self):
        self.rezultat_name = 'rezultat_name.txt'
        self.final_rezultat_name = open(self.rezultat_name, mode='w', encoding='Latin-1')
        self.search_name = r"[A-Z]+[^0-9_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{1,}[a-z]*\s+[A-Z]+[^0-9_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{1,}[a-z]*\s*[A-Z]*[a-z]*\s+"
        self.rezultat_name_all = re.findall(self.search_name, self.class_text)
        for item1 in self.rezultat_name_all:
            print(item1)
            self.final_rezultat_name.write(item1 + "\n")
        return f'Total: {str(len(self.rezultat_name_all))}'


name1 = Name()
print(name1.metod_name())


class Email(Name):
    def __init__(self):
        super(Email, self).__init__()
        self.rezultat_email = 'rezltat_email.txt'
        self.final_rezultat_email = open(self.rezultat_email, mode='w', encoding='Latin-1')
        self.search_email = r'\s+[\w.-]+@[\w.-]+\.[\w.-]+'
        self.rezultat_email_all = re.findall(self.search_email, self.class_text)

    def metod_email(self):
        for item2 in self.rezultat_email_all:
            print(item2)
            self.final_rezultat_email.write(item2 + "\n")
        return f'Total: {str(len(self.rezultat_email_all))}'


email1 = Email()
print(email1.metod_email())


class Rasshirenie(Name):
    def __init__(self):
        super(Rasshirenie, self).__init__()
        self.rezultat_rasshirenie = 'rezultat__rasshirenie.txt'
        self.final_rezultat_rasshirenie = open(self.rezultat_rasshirenie, mode='w', encoding='Latin-1')
        self.search_rasshirenie = r'\s[\w.-]+\.\w+'
        self.rezultat_rasshirenie_all = re.findall(self.search_rasshirenie, self.class_text)

    def metod_rasshirenie(self):
        for item3 in self.rezultat_rasshirenie_all:
            print(item3)
            self.final_rezultat_rasshirenie.write(item3 + "\n")
        return f'Total: {str(len(self.rezultat_rasshirenie_all))}'


rasshirenie1 = Rasshirenie()
print(rasshirenie1.metod_rasshirenie())


class Color(Name):
    def __init__(self):
        super(Color, self).__init__()
        self.rezultat_color = 'rezult_color.txt'
        self.final_rezultat_color = open(self.rezultat_color, mode='w', encoding='Latin-1')
        self.search_color = r'#[\w.-]+'
        self.rezultat_color_all = re.findall(self.search_color, self.class_text)

    def metod_color(self):
        for item4 in self.rezultat_color_all:
            print(item4)
            self.final_rezultat_color.write(item4 + "\n")
        return f'Total: {str(len(self.rezultat_color_all))}'


color1 = Color()
print(color1.metod_color())
