done_homework=12
time_homework=1.5
name_course=("Python")
time_oneHomework=time_homework/done_homework # В дробных числах
time_minutes=int(time_homework*60)//done_homework
time_secunds=(((time_homework*60)/done_homework)-((time_homework*60)//done_homework))*60
print("Курс:",name_course,", Всего задач:",done_homework,", Затрачено часов:",time_homework,", Среднее время выполнения ",time_oneHomework)
print("или ",time_minutes,"минут ",int(time_secunds), "секунд")
