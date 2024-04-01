import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import Qt


class checkboxItem(QTableWidgetItem):
    def __init__(self):
        super().__init__()

    # 정렬시 발생 이벤트
    def __lt__(self, other):
        if self.checkState() == other.checkState() or self.checkState() == Qt.Checked:
            return False
        return True


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["col1", "col2"])
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        for idx in range(3):
            # 체크박스 넣는 부분
            item = checkboxItem()
            item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            item.setCheckState(QtCore.Qt.Checked)
            item.setData(Qt.UserRole, item.checkState())

            self.tableWidget.setItem(idx, 0, item)
            self.tableWidget.setItem(idx, 1, QTableWidgetItem(str(idx)))

        # 체크박스 클릭이벤트 추가
        self.tableWidget.cellChanged.connect(self.onCellChanged)
        # 셀 정렬기능 해제
        self.tableWidget.setSortingEnabled(False)

        header = self.tableWidget.horizontalHeader()
        # 헤더 클릭시 정렬이벤트 추가
        header.sectionClicked.connect(self.headerSorting)

        layout.addWidget(self.tableWidget)

        self.setLayout(layout)
        self.setWindowTitle('MyApp')
        self.resize(300, 300)
        self.show()

    # 헤더 클릭시 정렬이벤트
    def headerSorting(self):
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setSortingEnabled(False)

    # 체크박스 클릭 이벤트
    def onCellChanged(self, row, column):
        item = self.tableWidget.item(row, column)
        lastState = item.data(Qt.UserRole)
        currentState = item.checkState()
        if currentState != lastState:
            if currentState == QtCore.Qt.Checked:
                print("체크됨")
            else:
                print("체크 해제")
            item.setData(Qt.UserRole, currentState)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())