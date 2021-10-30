import json
from json.decoder import JSONDecodeError

#definitions
file = r'C:\Users\eneav\OneDrive\Dokumente\Uni\Informatik\Python\Students\data.json'
with open(file, 'r') as f:
    try:
        students = json.loads(f.read())
    except JSONDecodeError:
        students = {}

#functions
def add_student(name, full_name, salary, file, students):
    with open(file, 'w+') as f:
        '''try:
            students = json.loads(f.read())
        except JSONDecodeError: students = {}'''
        students[name] = {"Personals": {
            "name": full_name,
            "salary": salary
        },
        "Lessons": {
        }
        }
        f.write(json.dumps(students))
    '''students = json.loads(file)
    students[name] = [salary]
    students = json.dumps(students)
    file.write(students)'''
    '''s = {}
    d = {}
    s[salary] = {}
    d[name] = s
    print(json.dumps(d))'''

def add_lesson(name, money, date, file, students):
    with open(file, 'w+') as f:
        '''students = json.loads(f.read())'''
        student = students[name]
        lessons = student["Lessons"]
        lessons[date] = money
        f.write(json.dumps(students))
'''#create dict of students
for student in data:
        student = student.split(',')
        temp_name = student.pop(0)
        temp_salary = student.pop(0)
        students[temp_name] = [temp_salary]
        if not student == []:
            for lesson in student:
                temp_time = student.pop(0)
                temp_date = student.pop(0)
                add = temp_time, temp_date
                students[temp_name].append(add)
        else: pass'''

#start
action = input("What do you want to do?\n1. Add lesson\n2. Add student\n3. Show total of lessons and total of money earned\n")

if action == '1':
    name = input('Who got tutored?\n')
    date = input('What date was the lesson?\n')
    money = input('How much money did they give?\n')
    add_lesson(name, money, date, file, students)
elif action == '2':
    name = input('What key do you want to use?\n')
    full_name = input('What is the name of the student?\n')
    salary = input('How much do they pay?\n')
    add_student(name, full_name, salary, file, students)
elif action == '3':
    name = input('Which student?\n')
    salary = students[name].pop(0)
    lesson_count = students[name]
    earnings = 0
    for lesson in students[name]:
        lesson = list(lesson)
        earnings += salary*lesson[1]
    print(f'{name} has had a total of {lesson_count} lessons.\nYou earned {earnings}.- from this student.')
