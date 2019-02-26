def age_level(user_age):
	if user_age < 2:
		if user_age <= 0:
			return"Ты похоже еще не родился"
		return "Тебе рано еще чем-то заниматься."
	elif user_age < 7:
		return "Пора в детский сад"
	elif user_age < 17:
		return "Школа ждет"
	elif user_age < 22:
		return "Пора выбрать ВУЗ"
	elif user_age < 65:
		return "Ну вот, можно и по-работать"
	else:
		if user_age > 120:
			return "Ты либо долгожитель, либо неправильно указал возраст"
		return "Пенсия, можно передохнуть (если хочешь)"


user_age = int(input("Сколько вам лет? "))
user_level = age_level(user_age)
print(user_level)