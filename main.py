import string
import sys
import sqlite3
from spellchecker import SpellChecker
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem, QStatusBar


class NoFileError(Exception):
    pass


class NoNameError(Exception):
    pass


class NoNameInBaseError(Exception):
    pass


class Criteries_Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('criteries_window.ui', self)
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
            self.pixmaps = [QPixmap('cr_1_1.jpg'), QPixmap('cr_1_2.jpg'),
                            QPixmap('cr_1_3.jpg'), QPixmap('cr_1_4.jpg')]
        if self.esse_2_btn.isChecked():
            self.pixmaps = [QPixmap('cr_2_1.jpg'), QPixmap('cr_2_2.jpg'),
                            QPixmap('cr_2_3.jpg'), QPixmap('cr_2_4.jpg')]
        if self.esse_3_btn.isChecked():
            self.pixmaps = [QPixmap('cr_3_1.jpeg'), QPixmap('cr_3_2.jpeg'),
                            QPixmap('cr_3_3.jpeg'), QPixmap('cr_3_4.jpeg')]
        self.label.setPixmap(self.pixmaps[0])
        self.label.resize(500, 500)
        for i in range(4):
            self.change_btns[i].show()

    def change_criteries(self):
        self.label.setPixmap(self.pixmaps[int(self.sender().text()) - 1])


class Plagiat_Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('plagiat_window.ui', self)
        self.setWindowTitle('PlagiatWindow')
        self.text1, self.text2 = set(), set()
        self.same_str_list.hide()
        self.first_btn.clicked.connect(self.get_first_f)
        self.second_btn.clicked.connect(self.get_second_f)
        self.compare_btn.clicked.connect(self.compare)
        self.checkBox.clicked.connect(self.show_same_str)

    def get_first_f(self):
        fname_1 = QFileDialog.getOpenFileName(
            self, 'Выбрать текст', '',
            '(*.txt)')[0]
        self.text1 = set(open(fname_1).readlines())
        self.text1 = set(filter(lambda x: x not in string.whitespace, self.text1))

    def get_second_f(self):
        fname_2 = QFileDialog.getOpenFileName(
            self, 'Выбрать текст', '',
            '(*.txt)')[0]
        self.text2 = set(open(fname_2).readlines())
        self.text2 = set(filter(lambda x: x not in string.whitespace, self.text2))

    def compare(self):
        try:
            if not self.text1 or not self.text2:
                raise NoFileError
            res = round(len(self.text1 & self.text2) / len(self.text1 | self.text2) * 100, 2)
            self.label_2.setText(f"{res}%")
            self.label.setText(f"Плагиат на")
        except NoFileError:
            self.label.setText('Вы не выбрали файлы.')
            self.label_2.setText('')

    def show_same_str(self):
        if self.checkBox.isChecked():
            self.same_str_list.show()
            self.same_str_list.addItems(sorted(list(self.text1 & self.text2), reverse=True))
        else:
            self.same_str_list.hide()
            self.same_str_list.clear()


class Format_Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('format_window.ui', self)
        self.setWindowTitle('FormatWindow')
        self.text_btn.clicked.connect(self.get_f)

    def get_f(self):
        fname = QFileDialog.getOpenFileName(
            self, 'Выбрать текст', '',
            '(*.txt)')[0]
        self.text = open(fname).readlines()
        self.num_paragraphs()
        self.num_words()
        self.check_cliche()
        self.coorect_words()

    def check_cliche(self):
        b_d = sqlite3.connect("clishe_base")
        cur = b_d.cursor()
        clishes = cur.execute("""SELECT name FROM clishe""").fetchall()
        for lines in self.text:
            for clishe in clishes:
                if clishe[0] in lines.lower():
                    self.tableWidget.setItem(1, -1, QTableWidgetItem('есть'))
                    b_d.close()
                    return
        self.tableWidget.setItem(1, -1, QTableWidgetItem('нет'))
        b_d.close()

    def num_paragraphs(self):
        n = len(list(filter(lambda x: x.startswith('\t'), self.text)))
        if n == 0:
            n = len(list(filter(lambda x: x == '\n', self.text))) + 1
        self.tableWidget.setItem(1, 2, QTableWidgetItem(str(n)))

    def coorect_words(self):
        spell = SpellChecker(language='ru')
        table = str.maketrans("", "", string.punctuation + '–«»')
        n = 0
        for lines in self.text:
            line = lines.translate(table)
            n += len(spell.unknown(filter(lambda x: len(x) >= 3, line.split())))
        self.tableWidget.setItem(1, 1, QTableWidgetItem(str(n)))
        if n:
            self.tableWidget.setItem(1, 0, QTableWidgetItem('есть'))
        else:
            self.tableWidget.setItem(1, 0, QTableWidgetItem('нет'))

    def num_words(self):
        n = sum(map(lambda x: len(x.split()), self.text))
        self.tableWidget.setItem(1, 3, QTableWidgetItem(str(n)))


