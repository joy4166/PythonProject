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

            self.init_widget()

        def init_widget(self):

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