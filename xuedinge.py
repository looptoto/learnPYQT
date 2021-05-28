import sys
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication
from PyQt5.QtGui import QFont

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont("楷体", 10))
        self.setToolTip("跟<b>薛定谔的猫</b>学编程")
        btn = QPushButton("Button", self)
        btn.setToolTip("公众号<b>猫说编程</b>")
        # btn.sizeHint()显示默认尺寸
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle("黑猫编程")
        self.show()

if __name__ == "__main__":

    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())