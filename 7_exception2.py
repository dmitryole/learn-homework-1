"""

Домашнее задание №1

Исключения: приведение типов

* Перепишите функцию discounted(price, discount, max_discount=20)
  из урока про функции так, чтобы она перехватывала исключения,
  когда переданы некорректные аргументы.
* Первые два нужно приводить к вещественному числу при помощи float(),
  а третий - к целому при помощи int() и перехватывать исключения
  ValueError и TypeError, если приведение типов не сработало.
    
"""

def discounted(price, discount, max_discount=20):
  try:
    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(int(max_discount))
    if max_discount >= 100:
      raise ValueError('Максимальная скидка не должна быть больше 100')
    if discount >= max_discount:
      price_with_discount = price
    else:
      price_with_discount = price - (price * discount / 100)
    return price_with_discount
  except (TypeError):
        return('Ошибка в типе данных')
  except (ValueError):
        return('Ошибка в значении')
    
if __name__ == "__main__":
  print(discounted(100, 2))
  print(discounted(100, "3"))
  print(discounted("100", "4.5"))
  print(discounted("five", 5)) #ValueError
  print(discounted("сто", "десять")) #ValueError
  print(discounted(100.0, 5, "10"))
  print(discounted(100.0, {4, 5, 6}, "10")) #ValueError