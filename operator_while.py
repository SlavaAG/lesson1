def ask_user():
    dialog = {"Как дела?": "Хорошо", "Что делаешь?": "Программирую",
              "Как настроение?": "Отлично", "Когда освободишься?": "Сегодня вряд-ли",
              "Сколько тебе лет?": "Не знаю", "Как тебя зовут?": "Оператор while"}
    
    while True:
        question = input("Спроси что-нибудь? ")
        if question in dialog:
            print(dialog[question])
        else:
            print("Я не знаю, ")

ask_user()