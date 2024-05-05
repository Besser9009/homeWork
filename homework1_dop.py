# Задание "Средний балл":
# Вам необходимо решить задачу из реальной жизни: "школьные учителя устали подсчитывать вручную средний балл каждого
# ученика, поэтому вам предстоит автоматизировать этот процесс":

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
print(students)

def newList():
    grades_1 = []
    for i in range(len(grades)):
        sum = 0
        counter = 0
        for j in range(len(grades[i])):
            sum += grades[i][j]
            counter += 1
        grades_1.append(sum / counter)
    return grades_1

grades = newList()
print(grades)

average_score = {}
for name in students:
    for res in grades:
        average_score[name] = res
        grades.remove(res)
        break
print(average_score)


