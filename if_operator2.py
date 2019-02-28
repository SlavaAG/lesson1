def comparison(first_word, second_word):
    if (type(first_word) or type(second_word)) is not str:
        return 0
    elif len(first_word) == len(second_word):
        return 1
    elif len(first_word) != len(second_word) and second_word == "learn":
        return 3
    elif len(first_word) > len(second_word):
        return 2


repetition = int(input("Сколько раз будем сравнивать? "))
for i in range(repetition):
    first_word = input("Введите первую строку: ")
    second_word = input("Введите вторую строку: ")
    print(comparison(first_word, second_word))
print("Работа завершена.")