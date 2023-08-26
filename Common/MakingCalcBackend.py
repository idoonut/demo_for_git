from PyQt5 import QtWidgets
from PyQt5.uic import loadUi

class Making(QtWidgets.QDialog):
    def __init__(self):
        super(Making, self).__init__()
        loadUi("Common\MakingCalc.ui", self)
        self.Mntwt.valueChanged.connect(lambda: self.Calc())
        self.Mamount.valueChanged.connect(lambda: self.Calc())
        self.Mrate.valueChanged.connect(lambda: self.Calc())
        self.EBill.stateChanged.connect(lambda: self.Calc())
        self.show()

    def Calc(self):
        if self.Mamount.value()!=0 and self.Mntwt.value()!=0.0 and self.Mrate.value()!=0:
            if self.Mntwt.value()>=1.0:
                if self.EBill.isChecked()!=True:
                    Making=((self.Mamount.value()/1.03)/self.Mntwt.value())-self.Mrate.value()
                else:
                    Making=((self.Mamount.value())/self.Mntwt.value())-self.Mrate.value()
            else:
                if self.EBill.isChecked()!=True:
                    Making=((self.Mamount.value()/1.03)-(self.Mntwt.value()*self.Mrate.value()))
                else:
                    Making=((self.Mamount.value())-(self.Mntwt.value()*self.Mrate.value()))
            print(Making)
            self.Result.setText(f"Making: {Making}")

if __name__=='__main__':
    import sys
    app=QtWidgets.QApplication(sys.argv)
    dialog=Making()
    sys.exit(app.exec_())