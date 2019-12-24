import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget, QLabel, QGridLayout, QPushButton, \
    QLineEdit
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('IMISSYOU')
layout = QGridLayout()

layout.addWidget(QPushButton('1'), 0, 0)
layout.addWidget(QPushButton('2'), 0, 1)
layout.addWidget(QPushButton('3'), 0, 2)
layout.addWidget(QPushButton('4'), 1, 0)
layout.addWidget(QPushButton('5'), 1, 1)
layout.addWidget(QPushButton('6'), 1, 2)
layout.addWidget(QPushButton('7'), 2, 0)
layout.addWidget(QPushButton('8'), 2, 1)
layout.addWidget(QPushButton('9'), 2, 2)
layout.addWidget(QPushButton('del'), 3, 0)
layout.addWidget(QPushButton('0'), 3, 1)
layout.addWidget(QPushButton('.'), 3, 2)
window.setLayout(layout)
window.show()

sys.exit(app.exec_())