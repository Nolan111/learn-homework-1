"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

questions_and_answers = {"Как дела": "Хорошо!", "Что делаешь?": "Программирую", "Как поел?": 'Вкусно'}

def ask_user(answers_dict):

  
    while True:
        user = input("Пользователь:")
        if user in answers_dict:
            print(answers_dict[user])
    
        else:
            print('Я ХЗ')       
if __name__ == "__main__":
    ask_user(questions_and_answers)
