from PyQt5 import QtWidgets
from Common.URDdialog import Ui_Dialog
from Common.Backend import Bill_store, Get_delBills, Get_specificbills, del_billnum, Get_Sale_store
from Common.Transaction import GoldSell, SilverSell, OldOrder, Bill, VC, NO, purchase
from Common.Frontendlogic import MainWindow


if __name__=='__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PyBookKeeper = QtWidgets.QMainWindow()
    ui = MainWindow()
    sys.exit(app.exec_())

