import  sys
from PyQt5.QtWidgets import  QApplication,QWidget,QPushButton

class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.button = QPushButton('开始',self)
        self.button.pressed.connect(self.button.released)
        self.button.released.connect(self.change_text)

    def change_text(self):
        if self.button.text()=='开始':
            self.button.setText('终止')
        else:
            self.button.setText('开始')


if __name__=='__main__':
        app = QApplication(sys.argv)
        demo = Demo()
        demo.show()
        sys.exit(app.exec_())