class Marks_Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('marks_window.ui', self)
        self.setWindowTitle('MarksWindow')
        self.is_add = True
        self.edits = [self.understand_meaning_point_spin, self.argument_point_spin, self.subsequence_point_spin,
                      self.composition_point_spin, self.grammer_point_spin]
        self.labels = [self.label_2, self.label_3, self.label_4, self.label_5, self.label_6]
        for i in range(5):
            self.edits[i].hide()
            self.labels[i].hide()
        self.statusBar = QStatusBar(self)
        self.statusBar.move(40, 500)
        self.statusBar.resize(500, 20)
        self.add_btn.clicked.connect(self.show_edits)
        self.delete_btn.clicked.connect(self.delete)
        self.change_btn.clicked.connect(self.show_edits)
        self.ok_btn.hide()
        self.ok_btn.clicked.connect(self.save)

    def show_edits(self):
        try:
            self.name = self.name_edit.text()
            if not self.name:
                raise NoNameError
            for i in range(5):
                self.edits[i].show()
                self.labels[i].show()
            self.ok_btn.show()
            if self.sender().text() != 'Добавить':
                self.is_add = False
                self.show_change_edits()
            else:
                self.is_add = True
        except NoNameError:
            self.statusBar.showMessage("Вы не ввели имя!")

    def hide_edits(self):
        for i in range(5):
            self.edits[i].hide()
            self.labels[i].hide()
        self.ok_btn.hide()
        self.name_edit.setText('')

    def save(self):
        if self.is_add:
            self.add()
        else:
            self.change()

    def add(self):
        understand_meaning_point = self.understand_meaning_point_spin.value()
        argument_point = self.argument_point_spin.value()
        subsequence_point = self.subsequence_point_spin.value()
        composition_point = self.composition_point_spin.value()
        grammer_point = self.grammer_point_spin.value()
        main_mark = sum([understand_meaning_point, argument_point, subsequence_point,
                         composition_point, grammer_point])
        b_d = sqlite3.connect("students_rus_esse_base")
        cur = b_d.cursor()
        cur.execute("""INSERT INTO students_marks(name, understand_meaning_point, argument_point, 
                                                subsequence_point, composition_point, grammer_point, main_mark) 
                        VALUES(?, ?, ?, ?, ?, ?, ?)""",
                    (self.name, understand_meaning_point, argument_point, subsequence_point,
                     composition_point, grammer_point, main_mark))
        b_d.commit()
        b_d.close()
        self.statusBar.showMessage("Успешно!")
        self.hide_edits()

    def delete(self):
        try:
            name = self.name_edit.text()
            if not name:
                raise NoNameError
            b_d = sqlite3.connect("students_rus_esse_base")
            cur = b_d.cursor()
            cur.execute("""DELETE from students_marks
                            where name = ?""", (name, ))
            b_d.commit()
            b_d.close()
            self.statusBar.showMessage("Успешно!")
            self.name_edit.setText('')
        except NoNameError:
            self.statusBar.showMessage("Вы не ввели имя!")

    def show_change_edits(self):
        try:
            b_d = sqlite3.connect("students_rus_esse_base")
            cur = b_d.cursor()
            res = cur.execute("""SELECT understand_meaning_point, argument_point, 
                                subsequence_point, composition_point, grammer_point from students_marks
                                        where name = ?""", (self.name,)).fetchall()
            b_d.close()
            if not res:
                raise NoNameInBaseError
            for i in range(5):
                self.edits[i].setValue(res[0][i])
        except NoNameInBaseError:
            self.statusBar.showMessage("Такого ученика нет базе данных.")
            self.hide_edits()

    def change(self):
        understand_meaning_point = self.understand_meaning_point_spin.value()
        argument_point = self.argument_point_spin.value()
        subsequence_point = self.subsequence_point_spin.value()
        composition_point = self.composition_point_spin.value()
        grammer_point = self.grammer_point_spin.value()
        main_mark = sum([understand_meaning_point, argument_point, subsequence_point,
                         composition_point, grammer_point])
        b_d = sqlite3.connect("students_rus_esse_base")
        cur = b_d.cursor()
        cur.execute("""UPDATE students_marks
                        SET understand_meaning_point = ?
                        WHERE name = ?""", (understand_meaning_point, self.name, ))
        cur.execute("""UPDATE students_marks
                                SET argument_point = ?
                                WHERE name = ?""", (argument_point, self.name,))
        cur.execute("""UPDATE students_marks
                                SET subsequence_point = ?
                                WHERE name = ?""", (subsequence_point, self.name,))
        cur.execute("""UPDATE students_marks
                                SET composition_point = ?
                                WHERE name = ?""", (composition_point, self.name,))
        cur.execute("""UPDATE students_marks
                                SET grammer_point = ?
                                WHERE name = ?""", (grammer_point, self.name,))
        cur.execute("""UPDATE students_marks
                                SET main_mark = ?
                                WHERE name = ?""", (main_mark, self.name,))
        b_d.commit()
        b_d.close()
        self.statusBar.showMessage("Успешно!")
        self.hide_edits()


class Main_Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main_window.ui', self)
        self.managment_btn.clicked.connect(self.show_window_themes)
        self.plagiat_btn.clicked.connect(self.show_window_plagiat)
        self.format_btn.clicked.connect(self.show_window_format)
        self.marks_btn.clicked.connect(self.show_window_marks)
        self.inform_btn.clicked.connect(self.show_inform)
        self.inform_edit.hide()

    def show_window_themes(self):
        self.w = Criteries_Widget()
        self.w.show()

    def show_window_plagiat(self):
        self.w = Plagiat_Widget()
        self.w.show()

    def show_window_format(self):
        self.w = Format_Widget()
        self.w.show()

    def show_window_marks(self):
        self.w = Marks_Widget()
        self.w.show()

    def show_inform(self):
        if self.inform_edit.isHidden():
            self.inform_edit.show()
        else:
            self.inform_edit.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main_Widget()
    ex.show()
    sys.exit(app.exec_())
