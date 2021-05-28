import  sys
from PyQt5 import QtWidgets
import ui_FormHello

app = QtWidgets.QApplication(sys.argv)
baseWidget= QtWidgets.QWidget()

ui = ui_FormHello.Ui_FormHello()
ui.setupUi(baseWidget)

baseWidget.show()
#ui.LabHello.setText("热爱祖国 ~")
sys.exit(app.exec_())