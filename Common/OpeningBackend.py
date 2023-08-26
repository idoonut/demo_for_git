from msilib.schema import Dialog
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Common.Backend import Store_Opening

class Opening(QtWidgets.QDialog):
    def __init__(self):
        super(Opening, self).__init__()
        loadUi("Common\Opening.ui", self)
        self.Submit.clicked.connect(lambda: self.Submit_data())
        self.Cancel.clicked.connect(lambda: self.close())
        self.show()

    def Submit_data(self):
        if self.GoldRate.value()!=0 and self.SilverRate.value()!=0 and self.OpnCash.value()!=0:
            Store_Opening(self.GoldRate.value(), self.SilverRate.value(), self.OpnCash.value())
            Opnsub=QtWidgets.QMessageBox()
            Opnsub.setIcon(QMessageBox.Information)
            Opnsub.setWindowTitle("Data Entry Confirmation")
            Opnsub.setText("The Details have been entered")
            Opnsub.setStandardButtons(QMessageBox.Ok)
            retval=Opnsub.exec_()
            self.close()
        else:
            OpnWarn=QtWidgets.QMessageBox()
            OpnWarn.setIcon(QMessageBox.Warning)
            OpnWarn.setWindowTitle("Invalid Entry")
            OpnWarn.setText("Please retry your details")
            OpnWarn.setStandardButtons(QMessageBox.Ok)
            retval=OpnWarn.exec_()

if __name__=='__main__':
    import sys
    app=QtWidgets.QApplication(sys.argv)
    dialog=Opening()
    sys.exit(app.exec_())
