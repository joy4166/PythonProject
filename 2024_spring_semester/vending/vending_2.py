import sys
import sqlite3
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import  *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Layout
        self.vbox = QVBoxLayout()
        self.hbox = QHBoxLayout()

        self.drink_grid_list = []
        for i in range(10):
            self.drink_grid_list.append(QGridLayout())

        self.entire_grid = QGridLayout()

        self.groupbox_list = []
        for i in range(10):
            self.groupbox_list.append(QGroupBox())

        for i in range(10):
            self.groupbox_list[i].setLayout(self.drink_grid_list[i])

        # Title
        self.title_lb = QLabel("음료수 자판기 프로그램")
        self.title_lb.setAlignment(Qt.AlignCenter)
        font1 = self.title_lb.font()
        font1.setPointSize(50)
        font1.setFamily('궁서')
        self.title_lb.setFont(font1)

        # Main Area
        self.drink_name_lb_list = []
        self.drink_price_lb_list = []
        self.drink_left_lb_list = []
        self.drink_buy_lb_list = []

        for i in range(10):
            self.drink_name_lb_list.append(QLabel("음료이름"))
            self.drink_price_lb_list.append(QLabel("음료가격"))
            self.drink_left_lb_list.append(QLabel("남은수량"))
            self.drink_buy_lb_list.append(QLabel("구입수량"))

        self.drink_name_le_list = []
        self.drink_price_le_list = []
        self.drink_left_sp_list = []
        self.drink_buy_sp_list = []

        for i in range(10):
            self.drink_name_le_list.append(QLineEdit())
            self.drink_price_le_list.append(QLineEdit())
            self.drink_left_sp_list.append(QSpinBox())
            self.drink_buy_sp_list.append(QSpinBox())

        # Extra
        self.exit_btn = QPushButton("종료")
        self.get_money_lb = QLabel("투입금액(원)")
        self.change_lb = QLabel("거스름돈(원)")
        self.get_money_le = QLineEdit()
        self.change_lb2 = QLabel()
        self.pay_btn = QPushButton("결재")
        self.pay_cancel_btn = QPushButton("결재취소")

        self.get_money_lb.setAlignment(Qt.AlignRight)
        self.change_lb.setAlignment(Qt.AlignRight)

        self.init_widget()

    def init_widget(self):
        self.spinbox_set()

        # Layout
        self.set_grid_layout()
        self.set_layout()

        #db
        self.con = self.connection()
        self.set_menu(self.con)
        self.buy_limit()

        # Button connect
        self.pay_btn.clicked.connect(self.on_pay_btn_clicked)
        self.exit_btn.clicked.connect(self.on_exit_btn_clicked)
        self.pay_cancel_btn.clicked.connect(self.on_cancel_btn_clicked)

        widget = QWidget()
        widget.setLayout(self.entire_grid)
        self.setCentralWidget(widget)
        self.setGeometry(400,350,1800,400)
        self.setWindowTitle("Vending Machine")
        self.statusBar().showMessage("Developed by Cactus")

    def connection(self):
        try:
            con = sqlite3.connect("vending2.db")
            return con
        except Exception as e:
            print(e)

    def spinbox_set(self):
        for i in range(10):
            self.drink_left_sp_list[i].setMinimum(0)
            self.drink_buy_sp_list[i].setMinimum(0)

    def set_grid_layout(self):
        for i in range(10):
            self.drink_grid_list[i].addWidget(self.drink_name_lb_list[i], 0, 0)
            self.drink_grid_list[i].addWidget(self.drink_name_le_list[i], 0, 1)
            self.drink_grid_list[i].addWidget(self.drink_price_lb_list[i], 1, 0)
            self.drink_grid_list[i].addWidget(self.drink_price_le_list[i], 1, 1)
            self.drink_grid_list[i].addWidget(self.drink_left_lb_list[i], 2, 0)
            self.drink_grid_list[i].addWidget(self.drink_left_sp_list[i], 2, 1)
            self.drink_grid_list[i].addWidget(self.drink_buy_lb_list[i], 3, 0)
            self.drink_grid_list[i].addWidget(self.drink_buy_sp_list[i], 3, 1)

    def set_layout(self):
        self.entire_grid.addWidget(self.title_lb, 0, 0, 1, 4)
        self.entire_grid.addWidget(self.exit_btn, 0, 4)
        for i in range(10):
            row = 1 + i//5
            col = i % 5
            self.entire_grid.addWidget(self.groupbox_list[i], row, col)
        self.entire_grid.addWidget(self.get_money_lb, 3, 2)
        self.entire_grid.addWidget(self.get_money_le, 3, 3)
        self.entire_grid.addWidget(self.pay_btn, 3, 4)
        self.entire_grid.addWidget(self.change_lb, 4, 2)
        self.entire_grid.addWidget(self.change_lb2, 4, 3)
        self.entire_grid.addWidget(self.pay_cancel_btn, 4, 4)

    def set_menu(self, con):
        data = self.take_data(con)

        for i in range(10):
            self.drink_name_le_list[i].setText(data[i][1])
            self.drink_price_le_list[i].setText(str(data[i][2]))
            self.drink_left_sp_list[i].setValue(data[i][3])

    def buy_limit(self):
        for i in range(10):
            self.drink_buy_sp_list[i].setMaximum(self.drink_left_sp_list[i].value())

    def on_pay_btn_clicked(self):
        try:
            reply = QMessageBox.question(self, "구매 확인", "구매하시겠습니까?",
                                         QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                if int(self.get_money_le.text()) >= self.total_money():
                    con = self.con
                    change = int(self.get_money_le.text()) - self.total_money()
                    self.current_money = self.get_money_le.text()
                    for i in range(10):
                        id = i+1
                        name = self.drink_name_le_list[i].text()
                        price = self.drink_price_le_list[i].text()
                        left = self.drink_left_sp_list[i].value()
                        self.backup_data(con, id, name, price, left)
                    self.count_down()
                    self.buy_limit()
                    self.change_lb2.setText(str(change))
                    self.get_money_le.clear()
                    for i in range(10):
                        id = i+1
                        name = self.drink_name_le_list[i].text()
                        price = self.drink_price_le_list[i].text()
                        left = self.drink_left_sp_list[i].value()
                        self.save_data(con, id, name, price, left)
                else:
                    self.change_lb2.setText("금액부족")
                    return

        except Exception as e:
            print(e)
            self.change_lb2.setText("Error")

    def on_exit_btn_clicked(self):
        con = self.con
        for i in range(10):
            id = i + 1
            name = self.drink_name_le_list[i].text()
            price = self.drink_price_le_list[i].text()
            left = self.drink_left_sp_list[i].value()
            self.save_data(con, id, name, price, left)
        sys.exit()

    def on_cancel_btn_clicked(self):
        try:
            data = self.take_backup(self.con)
        # print(data)

            for i in range(10):
                self.drink_name_le_list[i].setText(data[i][1])
                self.drink_price_le_list[i].setText(str(data[i][2]))
                self.drink_left_sp_list[i].setValue(data[i][3])

            self.buy_limit()
            self.get_money_le.setText(self.current_money)
            self.change_lb2.setText("퉷")
        except Exception as e:
            print("e")
            self.change_lb2.setText("error")

    def total_money(self):
        total = 0
        for i in range(10):
            total += int(self.drink_price_le_list[i].text()) * self.drink_buy_sp_list[i].value()
        return total

    def count_down(self):
        for i in range(10):
            self.drink_left_sp_list[i].setValue(self.drink_left_sp_list[i].value() - self.drink_buy_sp_list[i].value())
            self.drink_buy_sp_list[i].setValue(0)

    def take_data(self, con):
        try:
            cur = con.cursor()
            sql = "SELECT * FROM drink"
            cur.execute(sql)
            data = cur.fetchall()
            return data

        except Exception as e:
            print(e)

    def save_data(self, con, id, name, price, left):
        try:
            cur = con.cursor()
            sql = "UPDATE drink SET name = ?, price = ?, left = ? WHERE id = ?"
            data = (name, price, left, id)
            cur.execute(sql, data)
        except Exception as e:
            print(e)
        finally:
            con.commit()

    def backup_data(self, con, id, name, price, left):
        try:
            cur = con.cursor()
            sql = "UPDATE backup SET name = ?, price = ?, left = ? WHERE id = ?"
            data = (name, price, left, id)
            cur.execute(sql, data)
        except Exception as e:
            print(e)
        finally:
            con.commit()

    def take_backup(self, con):
        try:
            cur = con.cursor()
            sql = "SELECT * FROM backup"
            cur.execute(sql)
            data = cur.fetchall()
            return data
        except Exception as e:
            print('error', e)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())