import string
import sys
import sqlite3
from spellchecker import SpellChecker
from design.check_text import Ui_CheckWindow
from design.new_student import Ui_NewStudentWindow
from design.criteries_wondow import Ui_CriteriesWindow
from design.plagiat_window import Ui_PlagiatWindow
from design.result_window import Ui_ResultWindow
from design.main_window import Ui_MainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem


class NoFileError(Exception):
    pass


class NoNameError(Exception):
    pass


class NoNameInBaseError(Exception):
    pass


class NewStudentWidget(QMainWindow, Ui_NewStudentWindow):
    def __init__(self):
        super().__init__()
        self.text = None
        self.setupUi(self)
        self.setWindowTitle('NewStudentWindow')
        self.add_esse_btn.clicked.connect(self.get_f)
        self.ok_btn.clicked.connect(self.save)

    def get_f(self):
        fname = QFileDialog.getOpenFileName(
            self, 'Выбрать текст', '',
            '(*.txt)')[0]
        self.text = open(fname).read()

    def save(self):
        import sqlite3
        b_d = sqlite3.connect("students_rus_esse_base")
        cur = b_d.cursor()
        cur.execute("""INSERT INTO esse(text)
                                                VALUES(?)""", (self.text,))
        cur.execute("""INSERT INTO students_marks(name)
                                                        VALUES(?)""", (self.name_edit.text(),))
        b_d.commit()
        id_text = cur.execute("""SELECT id FROM esse where text = ?""", (self.text,)).fetchall()[0][0]
        id_student = cur.execute("""SELECT id FROM students_marks where name = ?""",
                                 (self.name_edit.text(),)).fetchall()[0][0]
        cur.execute("""INSERT INTO esse_students_mark(id_text, id_marks)
                                                                VALUES(?, ?)""", (id_text, id_student))
        b_d.commit()
        b_d.close()
        self.statusBar().showMessage("Успешно!")


