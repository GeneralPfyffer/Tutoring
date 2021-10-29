import json

#definitions
data = open(r'C:\Users\eneav\OneDrive\Dokumente\Uni\Informatik\Python\Students\data.csv', 'r+')
students = {}
data_append = open(r'C:\Users\eneav\OneDrive\Dokumente\Uni\Informatik\Python\Students\data.csv', 'a')

#create dict of students
for student in data:
        student = student.split(',')
        temp_name = student.pop(0)
        temp_salary = student.pop(0)
        students[temp_name] = [temp_salary]
        for lesson in student:
            temp_time = student.pop(0)
            temp_date = student.pop(0)
            add = temp_time, temp_date
            students[temp_name].append(add)

#start
action = input("What do you want to do?\n1. Add lesson\n2. Add student\n3. Show total of lessons and total of money earned\n")

if action == '1':
    name = input('Who got tutored?\n')
    date = input('What date was the lesson?\n')
    time = input('How long was the lesson?\n')
    data_append.write(f',{date},{time}')
elif action == '2':
    name = input('What is the name of the student?\n')
    salary = input('How much do they pay?\n')
    data_append.write(f'\n{name},{salary}')
elif action == '3':
    name = input('Which student?\n')
    salary = students[name].pop(0)
    lesson_count = students[name]
    earnings = 0
    for lesson in students[name]:
        lesson = list(lesson)
        earnings += salary*lesson[1]
    print(f'{name} has had a total of {lesson_count} lessons.\nYou earned {earnings}.- from this student.')

data.close()
data_append.close()