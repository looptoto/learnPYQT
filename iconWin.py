# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip,QPushButton
from PyQt5.QtGui import QIcon,QFont


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()  # 界面绘制交给InitUi方法

    def initUI(self):
        # 设置窗口的位置和大小
        self.setGeometry(300, 300, 300, 220)
        # 设置窗口的标题
        self.setWindowTitle('Icon')
        # 设置窗口的图标，引用当前目录下的web.png图片
        self.setWindowIcon(QIcon('looptoto.png'))
        QToolTip.setFont(QFont("宋体", 10))
        self.setToolTip('zai bianji zhong')

        btn = QPushButton('Button', self)
        # btn.set
        btn.setToolTip("这是<b>按钮</b>件 do it")

        btn.resize(btn.sizeHint())
        btn.move(50,50)
        self.setGeometry(300,300,300,200)
        self.setWindowTitle("工具提示")
        # 显示窗口
        self.show()


if __name__ == '__main__':
    # 创建应用程序和对象
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())