class CriteriesWidget(QMainWindow, Ui_CriteriesWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('CriteriesWindow')
        self.esse_1_btn.clicked.connect(self.show_criteries)
        self.esse_2_btn.clicked.connect(self.show_criteries)
        self.esse_3_btn.clicked.connect(self.show_criteries)
        self.change_btns = [self.page_btn, self.page_btn_2, self.page_btn_3, self.page_btn_4]
        for i in range(4):
            self.change_btns[i].hide()
            self.change_btns[i].clicked.connect(self.change_criteries)

    def show_criteries(self):
        if self.esse_1_btn.isChecked():
            self.pixmaps = [QPixmap('photos/cr_1_1.jpg'), QPixmap('photos/cr_1_2.jpg'),
                            QPixmap('photos/cr_1_3.jpg'), QPixmap('photos/cr_1_4.jpg')]
        if self.esse_2_btn.isChecked():
            self.pixmaps = [QPixmap('photos/cr_2_1.jpg'), QPixmap('photos/cr_2_2.jpg'),
                            QPixmap('photos/cr_2_3.jpg'), QPixmap('photos/cr_2_4.jpg')]
        if self.esse_3_btn.isChecked():
            self.pixmaps = [QPixmap('photos/cr_3_1.jpeg'), QPixmap('photos/cr_3_2.jpeg'),
                            QPixmap('photos/cr_3_3.jpeg'), QPixmap('photos/cr_3_4.jpeg')]
        self.label.setPixmap(self.pixmaps[0])
        self.label.resize(500, 500)
        for i in range(4):
            self.change_btns[i].show()

    def change_criteries(self):
        self.label.setPixmap(self.pixmaps[int(self.sender().text()) - 1])


class PlagiatWidget(QMainWindow, Ui_PlagiatWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('PlagiatWindow')
        self.text1, self.text2 = set(), set()
        self.same_str_list.hide()
        self.compare_btn.clicked.connect(self.compare)
        self.checkBox.clicked.connect(self.show_same_str)

    def get_text_1(self):
        try:
            if self.name_edit.text() == 'Фамилия и имя ученика':
                raise NoNameError
            b_d = sqlite3.connect("students_rus_esse_base")
            cur = b_d.cursor()
            self.id_student = cur.execute("""SELECT id from students_marks
                                                                where name = ?""",
                                          (self.name_edit.text(),)).fetchall()
            if not self.id_student:
                raise NoNameInBaseError
            id_text = cur.execute("""SELECT id_text from esse_students_mark
                                                                where id_marks = ?""",
                                  (self.id_student[0][0],)).fetchall()
            self.text1 = cur.execute("""SELECT text from esse
                                                                where id = ?""", (id_text[0][0],)).fetchall()[0][0]
            self.text1 = set(filter(lambda x: x not in string.whitespace, self.text1.split('\n')))
            b_d.close()
        except NoNameError:
            self.statusBar().showMessage('Вы не ввели имя.')
        except NoNameInBaseError:
            self.statusBar().showMessage('Такого ученика нету в базе данных.')

    def get_text_2(self):
        try:
            if self.name_edit_2.text() == 'Фамилия и имя ученика':
                raise NoNameError
            b_d = sqlite3.connect("students_rus_esse_base")
            cur = b_d.cursor()
            self.id_student = cur.execute("""SELECT id from students_marks
                                                                where name = ?""",
                                          (self.name_edit_2.text(),)).fetchall()
            if not self.id_student:
                raise NoNameInBaseError
            id_text = cur.execute("""SELECT id_text from esse_students_mark
                                                                where id_marks = ?""",
                                  (self.id_student[0][0],)).fetchall()
            self.text2 = cur.execute("""SELECT text from esse
                                                                where id = ?""", (id_text[0][0],)).fetchall()[0][0]
            self.text2 = set(filter(lambda x: x not in string.whitespace, self.text2.split('\n')))
            b_d.close()
        except NoNameError:
            self.statusBar().showMessage('Вы не ввели имя.')
        except NoNameInBaseError:
            self.statusBar().showMessage('Такого ученика нету в базе данных.')

    def compare(self):
        self.get_text_1()
        self.get_text_2()
        if self.text1 and self.text2:
            res = round(len(self.text1 & self.text2) / len(self.text1 | self.text2) * 100, 2)
            self.label_2.setText(f"{res}%")
            self.label.setText(f"Плагиат на")

    def show_same_str(self):
        if self.checkBox.isChecked():
            self.same_str_list.show()
            self.same_str_list.addItems(sorted(list(self.text1 & self.text2), reverse=True))
        else:
            self.same_str_list.hide()
            self.same_str_list.clear()


class CheckWidget(QMainWindow, Ui_CheckWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('CheckWindow')
        self.save_btn.hide()
        self.ok_btn.clicked.connect(self.get_text)
        self.save_btn.clicked.connect(self.save)

    def get_text(self):
        try:
            if self.name_edit.text() == 'Фамилия и имя ученика':
                raise NoNameError
            b_d = sqlite3.connect("students_rus_esse_base")
            cur = b_d.cursor()
            self.id_student = cur.execute("""SELECT id from students_marks
                                                    where name = ?""", (self.name_edit.text(),)).fetchall()
            if not self.id_student:
                raise NoNameInBaseError
            id_text = cur.execute("""SELECT id_text from esse_students_mark
                                                    where id_marks = ?""", (self.id_student[0][0],)).fetchall()
            self.text = cur.execute("""SELECT text from esse
                                                    where id = ?""", (id_text[0][0],)).fetchall()[0][0]
            b_d.close()
            self.save_btn.show()
            self.original_edit.setPlainText(self.text)
            self.check_cliche()
            self.num_words()
            self.num_paragraphs()
            self.coorect_words()

        except NoNameError:
            self.original_edit.setPlainText('Вы не ввели имя.')
        except NoNameInBaseError:
            self.original_edit.setPlainText('Такого ученика нету в базе данных.')

    def check_cliche(self):
        b_d = sqlite3.connect("clishe_base")
        cur = b_d.cursor()
        clishes = cur.execute("""SELECT name FROM clishe""").fetchall()
        for lines in self.text.split('\n'):
            for clishe in clishes:
                if clishe[0] in lines.lower():
                    self.composition_point_spin.setValue(1)
                    break
        b_d.close()

    def num_paragraphs(self):
        n = len(list(filter(lambda x: x.startswith('\t'), self.text.split('\n'))))
        if n == 0:
            n = len(list(filter(lambda x: x == '', self.text.split('\n'))))
        if n >= 4:
            self.subsequence_point_spin.setValue(self.subsequence_point_spin.value() + 1)
            self.argument_point_spin.setValue(3)
        if n == 3:
            self.argument_point_spin.setValue(2)

    def coorect_words(self):
        spell = SpellChecker(language='ru')
        table = str.maketrans("", "", string.punctuation + '–«»')
        mistakes = []
        for line in self.text.split('\n'):
            l = line.translate(table)
            mistakes += list(spell.unknown(filter(lambda x: len(x) >= 3, l.split())))
        new_text = ""
        for line in self.text.split('\n'):
            new_line = ""
            for word in line.split():
                for mistake in mistakes:
                    if word.translate(table) == mistake:
                        new_line += f"({word}) "
                        break
                else:
                    new_line += f"{word} "
            new_text += f"{new_line}\n"
        self.result_edit.setPlainText(new_text)
        n = len(mistakes)
        if n <= 1:
            self.grammer_point_spin.setValue(10)
        elif n <= 10:
            self.grammer_point_spin.setValue(5)
        else:
            self.grammer_point_spin.setValue(1)

    def num_words(self):
        n = sum(map(lambda x: len(x.split()), self.text.split()))
        if n >= 70:
            self.subsequence_point_spin.setValue(self.subsequence_point_spin.value() + 1)

    def save(self):
        sum_points = self.understand_meaning_point_spin.value() + self.subsequence_point_spin.value() + \
                     self.argument_point_spin.value() + self.composition_point_spin.value() + \
                     self.grammer_point_spin.value()

        b_d = sqlite3.connect("students_rus_esse_base")
        cur = b_d.cursor()
        cur.execute("""UPDATE students_marks
                                SET understand_meaning_point = ?
                                WHERE id = ?""", (self.understand_meaning_point_spin.value(), self.id_student[0][0]))
        cur.execute("""UPDATE students_marks
                                        SET argument_point = ?
                                        WHERE id = ?""", (self.subsequence_point_spin.value(), self.id_student[0][0]))
        cur.execute("""UPDATE students_marks
                                        SET subsequence_point = ?
                                        WHERE id = ?""", (self.argument_point_spin.value(), self.id_student[0][0]))
        cur.execute("""UPDATE students_marks
                                        SET composition_point = ?
                                        WHERE id = ?""", (self.composition_point_spin.value(), self.id_student[0][0]))
        cur.execute("""UPDATE students_marks
                                        SET grammer_point = ?
                                        WHERE id = ?""", (self.grammer_point_spin.value(), self.id_student[0][0]))
        cur.execute("""UPDATE students_marks
                                        SET main_mark = ?
                                        WHERE id = ?""", (sum_points, self.id_student[0][0]))
        b_d.commit()
        b_d.close()
        self.statusBar().showMessage("Успешно!")


class ResultWidget(QMainWindow, Ui_ResultWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('MarksWindow')
        self.set_results()

    def set_results(self):
        b_d = sqlite3.connect("students_rus_esse_base")
        cur = b_d.cursor()
        students = cur.execute("""SELECT name, main_mark from students_marks""").fetchall()
        b_d.close()
        self.res_table.setRowCount(len(students) - 1)
        for j in range(len(students)):
            self.res_table.setItem(j, 0, QTableWidgetItem(str(students[j][0])))
            self.res_table.setItem(j, 1, QTableWidgetItem(str(students[j][1])))


class MainWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.managment_btn.clicked.connect(self.show_window_criteries)
        self.plagiat_btn.clicked.connect(self.show_window_plagiat)
        self.format_btn.clicked.connect(self.show_window_check)
        self.marks_btn.clicked.connect(self.show_window_result)
        self.add_student_btn.clicked.connect(self.show_window_new_student)
        self.inform_btn.clicked.connect(self.show_inform)
        self.inform_edit.hide()

    def show_window_new_student(self):
        self.w = NewStudentWidget()
        self.w.show()

    def show_window_criteries(self):
        self.w = CriteriesWidget()
        self.w.show()

    def show_window_plagiat(self):
        self.w = PlagiatWidget()
        self.w.show()

    def show_window_check(self):
        self.w = CheckWidget()
        self.w.show()

    def show_window_result(self):
        self.w = ResultWidget()
        self.w.show()

    def show_inform(self):
        if self.inform_edit.isHidden():
            self.inform_edit.show()
        else:
            self.inform_edit.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWidget()
    ex.show()
    sys.exit(app.exec_())
