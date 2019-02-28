school_performance = [{'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
                      {'school_class': '4b', 'scores': [4, 2, 5, 3, 5]},
                      {'school_class': '5a', 'scores': [4, 4, 3, 5, 3, 4]},
                      {'school_class': '5b', 'scores': [3, 3, 4, 2, 3, 5]},
                      {'school_class': '6a', 'scores': [4, 4, 5, 5, 5]},
                      {'school_class': '6b', 'scores': [4, 5, 3, 2, 3]}]

average_score_class = 0
amount_score = 0
amount_class = 0
for number_class in school_performance:
    average_score_school = 0
    for key, value in number_class.items():
        if key == 'scores':
            amount = 0
            students = 0
            for value in number_class['scores']:
                amount += value
                students += 1
            average_score_class = round(amount / students, 2)
        else:
            class_level = value
    score_class = f"Класс {class_level}: средний балл {average_score_class}."
    print(score_class)
    amount_score += average_score_class
    amount_class += 1
average_score_school = round(amount_score / amount_class, 2)
score_school = f"Средний балл по школе {average_score_school}."
print(score_school)