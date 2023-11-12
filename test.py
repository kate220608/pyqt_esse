import sqlite3
b_d = sqlite3.connect("students_rus_esse_base")
cur = b_d.cursor()
students = cur.execute("""SELECT name, main_mark from students_marks""").fetchall()
b_d.close()
print(students)

