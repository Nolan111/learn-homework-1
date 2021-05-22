"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def string (string_1, string_2):
    if not isinstance(string_1, str) or not isinstance(string_2, str):
      return 0
    elif string_1 == string_2:
      return 1
    elif len(string_1) > len(string_2):
      return 2
    elif string_2 == 'learn':
      return 3
    else: 
      return "строки разные и  вторая строка не 'learn'"

if __name__ == "__main__":


    print(string(10.5, "test"))
    print(string("test", 22))
    print(string("test", "test"))
    print(string("teeest", "test"))
    print(string("aaa", "learn"))
    print(string("afd", "glearn"))



