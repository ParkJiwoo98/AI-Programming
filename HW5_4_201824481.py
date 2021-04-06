class Quizzes:
    grade = []
    def __init__(self, grade1, grade2, grade3, grade4, grade5, grade6):
        self.grade.append(grade1)
        self.grade.append(grade2)
        self.grade.append(grade3)
        self.grade.append(grade4)
        self.grade.append(grade5)
        self.grade.append(grade6)

    def average(self):
        sum = 0
        lowest = self.grade[0]
        for i in range(len(self.grade)):
            sum += self.grade[i]
            if lowest > self.grade[i]:
                lowest = self.grade[i]
        sum -= lowest
        average = sum / 5
        return average

    def __str__(self):
        return "Quiz average: " + str(self.average())

grade = []
for i in range(0, 6):
    grade.append(int(input('Enter grade on quiz {}: '.format(i + 1))))
quiz = Quizzes(grade[0], grade[1], grade[2], grade[3], grade[4], grade[5])
print(quiz.__str__())