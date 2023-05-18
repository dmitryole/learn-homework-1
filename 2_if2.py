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
def comparison(one, two):
  if (type(one) != type(two)):
    return 0
  elif (one == two):
    return 1
  elif (one != two and len(one) > len(two)):
    return 2
  elif (one != two and two == 'learn'): #Отсутствует приоретизация на уровне постоновки задачи
    return 3

def main():
    print(comparison('строка 1', 0)) #0
    print(comparison('строка 1', 'строка 1')) #1
    print(comparison('строка 1', 'строк')) #2
    print(comparison('строка 1', 'learn')) #2
    print(comparison('стр', 'learn')) #3
    
if __name__ == "__main__":
    main()
