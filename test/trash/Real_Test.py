import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import  *

class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            self.init_ui()

        def init_ui(self):
            self.vbox = QVBoxLayout()
            self.hbox = QHBoxLayout()

            self.button = QPushButton("Button")
            self.button.setStyleSheet('''
            QPushButton {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                stop:0 rgba(0,172,238,1),
                stop:1 rgba(2,126,251,1));
            width: 130px;
            height: 40px;
            line-height: 42px;
            padding: 0;
            border: none;
            }
            QPushButton::hover {
                background: transparent;
                box-shadow: none;
            }
            QPushButton::hover:before {
                height: 100%;
            }
            QPushButton::hover:after {
                width: 100%;
            }
            QPushButton::hover span {
                color: rgba(2,126,251,1);
            }
            QPushButton span:before,
            QPushButton span:after {
                position: absolute;
                content: "";
                left: 0;
                bottom: 0;
                background: rgba(2,126,251,1);
                transition: all 0.3s ease;
            }
            QPushButton span:before {
                width: 2px;
                height: 0%;
            }
            QPushButton span:after {
                width: 0%;
                height: 2px;
            }
            QPushButton span:hover:before {
                height: 100%;
            }
            QPushButton span:hover:after {
                width: 100%;
            }
            ''')

            self.init_widget()

        def init_widget(self):
            self.vbox.addWidget(self.button)

            widget = QWidget()
            widget.setLayout(self.vbox)
            self.setCentralWidget(widget)
            self.setGeometry(700, 400, 1400, 700)
            self.setWindowTitle("")
            self.statusBar().showMessage("Developed by Cactus")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())