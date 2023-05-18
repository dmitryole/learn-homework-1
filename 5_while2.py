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

questions_and_answers = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую"}

def search_questions(question):
  questions = list(questions_and_answers)
  if question in questions:
    return True
  else:
    return None


def ask_user(answers_dict):
    while True:
      user_say = input('Введите вопрос\n')
      if (search_questions(user_say) != None):
        print(questions_and_answers[user_say])
    
    
if __name__ == "__main__":
    ask_user(questions_and_answers)
