import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QLineEdit

from PyQt5.QtWidgets import QLabel

from PyQt5.QtWidgets import QPushButton

from PyQt5.QtWidgets import QVBoxLayout

from PyQt5.QtWidgets import QWidget
from functools import partial


class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('I MISS YOU')
        self.setFixedSize(250, 250)
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        self._createDisplay()
        self._createButtons()

    def _createDisplay(self):
        self.display = QLineEdit()
        self.display.setFixedHeight(35)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)

    def _createButtons(self):
        self.buttons = {}
        buttonsLayout = QGridLayout()
        buttons = {'7': (0, 0),
                   '8': (0, 1),
                   '9': (0, 2),
                   '/': (0, 3),
                   'C': (0, 4),
                   '4': (1, 0),
                   '5': (1, 1),
                   '6': (1, 2),
                   '*': (1, 3),
                   '(': (1, 4),
                   '1': (2, 0),
                   '2': (2, 1),
                   '3': (2, 2),
                   '+': (2, 3),
                   ')': (2, 4),
                   '.': (3, 0),
                   '0': (3, 1),
                   'del': (3, 2),
                   '-': (3 ,3),
                   '=': (3, 4)}
        for btn, pos in buttons.items():
            self.buttons[btn] = QPushButton(btn)
            self.buttons[btn].setFixedSize(40, 40)
            buttonsLayout.addWidget(self.buttons[btn], pos[0], pos[1])
            self.generalLayout.addLayout(buttonsLayout)

    def setDisplayText(self, text):
        self.display.setText(text)
        self.display.setFocus()

    def displayText(self):
        return self.display.text()

    def clearDisplay(self):
        self.setDisplayText('')

    def delDisplay(self):
        self.setDisplayText(self.display.text()[0:self.display.text().__len__()-1])


class IMISSYOUCtrl:
    def __init__(self, model, view):
        self._evaluate = model
        self._view = view
        self._connectSignals()

    def _calculateResult(self):
        result = self._evaluate(expression=self._view.displayText())
        self._view.setDisplayText(result)

    def _buildExpression(self, sub_exp):
        if self._view.displayText() == ERROR_MSG:
            self._view.clearDisplay()

        expression = self._view.displayText() + sub_exp
        self._view.setDisplayText(expression)

    def _connectSignals(self):
        for btnText, btn in self._view.buttons.items():
            if btnText not in {'=','C','del'}:
                btn.clicked.connect(partial(self._buildExpression, btnText))

        self._view.buttons['='].clicked.connect(self._calculateResult)
        self._view.display.returnPressed.connect(self._calculateResult)
        self._view.buttons['C'].clicked.connect(self._view.clearDisplay)
        self._view.buttons['del'].clicked.connect(self._view.delDisplay)


ERROR_MSG = 'ERROR'


def evaluateExpression(expression):
    try:
        result = str(eval(expression, {}, {}))
    except Exception:
        result = ERROR_MSG

    return result


def main():
    IMISSYOU = QApplication(sys.argv)
    view = UI()
    view.show()
    model = evaluateExpression
    IMISSYOUCtrl(model=model, view=view)
    sys.exit(IMISSYOU.exec_())


if __name__ == '__main__':
    main()
