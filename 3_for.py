"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():

    school = [
    {'school_class': '4a', 'scores': [3,2,4,4,1]},
    {'school_class': '5a', 'scores': [3,3,4,5,2]},
    {'school_class': '6a', 'scores': [3,5,4,2,2]},
    {'school_class': '7a', 'scores': [3,2,2,5,2]},
    {'school_class': '8a', 'scores': [3,1,5,5,2]},
    ]
    total_sum = 0
    total_len =  0
    for class_ in school: 
        class_score = class_["scores"]
        sum_score_class = 0
        for score in class_score:
            sum_score_class += score

        total_sum += sum_score_class
        total_len += len(class_score)
        

        print(f"Средняя оценка в {class_['school_class']} {sum_score_class/(len(class_score))}")
    print(f"Средняя оценка в школе {total_sum/total_len}")


    
if __name__ == "__main__": 
    main()

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in mylist:
    print(i + 1)

a = input("дима питон: ")
for word in a:
    print(word)

