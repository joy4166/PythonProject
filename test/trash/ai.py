import sys
from PyQt5.QtWidgets import  QApplication , QMainWindow,  QWidget, QVBoxLayout, QHBoxLayout, QLabel, QGridLayout, QPushButton

class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            self.init_ui()

        def init_ui(self):
            self.player = 1

            self.vbox = QVBoxLayout()
            self.grid_btn_layout = QGridLayout()

            self.btn_grid_1 = QPushButton("")
            self.btn_grid_2 = QPushButton("")
            self.btn_grid_3 = QPushButton("")
            self.btn_grid_4 = QPushButton("")
            self.btn_grid_5 = QPushButton("")
            self.btn_grid_6 = QPushButton("")
            self.btn_grid_7 = QPushButton("")
            self.btn_grid_8 = QPushButton("")
            self.btn_grid_9 = QPushButton("")
            self.btn_reset = QPushButton("Reset")

            self.btn_grid_1.clicked.connect(self.on_btn_grid_1_clicked)
            self.btn_grid_2.clicked.connect(self.on_btn_grid_2_clicked)
            self.btn_grid_3.clicked.connect(self.on_btn_grid_3_clicked)
            self.btn_grid_4.clicked.connect(self.on_btn_grid_4_clicked)
            self.btn_grid_5.clicked.connect(self.on_btn_grid_5_clicked)
            self.btn_grid_6.clicked.connect(self.on_btn_grid_6_clicked)
            self.btn_grid_7.clicked.connect(self.on_btn_grid_7_clicked)
            self.btn_grid_8.clicked.connect(self.on_btn_grid_8_clicked)
            self.btn_grid_9.clicked.connect(self.on_btn_grid_9_clicked)
            self.btn_reset.clicked.connect(self.on_btn_reset_clicked)


            self.grid_btn_layout.addWidget(self.btn_grid_1, 0, 0)
            self.grid_btn_layout.addWidget(self.btn_grid_2, 0, 1)
            self.grid_btn_layout.addWidget(self.btn_grid_3, 0, 2)
            self.grid_btn_layout.addWidget(self.btn_grid_4, 1, 0)
            self.grid_btn_layout.addWidget(self.btn_grid_5, 1, 1)
            self.grid_btn_layout.addWidget(self.btn_grid_6, 1, 2)
            self.grid_btn_layout.addWidget(self.btn_grid_7, 2, 0)
            self.grid_btn_layout.addWidget(self.btn_grid_8, 2, 1)
            self.grid_btn_layout.addWidget(self.btn_grid_9, 2, 2)

            self.vbox.addLayout(self.grid_btn_layout)
            self.vbox.addWidget(self.btn_reset)

            widget = QWidget()
            widget.setLayout(self.vbox)
            self.setCentralWidget(widget)
            self.setGeometry(700,400,500,300)
            self.setWindowTitle("Tic Tac Toe")
            self.statusBar().showMessage("Developed by Cactus")

        def on_btn_grid_1_clicked(self):
            if self.btn_grid_1.text() != "":
                pass
            else:
                if self.player == 1:
                    self.btn_grid_1.setText("O")
                    self.player = 2
                else:
                    self.btn_grid_1.setText("X")
                    self.player = 1

        def on_btn_grid_2_clicked(self):
            if self.btn_grid_2.text() != "":
                pass
            else:
                if self.player == 1:
                    self.btn_grid_2.setText("O")
                    self.player = 2
                else:
                    self.btn_grid_2.setText("X")
                    self.player = 1

        def on_btn_grid_3_clicked(self):
            if self.btn_grid_3.text() != "":
                pass
            else:
                if self.player == 1:
                    self.btn_grid_3.setText("O")
                    self.player = 2
                else:
                    self.btn_grid_3.setText("X")
                    self.player = 1

        def on_btn_grid_4_clicked(self):
            if self.btn_grid_4.text() != "":
                pass
            else:
                if self.player == 1:
                    self.btn_grid_4.setText("O")
                    self.player = 2
                else:
                    self.btn_grid_4.setText("X")
                    self.player = 1

        def on_btn_grid_5_clicked(self):
            if self.btn_grid_5.text() != "":
                pass
            else:
                if self.player == 1:
                    self.btn_grid_5.setText("O")
                    self.player = 2
                else:
                    self.btn_grid_5.setText("X")
                    self.player = 1

        def on_btn_grid_6_clicked(self):
            if self.btn_grid_6.text() != "":
                pass
            else:
                if self.player == 1:
                    self.btn_grid_6.setText("O")
                    self.player = 2
                else:
                    self.btn_grid_6.setText("X")
                    self.player = 1

        def on_btn_grid_7_clicked(self):
            if self.btn_grid_7.text() != "":
                pass
            else:
                if self.player == 1:
                    self.btn_grid_7.setText("O")
                    self.player = 2
                else:
                    self.btn_grid_7.setText("X")
                    self.player = 1

        def on_btn_grid_8_clicked(self):
            if self.btn_grid_8.text() != "":
                pass
            else:
                if self.player == 1:
                    self.btn_grid_8.setText("O")
                    self.player = 2
                else:
                    self.btn_grid_8.setText("X")
                    self.player = 1

        def on_btn_grid_9_clicked(self):
            if self.btn_grid_9.text() != "":
                pass
            else:
                if self.player == 1:
                    self.btn_grid_9.setText("O")
                    self.player = 2
                else:
                    self.btn_grid_9.setText("X")
                    self.player = 1

        def on_btn_reset_clicked(self):
            self.player = 1
            self.btn_grid_1.setText("")
            self.btn_grid_2.setText("")
            self.btn_grid_3.setText("")
            self.btn_grid_4.setText("")
            self.btn_grid_5.setText("")
            self.btn_grid_6.setText("")
            self.btn_grid_7.setText("")
            self.btn_grid_8.setText("")
            self.btn_grid_9.setText("")


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())