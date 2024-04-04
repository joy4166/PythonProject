import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sqlite3
from grouping_2 import Grouping

class Assign(QMainWindow):
        def __init__(self):
            super().__init__()
            self.init_ui()

        def init_ui(self):
            # Layout
            self.entire_hbox = QHBoxLayout()
            self.player_grid = QGridLayout()
            self.player_vbox = QVBoxLayout()
            self.table_vbox = QVBoxLayout()

            # Player
            self.name_lb = QLabel("이름")
            self.height_lb = QLabel("키")
            self.position_lb = QLabel("포지션")
            self.name_le = QLineEdit()
            self.height_sp = QSpinBox()
            self.position_cb = QComboBox()
            self.btn_apply = QPushButton("추가")

            self.height_sp.setMaximum(230)
            self.height_sp.setValue(170)
            self.position_cb.addItems(["포인트 가드", "슈팅 가드", "스몰 포워드", "파워 포워드", "센터"])

            self.btn_apply.clicked.connect(self.on_btn_apply_clicked)

            # List
            self.table = QTableWidget()
            self.btn_delete = QPushButton("삭제")

            self.btn_delete.clicked.connect(self.on_btn_delete_clicked)
            self.table.setColumnCount(3)
            self.table.setHorizontalHeaderLabels(["이름", "키", "포지션"])

            # CSS
            style_sheet = '''
                   QPushButton {
                       color: white;
                       background-color: qlineargradient(spread:reflect, x1:0.5, y1:0.5, x2:1, y2:0.5, stop:0 rgba(255, 199, 0, 255), stop:1 rgba(192, 5, 67, 255));
                       border-radius: 20px;
                       padding: 10px;
                   }


                   QPushButton:hover {
                       background-color: qlineargradient(spread:reflect, x1:0.5, y1:0.5, x2:1, y2:0.5, stop:0 rgba(255, 170, 0, 255), stop:1 rgba(166, 3, 58, 255));
                   }


                   QPushButton:pressed {
                       background-color: qlineargradient(spread:reflect, x1:0.5, y1:0.5, x2:1, y2:0.5, stop:0 rgba(192, 5, 67, 255), stop:1 rgba(122, 2, 43, 255));
                   }
               '''
            self.btn_apply.setStyleSheet(style_sheet)
            self.btn_delete.setStyleSheet(style_sheet)

            self.init_widget()

        def init_widget(self):
            self.con = self.connection()

            self.set_table()
            self.set_layout()

            widget = QWidget()
            widget.setLayout(self.entire_hbox)
            self.setCentralWidget(widget)
            self.setGeometry(700, 400, 1400, 700)
            self.setWindowTitle("Player Assign")
            self.setWindowIcon(QIcon("Maicon.ico"))
            self.statusBar().showMessage("Developed by Cactus")

        def on_btn_apply_clicked(self):
            names = self.get_player_name(self.con)
            con = self.con
            n = self.name_le.text()
            h = self.height_sp.value()
            p = self.position_cb.currentText()
            if self.name_le.text() in names:
                self.update_player(con, n, h, p)
            else:
                self.insert_player(con, n, h, p)
            self.set_table()
            self.name_le.clear()
            self.height_sp.setValue(170)

        def on_btn_delete_clicked(self):
            try:
                name = self.table.item(self.table.currentRow(), 0).text()
                self.delete_player(self.con, name)
                self.table.removeRow(self.table.currentRow())
            except Exception as e:
                print("del_btn", e)

        def connection(self):
            try:
                con = sqlite3.connect("grouping.db")
                return con
            except Exception as e:
                print("con", e)

        def get_player(self, con):
            try:
                cur = con.cursor()
                sql = "SELECT * FROM player"
                cur.execute(sql)
                data = cur.fetchall()
                return data
            except Exception as e:
                print("get", e)

        def get_player_name(self, con):
            try:
                cur = con.cursor()
                sql = "SELECT name FROM player"
                cur.execute(sql)
                data = cur.fetchall()
                string_list = [str(x[0]) for x in data]
                return string_list
            except Exception as e:
                print("get name", e)

        def update_player(self, con, n, h, p):
            try:
                cur = con.cursor()
                sql = "UPDATE player set height = ?, position = ? WHERE name = ?"
                data = (h, p, n)
                cur.execute(sql, data)
            except Exception as e:
                print("update", e)
            finally:
                con.commit()

        def insert_player(self, con, n, h, p):
            try:
                cur = con.cursor()
                sql = "INSERT INTO player (name, height, position) VALUES (?, ?, ?)"
                data = (n, h, p)
                cur.execute(sql, data)
            except Exception as e:
                print("insert", e)
            finally:
                con.commit()

        def delete_player(self, con, n):
            try:
                cur = con.cursor()
                sql = "DELETE FROM player WHERE name = ?"
                cur.execute(sql, (n,))
            except Exception as e:
                print("del", e)
            finally:
                con.commit()

        def set_table(self):
            self.table.clearContents()
            self.table.setRowCount(0)
            data = self.get_player(self.con)
            print(data)
            print(self.table.rowCount())
            for i in data:
                self.table.insertRow(self.table.rowCount())
                self.table.setItem(self.table.rowCount()-1, 0, QTableWidgetItem(i[0]))
                self.table.setItem(self.table.rowCount()-1, 1, QTableWidgetItem(str(i[1])))
                self.table.setItem(self.table.rowCount()-1, 2, QTableWidgetItem(i[2]))

        def set_layout(self):
            self.player_grid.addWidget(self.name_lb, 0, 0)
            self.player_grid.addWidget(self.name_le, 0, 1)
            self.player_grid.addWidget(self.height_lb, 1, 0)
            self.player_grid.addWidget(self.height_sp, 1, 1)
            self.player_grid.addWidget(self.position_lb, 2, 0)
            self.player_grid.addWidget(self.position_cb, 2, 1)

            self.player_vbox.addLayout(self.player_grid)
            self.player_vbox.addWidget(self.btn_apply)

            self.table_vbox.addWidget(self.table)
            self.table_vbox.addWidget(self.btn_delete)

            self.entire_hbox.addLayout(self.player_vbox)
            self.entire_hbox.addLayout(self.table_vbox)

if __name__ == "__main__":
    app = QApplication([])
    fwindow = Assign()
    swindow = Grouping()
    fwindow.show()
    swindow.show()
    sys.exit(app.exec_())