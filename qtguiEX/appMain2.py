# appMain2 .py 多继承
import  sys
from PyQt5.QtWidgets import QWidget, QApplication
from ui_FormHello import  Ui_FormHello
from PyQt5.QtGui import QIcon,QFont

class QmyWidget(QWidget,Ui_FormHello):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.Lab="多重继承Qmywidget"
        self.setupUi(self)
        self.LabHello.setText(self.Lab)
        self.setWindowIcon(QIcon("../looptoto.png"))
if __name__=="__main__":
    app = QApplication(sys.argv)
    mwf= QmyWidget()
    mwf.show()
    mwf.btnClose.setText("不 关 了")
    sys.exit(app.exec_())