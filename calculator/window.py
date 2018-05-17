import sys
import operator
from PyQt5 import QtCore, QtGui, QtWidgets
from calculator_front import Ui_MainWindow

READY = 0
INPUT = 1
app = QtWidgets.QApplication([])


class MainApplication(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super(MainApplication, self).__init__(*args, **kwargs)
        self.setupUi(self)

        for i in range(10):
            getattr(self, f'button{i}').pressed.connect(lambda v=i: self.input_number(v))

        self.button_plus.pressed.connect(lambda: self.operation(operator.add))
        self.button_minus.pressed.connect(lambda: self.operation(operator.sub))
        self.button_X.pressed.connect(lambda: self.operation(operator.mul))
        self.button_d.pressed.connect(lambda: self.operation(operator.truediv))
        self.button_pow.pressed.connect(lambda: self.operation(operator.pow))

        self.buttonAC.pressed.connect(self.reset)

        self.button_equal.pressed.connect(self.equals)

        self.reset()

        self.show()

    def input_number(self, v):
        if self.state == READY:
            self.state = INPUT
            self.stack[-1] = v
        else:
            self.stack[-1] = self.stack[-1] * 10 + v
        self.display()

    def display(self):
        self.lcd.display(self.stack[-1])

    def operation(self, op):
        if self.current_op:  # Complete the current operation
            self.equals()

        self.stack.append(0)
        self.state = INPUT
        self.current_op = op

    def reset(self):
        self.state = READY
        self.stack = [0]
        self.last_operation = None
        self.current_op = None
        self.display()

    def equals(self):
        if self.state == READY and self.last_operation:
            s, self.current_op = self.last_operation
            self.stack.append(s)

        if self.current_op:
            self.last_operation = self.stack[-1], self.current_op

            self.stack = [self.current_op(*self.stack)]
            self.current_op = None
            self.state = READY
            self.display()


window = MainApplication()
window.show()

sys.exit(app.exec_())

