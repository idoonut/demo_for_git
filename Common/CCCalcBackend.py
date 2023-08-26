from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from Common.Backend import Get_Billsday, Get_opn
from datetime import date

class CCCalc(QtWidgets.QDialog):
    def __init__(self):
        super(CCCalc, self).__init__()
        loadUi("Common\CCCalc.ui", self)
        self.Cashinhand.valueChanged.connect(lambda: self.DiffCalc())
        self.Dateentry.setInputMask("99-99-9999")
        self.Dateentry.setText(date.today().strftime("%d-%m-%Y"))
        self.Dateentry.textChanged.connect(lambda: self.CashCalc())
        self.total=0
        self.CashCalc()
        self.show()

    def CashCalc(self):
        from datetime import datetime
        dte=datetime.strptime(self.Dateentry.text(), "%d-%m-%Y")
        db=Get_Billsday(datetime.strftime(dte, "%Y-%m-%d"))
        temp_total= Get_opn(datetime.strftime(dte, "%Y-%m-%d"))
        for i in db:
            if i[10]=='Gold Sale':
                temp_total+=i[11]
            elif i[10]=='Silver Sale':
                temp_total+=i[11]
            elif i[10]=='Old Order':
                temp_total+=i[11]
            elif i[10]=='New Order':
                temp_total+=i[11]
            elif i[10]=='VC':
                temp_total+=i[11]
            elif i[10]=='Misc plus':
                temp_total+=i[11]
            elif i[10]=='Silver Purchase':
                temp_total-=i[11]
            elif i[10]=='Misc minus':
                temp_total-=i[11]
            elif i[10]=='Expense':
                temp_total-=i[11]
            elif i[10]=='Gold Purchase':
                temp_total-=i[11]
            if i[13]>0:
                temp_total-=i[13]
            if i[15]>0:
                temp_total-=i[15]
            if i[17]>0:
                temp_total-=i[17]
            if i[19]>0:
                temp_total-=i[19]
        self.total=temp_total
        self.ExpCash.setText(f"Expected Cash:      {self.total}")

    def DiffCalc(self):
        val=self.Cashinhand.value()-self.total
        self.Diff.setText(f"Difference:            {val}")