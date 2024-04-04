import ftplib
import sys
import sqlite3
from PyQt5.QtCore import *
from PyQt5.QtWidgets import  *
from PyQt5 import QtCore


class Grouping(QMainWindow):
        def __init__(self):
            super().__init__()
            self.init_ui()

        def init_ui(self):
            self.entire_hbox = QHBoxLayout()
            self.table_vbox = QVBoxLayout()
            self.btn_hbox = QHBoxLayout()
            self.team_a_vbox = QVBoxLayout()
            self.team_b_vbox = QVBoxLayout()
            self.list_hbox = QHBoxLayout()

            self.table_widget = QTableWidget()
            self.table_widget.setColumnCount(4)
            self.table_widget.setHorizontalHeaderLabels(["Check","이름", "키", "포지션"])

            self.random_rd = QRadioButton("랜덤")
            self.random_rd.setChecked(True)
            self.height_rd = QRadioButton("키")
            self.position_rd = QRadioButton("포지션")
            self.grouping_btn = QPushButton("마법의 버튼")
            self.refresh_btn = QPushButton("새로고침")
            self.grouping_btn.clicked.connect(self.add_checked_players)
            self.refresh_btn.clicked.connect(self.refresh_table)

            self.lb_team_a = QLabel("Team A")
            self.lb_team_b = QLabel("Team B")
            self.list_team_a = QListWidget()
            self.list_team_b = QListWidget()

            self.init_widget()

        def init_widget(self):
            self.con = self.connection()

            self.set_layout()
            self.set_table()

            widget = QWidget()
            widget.setLayout(self.entire_hbox)
            self.setCentralWidget(widget)
            self.setGeometry(700, 400, 1800, 1000)
            self.setWindowTitle("Grouping Program")
            self.statusBar().showMessage("Developed by Cactus")

        def set_layout(self):
            self.btn_hbox.addWidget(self.random_rd)
            self.btn_hbox.addWidget(self.height_rd)
            self.btn_hbox.addWidget(self.position_rd)
            self.btn_hbox.addWidget(self.grouping_btn)
            self.btn_hbox.addWidget(self.refresh_btn)

            self.table_vbox.addWidget(self.table_widget)
            self.table_vbox.addLayout(self.btn_hbox)

            self.team_a_vbox.addWidget(self.lb_team_a)
            self.team_a_vbox.addWidget(self.list_team_a)
            self.team_b_vbox.addWidget(self.lb_team_b)
            self.team_b_vbox.addWidget(self.list_team_b)

            self.list_hbox.addLayout(self.team_a_vbox)
            self.list_hbox.addLayout(self.team_b_vbox)

            self.entire_hbox.addLayout(self.table_vbox)
            self.entire_hbox.addLayout(self.list_hbox)

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
            self.table_widget.clearContents()
            self.table_widget.setRowCount(0)
            data = self.get_player(self.con)
            print(data)
            print(self.table_widget.rowCount())
            for i in data:
                row_position = self.table_widget.rowCount()
                self.table_widget.insertRow(row_position)
                checkbox = QCheckBox()
                self.table_widget.setCellWidget(row_position, 0, checkbox)
                self.table_widget.setItem(row_position, 1, QTableWidgetItem(i[0]))
                self.table_widget.setItem(row_position, 2, QTableWidgetItem(str(i[1])))
                self.table_widget.setItem(row_position, 3, QTableWidgetItem(i[2]))

        def refresh_table(self):
            self.set_table()

        def add_checked_players(self):
            selected_players_team_a = []
            selected_players_team_b = []

            for row in range(self.table_widget.rowCount()):
                checkbox_item = self.table_widget.cellWidget(row, 0)
                if checkbox_item.isChecked():
                    name_item = self.table_widget.item(row, 1)
                    height_item = self.table_widget.item(row, 2)
                    position_item = self.table_widget.item(row, 3)
                    if name_item and height_item and position_item:
                        name = name_item.text()
                        height = height_item.text()
                        position = position_item.text()
                        player_info = f"{name}-{height}-{position}"
                        selected_players_team_a.append(player_info)
                        selected_players_team_b.append(player_info)
                    else:
                        print("Error, Row:", row)

            self.list_team_a.clear()
            self.list_team_b.clear()

            self.list_team_a.addItems(selected_players_team_a)
            self.list_team_b.addItems(selected_players_team_b)


if __name__ == "__main__":
    app = QApplication([])
    window = Grouping()
    window.show()
    sys.exit(app.exec_())