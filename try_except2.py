def get_summ(num_one, num_two):
    try:
        summ = int(num_one) + int(num_two)
        return summ
    except ValueError:
        print("Нужно вводить только целые числа")   


num_one = input("Введите число ")
num_two = input("Введите число ")
print(get_summ(num_one, num_two))