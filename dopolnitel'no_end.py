grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# a = [5, 3, 3, 5, 4]
# b = [2, 2, 2, 3]
# c = [4, 5, 5, 2]
# d = [4, 4, 3]
# e = [5, 5, 5, 4, 5]
# a = sum(a) / len(a)
# b = sum(b) / len(b)
# c = sum(c) / len(c)
# d = sum(d) / len(d)
# e = sum(e) / len(e)
# print(a, b, c, d, e)
# a1 = {'Johnny'}
# b1 = {'Bilbo'}
# c1 = {'Steve'}
# d1 = {'Khendrik'}
# e1 = {'Aaron'}
# students_srednee = (a1, a, b1, b, c1, c, d1, d, e1, e)
# print(students_srednee)
# ЭТО СЛИШКОМ ДОЛГО И СКОРЕЕ ВСЕГО НЕПРАВИЛЬНО
# БОЛЕЕ ПОДРОБНО ИЗУЧИВ ПРОСТОРЫ ИНТЕРНЕТА НАШЕЛ ТАКОЕ РЕШЕНИЕ:
students_sort = sorted(students)
print(students_sort)
grades_srednee = (sum(grades[0]) / len(grades[0]),
                  sum(grades[1]) / len(grades[1]),
                  sum(grades[2]) / len(grades[2]),
                  sum(grades[3]) / len(grades[3]),
                  sum(grades[4]) / len(grades[4]))
print(grades_srednee)
sred_otcenka = {students_sort[0]: grades_srednee[0],
                students_sort[1]: grades_srednee[1],
                students_sort[2]: grades_srednee[2],
                students_sort[3]: grades_srednee[3],
                students_sort[4]: grades_srednee[4]}
print(sred_otcenka)

