import sqlite3
b_d = sqlite3.connect("students_rus_esse_base")
cur = b_d.cursor()
res = cur.execute("""SELECT understand_meaning_point, argument_point, 
                            subsequence_point, composition_point, grammer_point from students_marks
                            where name = ?""", ("Антон Павлов", )).fetchall()
b_d.commit()
b_d.close()
print(res)