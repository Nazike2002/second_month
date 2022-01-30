import sqlite3

data_basa = sqlite3.connect("Plan.db")
sql = data_basa.cursor()
sql.execute("CREATE TABLE IF NOT EXISTS users(Name TEXT,Day TEXT,Morning TEXT,Lunch TEXT,Evening TEXT)")
data_basa.commit()


def registr_user():
    global user_name, user_day, user_morning, user_lunch, user_evening
    while True:
        user_name = input("Как вас зовут: ")
        user_day = input("Какой день недели:")
        user_morning = input("Какие планы на утро:")
        user_lunch = input("Какие планы на обед:")
        user_evening = input("Какие планы на вечер: ")

        sql.execute(f"SELECT Day FROM users WHERE DAY = '{user_day}'")
        if sql.fetchone() is None:
            sql.execute(f"INSERT INTO users VALUES (?,?,?,?,?)",
                        (user_name, user_day, user_morning, user_lunch, user_evening))
            data_basa.commit()
            for value in sql.execute("SELECT * FROM users"):
                print(value)
        else:
            print("День недели не должен повторяться!")
            for value in sql.execute("SELECT * FROM users"):
                print(value)
        delete_choose = input("Есть ли у вас выполненные дни?"
                              "Если есть то напишите день недели,если нету то напишите нет:")
        sql.execute("DELETE FROM users WHERE Day == ?", (delete_choose,))
        if delete_choose != "нет":
            for value in sql.execute("SELECT * FROM users"):
                print(value)
            continue
        choose = input("Хотите продолжить записывать свои планы? да или нет")
        if choose == "да":
            continue
        elif choose == "нет":
            for value in sql.execute("SELECT * FROM users"):
                print(value)
            print("Ваши планы зарегистрированы!")
            break
        else:
            print("Напишите только да или нет")
            continue


if __name__ == '__main__':
    registr_user()