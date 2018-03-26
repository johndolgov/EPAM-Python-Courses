import operator
quantity_students = int(input('Please Enter Quantity of Students: ' ))
quantity_tasks = int(input('Please Enter Quantity of Tasks: '))
list_of_students = []
for i in range(quantity_students):
    a = input('Please Enter a Name of Student: ')
    list_of_students.append(a)
dict_of_notes = {number_of_task : 0 for number_of_task in range(1,quantity_tasks+1)}
list_of_students_with_notes = [] ##Не словарь т.к. могут быть одинаковые имена
for student in list_of_students:
    list_of_students_with_notes.append([student,0])
for task in range (quantity_tasks):
    sum = 0
    number_student = 0
    while number_student < quantity_students: ## while для того, чтобы возвращаться назад в цикле, если вдруг введут плохое число
        note = int(input('Please input note in range 0 - 10 for task№{} to student {} : '.format(task+1,list_of_students_with_notes[number_student][0])))
        list_of_students_with_notes[number_student][1] += note
        number_student += 1
        if note > 10 or note < 0:
            print ('Nope, enter note in range 0 - 10, do it again')
            list_of_students_with_notes[number_student][1] -= note
            number_student-=1
            continue
        sum += note
    dict_of_notes[task+1] += sum
list_of_students_with_notes.sort(key=lambda list_of_students_with_notes:list_of_students_with_notes[1]) ##Сортировка учеников по сумме баллов
list_of_notes_values = sorted(dict_of_notes.items(), key=operator.itemgetter(1)) ##Сортировка заданий от самого сложного до самого легкого
print('The smartest students are: ')
for i in range(3):
    print(list_of_students_with_notes.pop()[0])
print ('The toughest tasks for students were: ')
for i in range(3):
    print('Task№ {}'.format(list_of_notes_values.pop(0)[0]))
