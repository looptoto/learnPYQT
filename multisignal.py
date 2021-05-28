import sys
from PyQt5.QtWidgets import  QApplication,QWidget,QPushButton

class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(300,300)
        self.setWindowTitle("多任务")
        self.button = QPushButton('开始',self)
        self.cnt=0
        self.button.clicked.connect(self.change_text)
        self.button.clicked.connect(self.change_window_title)
        self.button.clicked.connect(self.change_window_size)


    def change_text(self):
        print('改变 文本')
        self.button.setText('终止')
        self.button.clicked.disconnect(self.change_text)

    def change_window_size(self):
        print('改变 窗体大小')
        self.resize(500,500)
        self.button.clicked.disconnect(self.change_window_size)

    def change_window_title(self):
        print('改变标题')
        self.cnt=self.cnt+1
        tit = "改变标题-"+str(self.cnt)
        self.setWindowTitle(tit)
        self.button.clicked.disconnect(self.change_window_title)


if __name__ =='__main__':
    app =QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())