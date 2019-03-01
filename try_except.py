def ask_user():
    dialog = {"Как дела?": "Хорошо", "Что делаешь?": "Программирую",
              "Как настроение?": "Отлично", "Когда освободишься?": "Сегодня вряд-ли",
              "Сколько тебе лет?": "Не знаю", "Как тебя зовут?": "Оператор while"}
    
    while True:
        try:
            question = input("Спроси что-нибудь? ")
        except KeyboardInterrupt:
            print("Пока")
            break
        if question in dialog:
            print(dialog[question])
        else:
            print("Я не знаю, ")

ask_user()