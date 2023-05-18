"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""
def sum_phone(dicts):
    for dict in dicts:
      sum_sold_phone = sum(dict['items_sold'])
      print (f'Total number of sales {dict["product"]}: {sum_sold_phone}')

def avg_phone(dicts):
    for dict in dicts:
      avg = round(sum(dict['items_sold'])/len(dict['items_sold']))
      print (f'Average number of sales {dict["product"]}: {avg}')

def sum_phones(dicts):
    sum_sold_phones = 0
    for dict in dicts:
      sum_sold_phones += sum(dict['items_sold'])
    print (f'Total number of sales: {sum_sold_phones}')

def avg_phones(dicts):
  sum_sold_phones = 0
  for dict in dicts:
      sum_sold_phones += sum(dict['items_sold'])
  avg_sold_phones = round((sum_sold_phones)/len(dicts))
  print (f'Average number of sales: {avg_sold_phones}')

phones = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
    ]

def main():
  sum_phone(phones)
  avg_phone(phones)
  sum_phones(phones)
  avg_phones(phones)
    
if __name__ == "__main__":
    main()
