import sys
from PyQt5.QtWidgets import QApplication,QDialog
from ui_dialog2_3 import Ui_Dialog

class QmyDialog(QDialog):
    def __init__(self, parent=None):
        super(QmyDialog, self).__init__(parent)
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)

    def  on_pushButton_clear_clicked(self):
        self.ui.plainTextEdit.clear()

    def on_checkBox_Bold_toggled(self, checked):
        font = self.ui.plainTextEdit.font()
        font.setBold(checked)
        self.ui.plainTextEdit.setFont(font)


if __name__=="__main__":
        app = QApplication(sys.argv)
        form = QmyDialog()
        form.show()
        sys.exit(app.exec_())