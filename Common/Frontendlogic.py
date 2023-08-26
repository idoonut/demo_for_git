from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMessageBox
from Common.Backend import Bill_store, Get_delBills, Get_specificbills, del_billnum, Get_Sale_store, create_tables
from Common.Transaction import GoldSell, SilverSell, OldOrder, Bill, VC, NO, purchase
from datetime import date
from Common.URDdialog import Ui_Dialog
from Common.createdocx import gen_billtoday, gen_sum
from Common.OpeningBackend import Opening
from Common.CCCalcBackend import CCCalc
from Common.MakingCalcBackend import Making

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("Common\Frontend.ui", self)
        #Dialog Initialize
        self.dialog=QtWidgets.QDialog()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self.dialog)
        #closing cash show
        self.CCbutton.clicked.connect(lambda: self.ClosingCash())
        self.MCbutton.clicked.connect(lambda: self.MakingCalc())
        self.OpnButton.clicked.connect(lambda: self.Opning())
        #create tables for database
        create_tables()
        #Validator Initialize
        self.OnlyInt=QtGui.QIntValidator()
        self.TransactionConfirm.clicked.connect(lambda: self.Switch_Widgets())
        self.nextlist={}
        self.pagenum=0
        #Shortcut Set up
        self.labelCName.setBuddy(self.Gold_custname)
        self.labelCash.setBuddy(self.Cash)
        self.labelDebt.setBuddy(self.DebtAmount)
        self.labelCName_2.setBuddy(self.Silver_custname)
        self.labelCName_3.setBuddy(self.Old_OrderName)
        self.labelCName_4.setBuddy(self.New_Order_Name)
        self.labelCName_5.setBuddy(self.VC_name)
        self.labelCName_6.setBuddy(self.GP_Name)
        self.labelCName_7.setBuddy(self.SP_Name)
        self.labelCash_2.setBuddy(self.Cash_2)
        self.labelCash_3.setBuddy(self.Cash_3)
        self.labelCash_4.setBuddy(self.Cash_4)
        self.labelCash_5.setBuddy(self.Cash_5)
        self.labelDebt_2.setBuddy(self.DebtAmount_2)        
        self.labelDebt_3.setBuddy(self.DebtAmount_3)
        self.labelDebt_4.setBuddy(self.DebtAmount_4)
        self.labelDebt_5.setBuddy(self.DebtAmount_5)
        self.labelOther.setBuddy(self.OtherAmount)
        self.labelOther_2.setBuddy(self.OtherAmount_2)
        self.labelOther_3.setBuddy(self.OtherAmount_3)
        self.labelOther_4.setBuddy(self.OtherAmount_4)
        self.labelOther_5.setBuddy(self.OtherAmount_5)
        self.labelOther_6.setBuddy(self.OtherAmount_6)
        #Completer Initialize
        self.golditemnames=QtWidgets.QCompleter(["ERG","NCK","CHK","SMS","MS","PDT","BNG","GBR","LBR","LR","GR","CH","LKT","GB","BBR","BR","BCH","TIKA","FERWA"])
        self.Gold_itemname.setCompleter(self.golditemnames)
        self.Gold_itemname_2.setCompleter(self.golditemnames)
        self.Gold_itemname_3.setCompleter(self.golditemnames)
        self.Gold_itemname_4.setCompleter(self.golditemnames)
        self.Gold_itemname_5.setCompleter(self.golditemnames)
        self.GP_Itemname.setCompleter(self.golditemnames)
        self.GP_Itemname_2.setCompleter(self.golditemnames)
        self.GP_Itemname_3.setCompleter(self.golditemnames) 
        self.GP_Itemname_4.setCompleter(self.golditemnames) 
        self.GP_Itemname_5.setCompleter(self.golditemnames)
        self.silveritemnames=QtWidgets.QCompleter(["PAYAL","FERWA","THALI","BRACELET","RINGS"])
        self.Silver_itemname.setCompleter(self.silveritemnames)
        self.Silver_itemname_2.setCompleter(self.silveritemnames)
        self.Silver_itemname_3.setCompleter(self.silveritemnames)
        self.Silver_itemname_4.setCompleter(self.silveritemnames)
        self.Silver_itemname_5.setCompleter(self.silveritemnames)
        self.SP_Itemname.setCompleter(self.silveritemnames)
        self.SP_Itemname_2.setCompleter(self.silveritemnames)
        self.SP_Itemname_3.setCompleter(self.silveritemnames)
        self.SP_Itemname_4.setCompleter(self.silveritemnames)
        self.SP_Itemname_5.setCompleter(self.silveritemnames)
        OOcomp=QtWidgets.QCompleter(["ERG","NCK","CHK","SMS","MS","PDT","BNG","GBR","LBR","LR","GR","CH","LKT","GB","BBR","BR","BCH","TIKA","PAYAL","FERWA","THALI","BRACELET","RINGS"])
        self.Old_Order_Itemname.setCompleter(OOcomp)
        self.Old_Order_Itemname_2.setCompleter(OOcomp)
        self.Old_Order_Itemname_3.setCompleter(OOcomp)
        self.Old_Order_Itemname_4.setCompleter(OOcomp)
        self.Old_Order_Itemname_5.setCompleter(OOcomp)
        self.New_Order_Itemname.setCompleter(OOcomp)
        self.New_Order_Itemname_2.setCompleter(OOcomp)
        self.New_Order_Itemname_3.setCompleter(OOcomp)
        self.New_Order_Itemname_4.setCompleter(OOcomp)
        self.New_Order_Itemname_5.setCompleter(OOcomp)
        self.VC_Itemname.setCompleter(OOcomp)
        self.VC_Itemname_2.setCompleter(OOcomp)
        self.VC_Itemname_3.setCompleter(OOcomp)
        self.VC_Itemname_4.setCompleter(OOcomp)
        self.VC_Itemname_5.setCompleter(OOcomp)
        self.URDitemname.setCompleter(OOcomp)
        self.URDitemname_2.setCompleter(OOcomp)
        self.URDitemname_3.setCompleter(OOcomp)
        self.URDitemname_4.setCompleter(OOcomp)
        self.URDitemname_5.setCompleter(OOcomp)

        #Input Mask Set Up


        #Table Dimensions
        self.tableWidget.setColumnWidth(0, 150)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 200)
        self.tableWidget.setColumnWidth(3, 100)
        self.tableWidget.setColumnWidth(4, 150)
        #Next button triggers
        self.Next.clicked.connect(lambda: self.GoldNext())
        self.Next_2.clicked.connect(lambda: self.SilverNext())
        self.Old_Order_Next.clicked.connect(lambda: self.OONext())
        self.VCNext.clicked.connect(lambda: self.VC_Next())
        self.GP_next.clicked.connect(lambda: self.GP_Next())
        self.SP_next.clicked.connect(lambda: self.SP_Next())
        #Previous button triggers
        self.Previous.clicked.connect(lambda: self.GoldPrevious())
        self.Previous_2.clicked.connect(lambda: self.SilverPrevious())
        self.Old_Order_Previous.clicked.connect(lambda: self.OOPrevious())
        self.VCPrevious.clicked.connect(lambda: self.VC_Previous())
        self.GP_previous.clicked.connect(lambda: self.GP_Previous())
        self.SP_previous.clicked.connect(lambda: self.SP_Previous())
        #Data Entry button triggers
        self.DataEntry_button.clicked.connect(lambda: self.GoldSell_withmessage())
        self.DataEntry_button_2.clicked.connect(lambda: self.SilverSell_withmessage())
        self.DataEntry_button_3.clicked.connect(lambda: self.Old_Order_submit())
        self.DataEntry_button_4.clicked.connect(lambda: self.New_Order_submit())
        self.Data_Entry_button_5.clicked.connect(lambda: self.Shree_submit())
        self.Data_Entry_button_6.clicked.connect(lambda: self.VC_submit())
        self.Data_Entry_button_7.clicked.connect(lambda: self.GP_submit())
        self.Data_Entry_button_8.clicked.connect(lambda: self.SP_submit())
        self.Data_Entry_button_9.clicked.connect(lambda: self.Expense_submit())
        #Search Button triggers
        self.deletesearch.clicked.connect(lambda: self.del_search())
        #Delete Button trigger
        self.DelButton.clicked.connect(lambda: self.del_entry())
        #Generate Docs
        self.DocDate.setInputMask("99-99-9999")
        self.DocDate.setText(date.today().strftime("%d-%m-%Y"))
        self.DocSummary.setInputMask("99-99-9999")
        self.DocSummary.setText(date.today().strftime("%d-%m-%Y"))
        self.DocGenerate.clicked.connect(lambda: self.Doc_gen())
        #Tree Widget Set up
        self.SumStartdate.setInputMask("99-99-9999")
        self.SumStartdate.setText(date.today().strftime("%d-%m-%Y"))
        self.SumEnddate.setInputMask("99-99-9999")
        self.SumEnddate.setText(date.today().strftime("%d-%m-%Y"))

        # self.SumSearch.clicked.connect(lambda: self.Summary_search())
        self.Summarytree.setColumnCount(2)
        self.SumSearch.clicked.connect(lambda: self.Summary_show())

        #Net Wt Max Setter
        self.Gold_grwt.valueChanged.connect(lambda: self.Ntwtsetter(self.Gold_grwt, self.Gold_ntwt))
        self.Gold_grwt_2.valueChanged.connect(lambda: self.Ntwtsetter(self.Gold_grwt_2, self.Gold_ntwt_2))
        self.Gold_grwt_3.valueChanged.connect(lambda: self.Ntwtsetter(self.Gold_grwt_3, self.Gold_ntwt_3))
        self.Gold_grwt_4.valueChanged.connect(lambda: self.Ntwtsetter(self.Gold_grwt_4, self.Gold_ntwt_4))
        self.Gold_grwt_5.valueChanged.connect(lambda: self.Ntwtsetter(self.Gold_grwt_5, self.Gold_ntwt_5))
        self.Silver_grwt.valueChanged.connect(lambda: self.Ntwtsetter(self.Silver_grwt, self.Silver_ntwt))
        self.Silver_grwt_2.valueChanged.connect(lambda: self.Ntwtsetter(self.Silver_grwt_2, self.Silver_ntwt_2))
        self.Silver_grwt_3.valueChanged.connect(lambda: self.Ntwtsetter(self.Silver_grwt_3, self.Silver_ntwt_3))
        self.Silver_grwt_4.valueChanged.connect(lambda: self.Ntwtsetter(self.Silver_grwt_4, self.Silver_ntwt_4))
        self.Silver_grwt_5.valueChanged.connect(lambda: self.Ntwtsetter(self.Silver_grwt_5, self.Silver_ntwt_5))
        self.Old_Order_grwt.valueChanged.connect(lambda: self.Ntwtsetter(self.Old_Order_grwt, self.Old_Order_ntwt))
        self.Old_Order_grwt_2.valueChanged.connect(lambda: self.Ntwtsetter(self.Old_Order_grwt_2, self.Old_Order_ntwt_2))
        self.Old_Order_grwt_3.valueChanged.connect(lambda: self.Ntwtsetter(self.Old_Order_grwt_3, self.Old_Order_ntwt_3))
        self.Old_Order_grwt_4.valueChanged.connect(lambda: self.Ntwtsetter(self.Old_Order_grwt_4, self.Old_Order_ntwt_4))
        self.Old_Order_grwt_5.valueChanged.connect(lambda: self.Ntwtsetter(self.Old_Order_grwt_5, self.Old_Order_ntwt_5))
        self.New_Order_grwt.valueChanged.connect(lambda: self.Ntwtsetter(self.New_Order_grwt, self.New_Order_ntwt))
        self.New_Order_grwt_2.valueChanged.connect(lambda: self.Ntwtsetter(self.New_Order_grwt_2, self.New_Order_ntwt_2))
        self.New_Order_grwt_2.valueChanged.connect(lambda: self.Ntwtsetter(self.New_Order_grwt_2, self.New_Order_ntwt_2))
        self.New_Order_grwt_2.valueChanged.connect(lambda: self.Ntwtsetter(self.New_Order_grwt_2, self.New_Order_ntwt_2))
        self.New_Order_grwt_2.valueChanged.connect(lambda: self.Ntwtsetter(self.New_Order_grwt_2, self.New_Order_ntwt_2))
        self.VC_grwt.valueChanged.connect(lambda: self.Ntwtsetter(self.VC_grwt, self.VC_ntwt))
        self.VC_grwt_2.valueChanged.connect(lambda: self.Ntwtsetter(self.VC_grwt_2, self.VC_ntwt_2))
        self.VC_grwt_3.valueChanged.connect(lambda: self.Ntwtsetter(self.VC_grwt_3, self.VC_ntwt_3))
        self.VC_grwt_4.valueChanged.connect(lambda: self.Ntwtsetter(self.VC_grwt_4, self.VC_ntwt_4))
        self.VC_grwt_5.valueChanged.connect(lambda: self.Ntwtsetter(self.VC_grwt_5, self.VC_ntwt_5))
        self.GP_grwt.valueChanged.connect(lambda: self.Ntwtsetter(self.GP_grwt, self.GP_ntwt))
        self.GP_grwt_2.valueChanged.connect(lambda: self.Ntwtsetter(self.GP_grwt_2, self.GP_ntwt_2))
        self.GP_grwt_3.valueChanged.connect(lambda: self.Ntwtsetter(self.GP_grwt_3, self.GP_ntwt_3))
        self.GP_grwt_4.valueChanged.connect(lambda: self.Ntwtsetter(self.GP_grwt_4, self.GP_ntwt_4))
        self.GP_grwt_5.valueChanged.connect(lambda: self.Ntwtsetter(self.GP_grwt_5, self.GP_ntwt_5))
        self.SP_grwt.valueChanged.connect(lambda: self.Ntwtsetter(self.SP_grwt, self.SP_ntwt))
        self.SP_grwt_2.valueChanged.connect(lambda: self.Ntwtsetter(self.SP_grwt_2, self.SP_ntwt_2))
        self.SP_grwt_3.valueChanged.connect(lambda: self.Ntwtsetter(self.SP_grwt_3, self.SP_ntwt_3))
        self.SP_grwt_4.valueChanged.connect(lambda: self.Ntwtsetter(self.SP_grwt_4, self.SP_ntwt_4))
        self.SP_grwt_5.valueChanged.connect(lambda: self.Ntwtsetter(self.SP_grwt_5, self.SP_ntwt_5))
        #Grwt to Ntwt copy
        self.Gold_grwt.valueChanged.connect(lambda: self.Gold_ntwt.setValue(self.Gold_grwt.value()))
        self.Gold_grwt_2.valueChanged.connect(lambda: self.Gold_ntwt_2.setValue(self.Gold_grwt_2.value()))
        self.Gold_grwt_3.valueChanged.connect(lambda: self.Gold_ntwt_3.setValue(self.Gold_grwt_3.value()))
        self.Gold_grwt_4.valueChanged.connect(lambda: self.Gold_ntwt_4.setValue(self.Gold_grwt_4.value()))
        self.Gold_grwt_5.valueChanged.connect(lambda: self.Gold_ntwt_5.setValue(self.Gold_grwt_5.value()))
        self.Silver_grwt.valueChanged.connect(lambda: self.Silver_ntwt.setValue(self.Silver_grwt.value()))
        self.Silver_grwt_2.valueChanged.connect(lambda: self.Silver_ntwt_2.setValue(self.Silver_grwt_2.value()))
        self.Silver_grwt_3.valueChanged.connect(lambda: self.Silver_ntwt_3.setValue(self.Silver_grwt_3.value()))
        self.Silver_grwt_4.valueChanged.connect(lambda: self.Silver_ntwt_4.setValue(self.Silver_grwt_4.value()))
        self.Silver_grwt_5.valueChanged.connect(lambda: self.Silver_ntwt_5.setValue(self.Silver_grwt_5.value()))
        self.Old_Order_grwt.valueChanged.connect(lambda: self.Old_Order_ntwt.setValue(self.Old_Order_grwt.value()))
        self.Old_Order_grwt_2.valueChanged.connect(lambda: self.Old_Order_ntwt_2.setValue(self.Old_Order_grwt_2.value()))
        self.Old_Order_grwt_3.valueChanged.connect(lambda: self.Old_Order_ntwt_3.setValue(self.Old_Order_grwt_3.value()))
        self.Old_Order_grwt_4.valueChanged.connect(lambda: self.Old_Order_ntwt_4.setValue(self.Old_Order_grwt_4.value()))
        self.Old_Order_grwt_5.valueChanged.connect(lambda: self.Old_Order_ntwt_5.setValue(self.Old_Order_grwt_5.value()))
        self.New_Order_grwt.valueChanged.connect(lambda: self.New_Order_ntwt.setValue(self.New_Order_grwt.value()))
        self.New_Order_grwt_2.valueChanged.connect(lambda: self.New_Order_ntwt_2.setValue(self.New_Order_grwt_2.value()))
        self.New_Order_grwt_3.valueChanged.connect(lambda: self.New_Order_ntwt_3.setValue(self.New_Order_grwt_3.value()))
        self.New_Order_grwt_4.valueChanged.connect(lambda: self.New_Order_ntwt_4.setValue(self.New_Order_grwt_4.value()))
        self.New_Order_grwt_5.valueChanged.connect(lambda: self.New_Order_ntwt_5.setValue(self.New_Order_grwt_5.value()))
        self.VC_grwt.valueChanged.connect(lambda: self.VC_ntwt.setValue(self.VC_grwt.value()))
        self.VC_grwt_2.valueChanged.connect(lambda: self.VC_ntwt_2.setValue(self.VC_grwt_2.value()))
        self.VC_grwt_3.valueChanged.connect(lambda: self.VC_ntwt_3.setValue(self.VC_grwt_3.value()))
        self.VC_grwt_4.valueChanged.connect(lambda: self.VC_ntwt_4.setValue(self.VC_grwt_4.value()))
        self.VC_grwt_5.valueChanged.connect(lambda: self.VC_ntwt_5.setValue(self.VC_grwt_5.value()))
        self.GP_grwt.valueChanged.connect(lambda: self.GP_ntwt.setValue(self.GP_grwt.value()))
        self.GP_grwt_2.valueChanged.connect(lambda: self.GP_ntwt_2.setValue(self.GP_grwt_2.value()))
        self.GP_grwt_3.valueChanged.connect(lambda: self.GP_ntwt_3.setValue(self.GP_grwt_3.value()))
        self.GP_grwt_4.valueChanged.connect(lambda: self.GP_ntwt_4.setValue(self.GP_grwt_4.value()))
        self.GP_grwt_5.valueChanged.connect(lambda: self.GP_ntwt_5.setValue(self.GP_grwt_5.value()))
        self.SP_grwt.valueChanged.connect(lambda: self.SP_ntwt.setValue(self.SP_grwt.value()))
        self.SP_grwt_2.valueChanged.connect(lambda: self.SP_ntwt_2.setValue(self.SP_grwt_2.value()))
        self.SP_grwt_3.valueChanged.connect(lambda: self.SP_ntwt_3.setValue(self.SP_grwt_3.value()))
        self.SP_grwt_4.valueChanged.connect(lambda: self.SP_ntwt_4.setValue(self.SP_grwt_4.value()))
        self.SP_grwt_5.valueChanged.connect(lambda: self.SP_ntwt_5.setValue(self.SP_grwt_5.value()))
        self.Gold_BillAmount.valueChanged.connect(lambda: self.Gold_TotalAmount())
        self.Gold_BillAmount_2.valueChanged.connect(lambda: self.Gold_TotalAmount())
        self.Gold_BillAmount_3.valueChanged.connect(lambda: self.Gold_TotalAmount())
        self.Gold_BillAmount_4.valueChanged.connect(lambda: self.Gold_TotalAmount())
        self.Gold_BillAmount_5.valueChanged.connect(lambda: self.Gold_TotalAmount())
        self.Silver_BillAmount.valueChanged.connect(lambda: self.Silver_TotalAmount())
        self.Silver_BillAmount_2.valueChanged.connect(lambda: self.Silver_TotalAmount())
        self.Silver_BillAmount_3.valueChanged.connect(lambda: self.Silver_TotalAmount())
        self.Silver_BillAmount_4.valueChanged.connect(lambda: self.Silver_TotalAmount())
        self.Silver_BillAmount_5.valueChanged.connect(lambda: self.Silver_TotalAmount())
        self.Old_Order_Amount.valueChanged.connect(lambda: self.Old_Order_TotalAmount())
        self.Old_Order_Amount_2.valueChanged.connect(lambda: self.Old_Order_TotalAmount())
        self.Old_Order_Amount_3.valueChanged.connect(lambda: self.Old_Order_TotalAmount())
        self.Old_Order_Amount_4.valueChanged.connect(lambda: self.Old_Order_TotalAmount())
        self.Old_Order_Amount_5.valueChanged.connect(lambda: self.Old_Order_TotalAmount())
        self.New_Order_Adv.valueChanged.connect(lambda: self.New_Order_TotalAmount())
        self.New_Order_Adv_2.valueChanged.connect(lambda: self.New_Order_TotalAmount())
        self.New_Order_Adv_3.valueChanged.connect(lambda: self.New_Order_TotalAmount())
        self.New_Order_Adv_4.valueChanged.connect(lambda: self.New_Order_TotalAmount())
        self.New_Order_Adv_5.valueChanged.connect(lambda: self.New_Order_TotalAmount())
        self.VC_Amount_2.valueChanged.connect(lambda: self.VC_TotalAmount())
        self.VC_Amount_3.valueChanged.connect(lambda: self.VC_TotalAmount())
        self.VC_Amount_4.valueChanged.connect(lambda: self.VC_TotalAmount())
        self.VC_Amount_5.valueChanged.connect(lambda: self.VC_TotalAmount())
        self.VC_Amount_6.valueChanged.connect(lambda: self.VC_TotalAmount())
        self.GP_Amount.valueChanged.connect(lambda: self.GP_TotalAmount())
        self.GP_Amount_2.valueChanged.connect(lambda: self.GP_TotalAmount())
        self.GP_Amount_3.valueChanged.connect(lambda: self.GP_TotalAmount())
        self.GP_Amount_4.valueChanged.connect(lambda: self.GP_TotalAmount())
        self.GP_Amount_5.valueChanged.connect(lambda: self.GP_TotalAmount())
        self.SP_Amount.valueChanged.connect(lambda: self.SP_TotalAmount())
        self.SP_Amount_2.valueChanged.connect(lambda: self.SP_TotalAmount())
        self.SP_Amount_3.valueChanged.connect(lambda: self.SP_TotalAmount())
        self.SP_Amount_4.valueChanged.connect(lambda: self.SP_TotalAmount())
        self.SP_Amount_5.valueChanged.connect(lambda: self.SP_TotalAmount())
        #remember to do total for VC and NO
        self.URD_multiple.clicked.connect(self.URDdialog)
        self.URD_multiple_2.clicked.connect(self.URDdialog)
        self.URD_multiple_3.clicked.connect(self.URDdialog)
        self.URD_multiple_4.clicked.connect(self.URDdialog)
        #set validators
        self.OnlyInt=QtGui.QIntValidator()
        self.Gold_phnumber.setValidator(self.OnlyInt)
        self.Silver_phnumber.setValidator(self.OnlyInt)
        self.Old_Order_phnum.setValidator(self.OnlyInt)
        self.New_Order_phnum.setValidator(self.OnlyInt)
        self.VC_phnum.setValidator(self.OnlyInt)
        self.GP_phnum.setValidator(self.OnlyInt)
        self.SP_phnum.setValidator(self.OnlyInt)
        self.ChequeNo.setValidator(self.OnlyInt)
        self.ChequeNo_2.setValidator(self.OnlyInt)
        self.ChequeNo_3.setValidator(self.OnlyInt)
        self.ChequeNo_4.setValidator(self.OnlyInt)
        self.ChequeNo_5.setValidator(self.OnlyInt)
        self.ChequeNo_6.setValidator(self.OnlyInt)
        self.ChequeNo_7.setValidator(self.OnlyInt)
        self.Del_Bnum.setValidator(self.OnlyInt)

        #Initilize various button groups for cards
        self.GoldCardgroup=QtWidgets.QButtonGroup()
        self.GoldCardgroup.addButton(self.Gold_Cardmachine)
        self.GoldCardgroup.addButton(self.Gold_Cardmachine_2)
        self.GoldCardgroup.addButton(self.Gold_Cardmachine_3)
        self.GoldCardgroup.addButton(self.Gold_Cardmachine_4)
        self.SilverCardgroup=QtWidgets.QButtonGroup()
        self.SilverCardgroup.addButton(self.Silver_Cardmachine)
        self.SilverCardgroup.addButton(self.Silver_Cardmachine_2)
        self.SilverCardgroup.addButton(self.Silver_Cardmachine_3)
        self.SilverCardgroup.addButton(self.Silver_Cardmachine_4)
        self.OOCardgroup=QtWidgets.QButtonGroup()
        self.OOCardgroup.addButton(self.Old_Order_Cardmachine)
        self.OOCardgroup.addButton(self.Old_Order_Cardmachine_2)
        self.OOCardgroup.addButton(self.Old_Order_Cardmachine_3)
        self.OOCardgroup.addButton(self.Old_Order_Cardmachine_4)
        self.NOCardgroup=QtWidgets.QButtonGroup()
        self.NOCardgroup.addButton(self.New_Order_Cardmachine)
        self.NOCardgroup.addButton(self.New_Order_Cardmachine_2)
        self.NOCardgroup.addButton(self.New_Order_Cardmachine_3)
        self.NOCardgroup.addButton(self.New_Order_Cardmachine_4)
        self.VCCardgroup=QtWidgets.QButtonGroup()
        self.VCCardgroup.addButton(self.VC_Cardmachine)
        self.VCCardgroup.addButton(self.VC_Cardmachine_2)
        self.VCCardgroup.addButton(self.VC_Cardmachine_3)
        self.VCCardgroup.addButton(self.VC_Cardmachine_4)
        #Intialize groups for UPI
        self.GoldUPIgroup=QtWidgets.QButtonGroup()
        self.GoldUPIgroup.addButton(self.UPI_BharatPe)
        self.GoldUPIgroup.addButton(self.UPI_GPay)
        self.GoldUPIgroup.addButton(self.UPI_Other)
        self.SilverUPIgroup=QtWidgets.QButtonGroup()
        self.SilverUPIgroup.addButton(self.UPI_BharatPe_2)
        self.SilverUPIgroup.addButton(self.UPI_GPay_2)
        self.SilverUPIgroup.addButton(self.UPI_Other_2)
        self.OOUPIgroup=QtWidgets.QButtonGroup() 
        self.OOUPIgroup.addButton(self.UPI_BharatPe_3)
        self.OOUPIgroup.addButton(self.UPI_GPay_3)
        self.OOUPIgroup.addButton(self.UPI_Other_3)
        self.NOUPIgroup=QtWidgets.QButtonGroup()
        self.NOUPIgroup.addButton(self.UPI_BharatPe_4)
        self.NOUPIgroup.addButton(self.UPI_GPay_4)
        self.NOUPIgroup.addButton(self.UPI_Other_4)
        self.VCUPIgroup=QtWidgets.QButtonGroup()
        self.VCUPIgroup.addButton(self.UPI_BharatPe_5)
        self.VCUPIgroup.addButton(self.UPI_GPay_5)
        self.VCUPIgroup.addButton(self.UPI_Other_5)
        #Button group Initialization for Shree
        self.Shgroup=QtWidgets.QButtonGroup()
        self.Shgroup.addButton(self.Shree_plus)
        self.Shgroup.addButton(self.Shree_minus)
        #Button group for Generate Doc
        self.Docgroup=QtWidgets.QButtonGroup()
        self.Docgroup.addButton(self.DocCustom)
        self.Docgroup.addButton(self.DocDaily)
        self.Docgroup.addButton(self.DocSum)
        #update payment types
        self.Gold_total.valueChanged.connect(lambda: self.update_payment())
        self.Silver_total.valueChanged.connect(lambda: self.update_payment())
        self.Old_Order_Deposit.valueChanged.connect(lambda: self.update_payment())
        self.Old_Order_Total.valueChanged.connect(lambda: self.update_payment())
        self.Old_Order_Sale.toggled.connect(lambda: self.update_payment())
        self.New_Order_total.valueChanged.connect(lambda: self.update_payment())
        self.VC_total.valueChanged.connect(lambda: self.update_payment())
        self.VC_Amount.valueChanged.connect(lambda: self.update_payment())
        self.VC_Saleconvert.toggled.connect(lambda: self.update_payment())
        self.GP_total.valueChanged.connect(lambda: self.update_payment())
        self.GP_Cash.toggled.connect(lambda: self.update_payment())
        self.GP_Cheque.toggled.connect(lambda: self.update_payment())
        self.GP_Other.toggled.connect(lambda: self.update_payment())
        self.SP_total.valueChanged.connect(lambda: self.update_payment())
        self.SP_Cash.toggled.connect(lambda: self.update_payment())
        self.SP_Cheque.toggled.connect(lambda: self.update_payment())
        self.SP_Other.toggled.connect(lambda: self.update_payment())
        self.Card.valueChanged.connect(lambda: self.update_payment())
        self.Card_2.valueChanged.connect(lambda: self.update_payment())
        self.Card_3.valueChanged.connect(lambda: self.update_payment())
        self.Card_4.valueChanged.connect(lambda: self.update_payment())
        self.Card_5.valueChanged.connect(lambda: self.update_payment())
        self.Cheque.valueChanged.connect(lambda: self.update_payment())
        self.Cheque_2.valueChanged.connect(lambda: self.update_payment())
        self.Cheque_3.valueChanged.connect(lambda: self.update_payment())
        self.Cheque_4.valueChanged.connect(lambda: self.update_payment())
        self.Cheque_5.valueChanged.connect(lambda: self.update_payment())
        self.Cheque_6.valueChanged.connect(lambda: self.update_payment())
        self.Cheque_7.valueChanged.connect(lambda: self.update_payment())
        self.UPI.valueChanged.connect(lambda: self.update_payment())
        self.UPI_2.valueChanged.connect(lambda: self.update_payment())
        self.UPI_3.valueChanged.connect(lambda: self.update_payment())
        self.UPI_4.valueChanged.connect(lambda: self.update_payment())
        self.UPI_5.valueChanged.connect(lambda: self.update_payment())
        self.URDAmount.valueChanged.connect(lambda: self.update_payment())
        self.URDAmount_2.valueChanged.connect(lambda: self.update_payment())
        self.URDAmount_3.valueChanged.connect(lambda: self.update_payment())
        self.URDAmount_4.valueChanged.connect(lambda: self.update_payment())
        self.URDAmount_5.valueChanged.connect(lambda: self.update_payment())
        self.DebtAmount.valueChanged.connect(lambda: self.update_payment())
        self.DebtAmount_2.valueChanged.connect(lambda: self.update_payment)
        self.DebtAmount_3.valueChanged.connect(lambda: self.update_payment)
        self.DebtAmount_4.valueChanged.connect(lambda: self.update_payment)
        self.DebtAmount_5.valueChanged.connect(lambda: self.update_payment)
        self.URD_grwt.valueChanged.connect(lambda: self.URD_ntwt.setValue(self.URD_grwt.value()))
        self.URD_grwt_2.valueChanged.connect(lambda: self.URD_ntwt_2.setValue(self.URD_grwt_2.value()))
        self.URD_grwt_3.valueChanged.connect(lambda: self.URD_ntwt_3.setValue(self.URD_grwt_3.value()))
        self.URD_grwt_4.valueChanged.connect(lambda: self.URD_ntwt_4.setValue(self.URD_grwt_4.value()))
        self.URD_grwt_5.valueChanged.connect(lambda: self.URD_ntwt_5.setValue(self.URD_grwt_5.value()))
        self.ui.Submit.clicked.connect(lambda: self.connectdialog_withtransfer())
        self.Old_Order_Sale.toggled.connect(lambda: self.Old_order_switch())
        self.VC_Saleconvert.toggled.connect(lambda: self.VC_switch())
        self.NO_switch()
        self.New_Order_Goods.toggled.connect(lambda: self.NO_switch())
        self.GP_switch()
        self.GP_Cash.toggled.connect(lambda: self.GP_switch())
        self.GP_Cheque.toggled.connect(lambda: self.GP_switch())
        self.GP_Other.toggled.connect(lambda: self.GP_switch())
        self.SP_switch()
        self.SP_Cash.toggled.connect(lambda: self.SP_switch())
        self.SP_Cheque.toggled.connect(lambda: self.SP_switch())
        self.SP_Other.toggled.connect(lambda: self.SP_switch())
        self.Docgroup.buttonClicked.connect(lambda: self.Doc_switch())

        self.show()

    def Opning(self):
        #Opening Cash Show
        self.opnui=Opening()

    def Ntwtsetter(self, grwtbox, ntwtbox):
        ntwtbox.setMaximum(grwtbox.value())

    def ClosingCash(self):
        self.ccash=CCCalc()
        
    def MakingCalc(self):
        self.mcalc=Making()

    def Doc_gen(self):
        from datetime import datetime
        if self.DocStacked.currentIndex()==1:
            dte=datetime.strptime(self.DocDate.text(), "%d-%m-%Y")
            gen_billtoday(datetime.strftime(dte, "%Y-%m-%d"))
        if self.DocStacked.currentIndex()==2:
            gen_sum(self.DocSummary.text())

    def Summary_show(self):
        self.Summarytree.setHeaderLabels(["Item names","Pcs"])
        GS=QtWidgets.QTreeWidgetItem(self.Summarytree, ["Gold Sale",""])        
        SS=QtWidgets.QTreeWidgetItem(self.Summarytree, ["Silver Sale",""])        
        GP=QtWidgets.QTreeWidgetItem(self.Summarytree, ["Gold Purchase",""])
        SP=QtWidgets.QTreeWidgetItem(self.Summarytree, ["Silver Purchase",""])
        temp_data=Get_Sale_store(self.SumStartdate.text(), self.SumEnddate.text())
        dup_dict={}
        
        for values in temp_data["Silver Sale"]:
            if len(values)>1:
                for value in values:
                    if value[0] in dup_dict.keys():
                        dup_dict[value[0]]+=1
                    else:
                        dup_dict[value[0]]=1
        for key in dup_dict.keys():
            temp_child=QtWidgets.QTreeWidgetItem(SS, [key, dup_dict[key]])

    def Summary_search(self):
        temp_dict=Get_Sale_store(self.SumStartdate.text(), self.SumEnddate.text())
        if temp_dict==None:
            Sumconfirm=QtWidgets.QMessageBox()
            Sumconfirm.setIcon(QMessageBox.Information)
            Sumconfirm.setWindowTitle("Date Error")
            Sumconfirm.setText("Start Date comes after the End date please reenter and try again")
            Sumconfirm.setStandardButtons(QMessageBox.Ok)
            retval=Sumconfirm.exec_()
            return
        else:
            self.Summarytree
        print(temp_dict)

    def Doc_switch(self):
        tempradio=self.Docgroup.checkedButton().text()
        if tempradio=='Daily':
            self.DocStacked.setCurrentIndex(1)
        elif tempradio=='Summary':
            self.DocStacked.setCurrentIndex(2)
        elif tempradio=='Custom':
            self.DocStacked.setCurrentIndex(3)

    def del_entry(self):
        temprow=self.tableWidget.currentRow()
        if temprow > -1:
            delbillnum=(self.tableWidget.item(temprow, 0).text())
            delmsg=QMessageBox()
            delmsg.setIcon(QMessageBox.Information)
            delmsg.setText("Please confirm if you wish to delete the following bill:")
            delmsg.setInformativeText(f"""Bill No.: {self.tableWidget.item(temprow,0).text()}, Name: {self.tableWidget.item(temprow, 1).text()}, 
Transaction Type:  {self.tableWidget.item(temprow, 2).text()}, Amount: {self.tableWidget.item(temprow, 3).text()}, 
Date: {self.tableWidget.item(temprow, 4).text()}""")
            delmsg.setWindowTitle("Delete Bill Message Box")
            delmsg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            returnval=delmsg.exec_()
            if returnval==QMessageBox.Ok:
                del_billnum(delbillnum)
                self.tableWidget.removeRow(temprow)

    def del_search(self):
        if self.Del_Name.text()=='' and self.Del_Bnum.text()=='' and self.Del_type.currentIndex()==0:
            temp_table=Get_delBills()
        else:
            temp_table=Get_specificbills(self.Del_Name.text(), self.Del_Bnum.text(), self.Del_type.currentText())
        print(temp_table)
        self.tableWidget.setRowCount(0)
        for row, tup in enumerate(temp_table):
            self.tableWidget.insertRow(row)
            for col_num, col_data in enumerate(tup):
                self.tableWidget.setItem(row, col_num, QtWidgets.QTableWidgetItem(str(col_data)))

    def SP_switch(self):
        if self.SP_Cash.isChecked():
            self.Cash_7.setEnabled(True)
        else:
            self.Cash_7.setEnabled(False)
        if self.SP_Cheque.isChecked():
            self.Cheque_7.setEnabled(True)
            self.ChequeNo_7.setEnabled(True)
        else:
            self.Cheque_7.setEnabled(False)
            self.ChequeNo_7.setEnabled(False)
        if self.SP_Other.isChecked():
            self.Other_Amount_2.setEnabled(True)
            self.Other_Name_2.setEnabled(True)
        else:
            self.Other_Amount_2.setEnabled(False)
            self.Other_Name_2.setEnabled(False)

    def GP_switch(self):
        if self.GP_Cash.isChecked():
            self.Cash_6.setEnabled(True)
        else:
            self.Cash_6.setEnabled(False)
        if self.GP_Cheque.isChecked():
            self.Cheque_6.setEnabled(True)
            self.ChequeNo_6.setEnabled(True)
        else:
            self.Cheque_6.setEnabled(False)
            self.ChequeNo_6.setEnabled(False)
        if self.GP_Other.isChecked():
            self.Other_Amount.setEnabled(True)
            self.Other_Name.setEnabled(True)
        else:
            self.Other_Amount.setEnabled(False)
            self.Other_Name.setEnabled(False)

    def NO_switch(self):    
        NOcleardict={}
        NOcleardict[0]=self.New_Order_Itemname
        NOcleardict[1]=self.New_Order_Itemname_2
        NOcleardict[2]=self.New_Order_Itemname_3
        NOcleardict[3]=self.New_Order_Itemname_4
        NOcleardict[4]=self.New_Order_Itemname_5
        NOcleardict[5]=self.New_Order_grwt
        NOcleardict[6]=self.New_Order_grwt_2
        NOcleardict[7]=self.New_Order_grwt_3
        NOcleardict[8]=self.New_Order_grwt_4
        NOcleardict[9]=self.New_Order_grwt_5
        NOcleardict[10]=self.New_Order_ntwt
        NOcleardict[11]=self.New_Order_ntwt_2
        NOcleardict[12]=self.New_Order_ntwt_3
        NOcleardict[13]=self.New_Order_ntwt_4
        NOcleardict[14]=self.New_Order_ntwt_5
        NOcleardict[15]=self.New_Order_GS
        NOcleardict[16]=self.New_Order_GS_2
        NOcleardict[17]=self.New_Order_GS_3
        NOcleardict[18]=self.New_Order_GS_4
        NOcleardict[19]=self.New_Order_GS_5

        if self.New_Order_Goods.isChecked():
            state=True
        else:
            state=False
        for key in NOcleardict.keys():
            NOcleardict[key].setEnabled(state)

    def VC_switch(self):
        if self.VC_Saleconvert.isChecked():
            self.VC_Stacked.setCurrentIndex(1)
        else:
            self.VC_Stacked.setCurrentIndex(0)

    def Old_order_switch(self):
        if self.Old_Order_Sale.isChecked():
            self.Old_Order_stacked.setCurrentIndex(1)
        else:
            self.Old_Order_stacked.setCurrentIndex(0)

    def URDdialog(self):
        self.dialog.show()

    def connectdialog_withtransfer(self):
        if self.TransactionType.currentIndex()==1:
            self.URDAmount.setValue(self.ui.URD_total.value())
        elif self.TransactionType.currentIndex()==2:
            self.URDAmount_2.setValue(self.ui.URD_total.value())
        elif self.TransactionType.currentIndex()==3:
            self.URDAmount_3.setValue(self.ui.URD_total.value())
        elif self.TransactionType.currentIndex()==4:
            self.URDAmount_4.setValue(self.ui.URD_total.value())
        elif self.TransactionType.currentIndex()==6:
            self.URDAmount_5.setValue(self.ui.URD_total.value())
        self.ui.connect_dialog(self.dialog)
    
    def Gold_TotalAmount(self):
        total_amount=0
        for key in self.nextlist.keys():
            if "GS" in key:
                total_amount+=self.nextlist[key].amount
        if str(self.pagenum*5)+"GS" not in self.nextlist.keys():
            total_amount+=self.Gold_BillAmount.value()
        if str(self.pagenum*5+1)+"GS" not in self.nextlist.keys():
            total_amount+=self.Gold_BillAmount_2.value()
        if str(self.pagenum*5+2)+"GS" not in self.nextlist.keys():
            total_amount+=self.Gold_BillAmount_3.value()
        if str(self.pagenum*5+3)+"GS" not in self.nextlist.keys():
            total_amount+=self.Gold_BillAmount_4.value()
        if str(self.pagenum*5+4)+"GS" not in self.nextlist.keys():
            total_amount+=self.Gold_BillAmount_5.value()
        self.Gold_total.setValue(total_amount)

    def Silver_TotalAmount(self):
        total_amount=0
        for key in self.nextlist.keys():
            if "SS" in key:
                total_amount+=self.nextlist[key].amount
        if str(self.pagenum*5)+"SS" not in self.nextlist.keys():
            total_amount+=self.Silver_BillAmount.value()
        if str(self.pagenum*5+1)+"SS" not in self.nextlist.keys():
            total_amount+=self.Silver_BillAmount_2.value()
        if str(self.pagenum*5+2)+"SS" not in self.nextlist.keys():
            total_amount+=self.Silver_BillAmount_3.value()
        if str(self.pagenum*5+3)+"SS" not in self.nextlist.keys():
            total_amount+=self.Silver_BillAmount_4.value()
        if str(self.pagenum*5+4)+"SS" not in self.nextlist.keys():
            total_amount+=self.Silver_BillAmount_5.value()
        self.Silver_total.setValue(total_amount)

    def Old_Order_TotalAmount(self):
        total_amount=0
        for key in self.nextlist.keys():
            if "OO" in key:
                total_amount+=self.nextlist[key].amount
        if str(self.pagenum*5)+"OO" not in self.nextlist.keys():
            total_amount+=self.Old_Order_Amount.value()
        if str(self.pagenum*5+1)+"OO" not in self.nextlist.keys():
            total_amount+=self.Old_Order_Amount_2.value()
        if str(self.pagenum*5+2)+"OO" not in self.nextlist.keys():
            total_amount+=self.Old_Order_Amount_3.value()
        if str(self.pagenum*5+3)+"OO" not in self.nextlist.keys():
            total_amount+=self.Old_Order_Amount_4.value()
        if str(self.pagenum*5+4)+"OO" not in self.nextlist.keys():
            total_amount+=self.Old_Order_Amount_5.value()
        self.Old_Order_Total.setValue(total_amount)

    def New_Order_TotalAmount(self):
        total_amount=0
        for key in self.nextlist.keys():
            if "NO" in key:
                total_amount+=self.nextlist[key].amount
        if str(self.pagenum*5)+"NO" not in self.nextlist.keys():
            total_amount+=self.New_Order_Adv.value()
        if str(self.pagenum*5+1)+"NO" not in self.nextlist.keys():
            total_amount+=self.New_Order_Adv_2.value()
        if str(self.pagenum*5+2)+"NO" not in self.nextlist.keys():
            total_amount+=self.New_Order_Adv_3.value()
        if str(self.pagenum*5+3)+"NO" not in self.nextlist.keys():
            total_amount+=self.New_Order_Adv_4.value()
        if str(self.pagenum*5+4)+"NO" not in self.nextlist.keys():
            total_amount+=self.New_Order_Adv_5.value()
        self.New_Order_total.setValue(total_amount)

    def VC_TotalAmount(self):
        total_amount=0
        for key in self.nextlist.keys():
            if "VC" in key:
                total_amount+=self.nextlist[key].amount
        if str(self.pagenum*5)+"VC" not in self.nextlist.keys():
            total_amount+=self.VC_Amount_2.value()
        if str(self.pagenum*5+1)+"VC" not in self.nextlist.keys():
            total_amount+=self.VC_Amount_3.value()
        if str(self.pagenum*5+2)+"VC" not in self.nextlist.keys():
            total_amount+=self.VC_Amount_4.value()
        if str(self.pagenum*5+3)+"VC" not in self.nextlist.keys():
            total_amount+=self.VC_Amount_5.value()
        if str(self.pagenum*5+4)+"VC" not in self.nextlist.keys():
            total_amount+=self.VC_Amount_6.value()
        self.VC_total.setValue(total_amount)

    def GP_TotalAmount(self):
        total_amount=0
        for key in self.nextlist.keys():
            if "GP" in key:
                total_amount+=self.nextlist[key].amount
        if str(self.pagenum*5)+"GP" not in self.nextlist.keys():
            total_amount+=self.GP_Amount.value()
        if str(self.pagenum*5+1)+"GP" not in self.nextlist.keys():
            total_amount+=self.GP_Amount_2.value()
        if str(self.pagenum*5+2)+"GP" not in self.nextlist.keys():
            total_amount+=self.GP_Amount_3.value()
        if str(self.pagenum*5+3)+"GP" not in self.nextlist.keys():
            total_amount+=self.GP_Amount_4.value()
        if str(self.pagenum*5+4)+"GP" not in self.nextlist.keys():
            total_amount+=self.GP_Amount_5.value()
        self.GP_total.setValue(total_amount)

    def SP_TotalAmount(self):
        total_amount=0
        for key in self.nextlist.keys():
            if "SP" in key:
                total_amount+=self.nextlist[key].amount
        if str(self.pagenum*5)+"SP" not in self.nextlist.keys():
            total_amount+=self.SP_Amount.value()
        if str(self.pagenum*5+1)+"SP" not in self.nextlist.keys():
            total_amount+=self.SP_Amount_2.value()
        if str(self.pagenum*5+2)+"SP" not in self.nextlist.keys():
            total_amount+=self.SP_Amount_3.value()
        if str(self.pagenum*5+3)+"SP" not in self.nextlist.keys():
            total_amount+=self.SP_Amount_4.value()
        if str(self.pagenum*5+4)+"SP" not in self.nextlist.keys():
            total_amount+=self.SP_Amount_5.value()
        self.SP_total.setValue(total_amount)

    def Switch_Widgets(self):
        if self.stackedWidget.currentIndex() != self.TransactionType.currentIndex():
            self.stackedWidget.setCurrentIndex(self.TransactionType.currentIndex())
            self.nextlist.clear()
            self.pagenum=0

    def GoldNext(self):
        if self.Gold_itemname.text() != '' and self.Gold_Itemid.value()!=0 and self.Gold_purity.text() != '' and self.Gold_grwt.value() != 0.000 and self.Gold_ntwt.value() != 0.000 or self.Gold_BillAmount.value() != 0:
            self.nextlist[str(self.pagenum*5)+"GS"]=((GoldSell(self.Gold_custname.text(), self.Gold_phnumber.text(), self.Gold_itemname.text(), self.Gold_Itemid.value(), self.Gold_grwt.value(), self.Gold_ntwt.value(), self.Gold_BillAmount.value(), self.Gold_purity.text(), date.today())))
        if self.Gold_itemname_2.text() != '' and self.Gold_Itemid_2.value()!=0 and self.Gold_purity_2.text() != '' and self.Gold_grwt_2.value() != 0.000 and self.Gold_ntwt_2.value() != 0.000 or self.Gold_BillAmount.value() != 0:
            self.nextlist[str(self.pagenum*5+1)+"GS"]=(GoldSell(self.Gold_custname.text(), self.Gold_phnumber.text(), self.Gold_itemname_2.text(), self.Gold_Itemid_2.value(), self.Gold_grwt_2.value(), self.Gold_ntwt_2.value(), self.Gold_BillAmount_2.value(), self.Gold_purity_2.text(), date.today()))        
        if self.Gold_itemname_3.text() != '' and self.Gold_Itemid_3.value()!=0 and self.Gold_purity_3.text() != '' and self.Gold_grwt_3.value() != 0.000 and self.Gold_ntwt_3.value() != 0.000 or self.Gold_BillAmount_3.value() != 0:
            self.nextlist[str(self.pagenum*5+2)+"GS"]=(GoldSell(self.Gold_custname.text(), self.Gold_phnumber.text(), self.Gold_itemname_3.text(), self.Gold_Itemid_3.value(), self.Gold_grwt_3.value(), self.Gold_ntwt_3.value(), self.Gold_BillAmount_3.value(), self.Gold_purity_3.text(), date.today()))
        if self.Gold_itemname_4.text() != '' and self.Gold_Itemid_4.value()!=0 and self.Gold_purity_4.text() != '' and self.Gold_grwt_4.value() != 0.000 and self.Gold_ntwt_4.value() != 0.000 or self.Gold_BillAmount_4.value() != 0:
            self.nextlist[str(self.pagenum*5+3)+"GS"]=(GoldSell(self.Gold_custname.text(), self.Gold_phnumber.text(), self.Gold_itemname_4.text(), self.Gold_Itemid_4.value(), self.Gold_grwt_4.value(), self.Gold_ntwt_4.value(), self.Gold_BillAmount_4.value(), self.Gold_purity_4.text(), date.today()))
        if self.Gold_itemname_5.text() != '' and self.Gold_Itemid_5.value()!=0 and self.Gold_purity_5.text() != '' and self.Gold_grwt_5.value() != 0.000 and self.Gold_ntwt_5.value() != 0.000 or self.Gold_BillAmount_5.value() != 0:
            self.nextlist[str(self.pagenum*5+4)+"GS"]=(GoldSell(self.Gold_custname.text(), self.Gold_phnumber.text(), self.Gold_itemname_5.text(), self.Gold_Itemid_5.value(), self.Gold_grwt_5.value(), self.Gold_ntwt_5.value(), self.Gold_BillAmount_5.value(), self.Gold_purity_5.text(), date.today()))
        self.pagenum+=1
        self.clearQlineedit()
        if (str(self.pagenum*5)+"GS") in self.nextlist.keys():
            self.Gold_itemname.setText(self.nextlist[str(self.pagenum*5)+"GS"].pr_name)
            self.Gold_Itemid.setValue(self.nextlist[str(self.pagenum*5)+"GS"].id)
            self.Gold_purity.setText(self.nextlist[str(self.pagenum*5)+"GS"].purity)
            self.Gold_grwt.setValue(self.nextlist[str(self.pagenum*5)+"GS"].gr_wt)
            self.Gold_ntwt.setValue(self.nextlist[str(self.pagenum*5)+"GS"].nt_wt)
            self.Gold_BillAmount.setValue(self.nextlist[str(self.pagenum*5)+"GS"].amount)
        if (str(self.pagenum*5+1)+"GS") in self.nextlist.keys():
            self.Gold_itemname_2.setText(self.nextlist[str(self.pagenum*5+1)+"GS"].pr_name)
            self.Gold_Itemid_2.setValue(self.nextlist[str(self.pagenum*5+1)+"GS"].id)
            self.Gold_purity_2.setText(self.nextlist[str(self.pagenum*5+1)+"GS"].purity)
            self.Gold_grwt_2.setValue(self.nextlist[str(self.pagenum*5+1)+"GS"].gr_wt)
            self.Gold_ntwt_2.setValue(self.nextlist[str(self.pagenum*5+1)+"GS"].nt_wt)
            self.Gold_BillAmount_2.setValue(self.nextlist[str(self.pagenum*5+1)+"GS"].amount)
        if (str(self.pagenum*5+2)+"GS") in self.nextlist.keys():
            self.Gold_itemname_3.setText(self.nextlist[str(self.pagenum*5+2)+"GS"].pr_name)
            self.Gold_Itemid_3.setValue(self.nextlist[str(self.pagenum*5+2)+"GS"].id)
            self.Gold_purity_3.setText(self.nextlist[str(self.pagenum*5+2)+"GS"].purity)
            self.Gold_grwt_3.setValue(self.nextlist[str(self.pagenum*5+2)+"GS"].gr_wt)
            self.Gold_ntwt_3.setValue(self.nextlist[str(self.pagenum*5+2)+"GS"].nt_wt)
            self.Gold_BillAmount_3.setValue(self.nextlist[str(self.pagenum*5+2)+"GS"].amount)
        if (str(self.pagenum*5+3)+"GS") in self.nextlist.keys():
            self.Gold_itemname_4.setText(self.nextlist[str(self.pagenum*5+3)+"GS"].pr_name)
            self.Gold_Itemid_4.setValue(self.nextlist[str(self.pagenum*5+3)+"GS"].id)
            self.Gold_purity_4.setText(self.nextliststr[(self.pagenum*5+3)+"GS"].purity)
            self.Gold_grwt_4.setValue(self.nextlist[str(self.pagenum*5+3)+"GS"].gr_wt)
            self.Gold_ntwt_4.setValue(self.nextlist[str(self.pagenum*5+3)+"GS"].nt_wt)
            self.Gold_BillAmount_4.setValue(self.nextlist[str(self.pagenum*5+3)+"GS"].amount)
        if (str(self.pagenum*5+4)+"GS") in self.nextlist.keys():
            self.Gold_itemname_5.setText(self.nextlist[str(self.pagenum*5+4)+"GS"].pr_name)
            self.Gold_Itemid_5.setValue(self.nextlist[str(self.pagenum*5+4)+"GS"].id)
            self.Gold_purity_5.setText(self.nextlist[str(self.pagenum*5+4)+"GS"].purity)
            self.Gold_grwt_5.setValue(self.nextlist[str(self.pagenum*5+4)+"GS"].gr_wt)
            self.Gold_ntwt_5.setValue(self.nextlist[str(self.pagenum*5+4)+"GS"].nt_wt)
            self.Gold_BillAmount_5.setValue(self.nextlist[str(self.pagenum*5+4)+"GS"].amount)
             
    def GoldPrevious(self):
        if self.pagenum < 1:
            GoldPreviousError=QtWidgets.QMessageBox()
            GoldPreviousError.setIcon(QMessageBox.Warning)
            GoldPreviousError.setWindowTitle("Already on the first page")
            GoldPreviousError.setText("As there is no previous page we cannot display it.")
            GoldPreviousError.setStandardButtons(QMessageBox.Ok)
            retval=GoldPreviousError.exec_()
            return
        else:   
            if self.Gold_itemname.text() != '' and self.Gold_Itemid.value()!=0 and self.Gold_purity.text() != '' and self.Gold_grwt.value() != 0.000 and self.Gold_ntwt.value() != 0.000 and self.Gold_BillAmount.value() != 0:
                self.nextlist[str(self.pagenum*5)+"GS"]=((GoldSell(self.Gold_custname.text(), self.Gold_phnumber.text(), self.Gold_itemname.text(), self.Gold_Itemid.value(), self.Gold_grwt.value(), self.Gold_ntwt.value(), self.Gold_BillAmount.value(), self.Gold_purity.text(), date.today())))
            if self.Gold_itemname_2.text() != '' and self.Gold_Itemid_2.value()!=0 and self.Gold_purity_2.text() != '' and self.Gold_grwt_2.value() != 0.000 and self.Gold_ntwt_2.value() != 0.000 and self.Gold_BillAmount.value() != 0:
                self.nextlist[str(self.pagenum*5+1)+"GS"]=(GoldSell(self.Gold_custname.text(), self.Gold_phnumber.text(), self.Gold_itemname_2.text(), self.Gold_Itemid_2.value(), self.Gold_grwt_2.value(), self.Gold_ntwt_2.value(), self.Gold_BillAmount_2.value(), self.Gold_purity_2.text(), date.today()))        
            if self.Gold_itemname_3.text() != '' and self.Gold_Itemid_3.value()!=0 and self.Gold_purity_3.text() != '' and self.Gold_grwt_3.value() != 0.000 and self.Gold_ntwt_3.value() != 0.000 and self.Gold_BillAmount_3.value() != 0:
                self.nextlist[str(self.pagenum*5+2)+"GS"]=(GoldSell(self.Gold_custname.text(), self.Gold_phnumber.text(), self.Gold_itemname_3.text(), self.Gold_Itemid_3.value(), self.Gold_grwt_3.value(), self.Gold_ntwt_3.value(), self.Gold_BillAmount_3.value(), self.Gold_purity_3.text(), date.today()))
            if self.Gold_itemname_4.text() != '' and self.Gold_Itemid_4.value()!=0 and self.Gold_purity_4.text() != '' and self.Gold_grwt_4.value() != 0.000 and self.Gold_ntwt_4.value() != 0.000 and self.Gold_BillAmount_4.value() != 0:
                self.nextlist[str(self.pagenum*5+3)+"GS"]=(GoldSell(self.Gold_custname.text(), self.Gold_phnumber.text(), self.Gold_itemname_4.text(), self.Gold_Itemid_4.value(), self.Gold_grwt_4.value(), self.Gold_ntwt_4.value(), self.Gold_BillAmount_4.value(), self.Gold_purity_4.text(), date.today()))
            if self.Gold_itemname_5.text() != '' and self.Gold_Itemid_5.value()!=0 and self.Gold_purity_5.text() != '' and self.Gold_grwt_5.value() != 0.000 and self.Gold_ntwt_5.value() != 0.000 and self.Gold_BillAmount_5.value() != 0:
                self.nextlist[str(self.pagenum*5+4)+"GS"]=(GoldSell(self.Gold_custname.text(), self.Gold_phnumber.text(), self.Gold_itemname_5.text(), self.Gold_Itemid_5.value(), self.Gold_grwt_5.value(), self.Gold_ntwt_5.value(), self.Gold_BillAmount_5.value(), self.Gold_purity_5.text(), date.today()))
            self.pagenum-=1
            self.clearQlineedit()
            if (str(self.pagenum*5)+"GS") in self.nextlist.keys():
                self.Gold_itemname.setText(self.nextlist[str(self.pagenum*5)+"GS"].pr_name)
                self.Gold_Itemid.setValue(self.nextlist[str(self.pagenum*5)+"GS"].id)
                self.Gold_purity.setText(self.nextlist[str(self.pagenum*5)+"GS"].purity)
                self.Gold_grwt.setValue(self.nextlist[str(self.pagenum*5)+"GS"].gr_wt)
                self.Gold_ntwt.setValue(self.nextlist[str(self.pagenum*5)+"GS"].nt_wt)
                self.Gold_BillAmount.setValue(self.nextlist[str(self.pagenum*5)+"GS"].amount)
            if (str(self.pagenum*5+1)+"GS") in self.nextlist.keys():
                self.Gold_itemname_2.setText(self.nextlist[str(self.pagenum*5+1)+"GS"].pr_name)
                self.Gold_Itemid_2.setValue(self.nextlist[str(self.pagenum*5+1)+"GS"].id)
                self.Gold_purity_2.setText(self.nextlist[str(self.pagenum*5+1)+"GS"].purity)
                self.Gold_grwt_2.setValue(self.nextlist[str(self.pagenum*5+1)+"GS"].gr_wt)
                self.Gold_ntwt_2.setValue(self.nextlist[str(self.pagenum*5+1)+"GS"].nt_wt)
                self.Gold_BillAmount_2.setValue(self.nextlist[str(self.pagenum*5+1)+"GS"].amount)
            if (str(self.pagenum*5+2)+"GS") in self.nextlist.keys():
                self.Gold_itemname_3.setText(self.nextlist[str(self.pagenum*5+2)+"GS"].pr_name)
                self.Gold_Itemid_3.setValue(self.nextlist[str(self.pagenum*5+2)+"GS"].id)
                self.Gold_purity_3.setText(self.nextlist[str(self.pagenum*5+2)+"GS"].purity)
                self.Gold_grwt_3.setValue(self.nextlist[str(self.pagenum*5+2)+"GS"].gr_wt)
                self.Gold_ntwt_3.setValue(self.nextlist[str(self.pagenum*5+2)+"GS"].nt_wt)
                self.Gold_BillAmount_3.setValue(self.nextlist[str(self.pagenum*5+2)+"GS"].amount)
            if (str(self.pagenum*5+3)+"GS") in self.nextlist.keys():
                self.Gold_itemname_4.setText(self.nextlist[str(self.pagenum*5+3)+"GS"].pr_name)
                self.Gold_Itemid_4.setValue(self.nextlist[str(self.pagenum*5+3)+"GS"].id)
                self.Gold_purity_4.setText(self.nextlist[str(self.pagenum*5+3)+"GS"].purity)
                self.Gold_grwt_4.setValue(self.nextlist[str(self.pagenum*5+3)+"GS"].gr_wt)
                self.Gold_ntwt_4.setValue(self.nextlist[str(self.pagenum*5+3)+"GS"].nt_wt)
                self.Gold_BillAmount_4.setValue(self.nextlist[str(self.pagenum*5+3)+"GS"].amount)
            if (str(self.pagenum*5+4)+"GS") in self.nextlist.keys():
                self.Gold_itemname_5.setText(self.nextlist[str(self.pagenum*5+4)+"GS"].pr_name)
                self.Gold_Itemid_5.setValue(self.nextlist[str(self.pagenum*5+4)+"GS"].id)
                self.Gold_purity_5.setText(self.nextlist[str(self.pagenum*5+4)+"GS"].purity)
                self.Gold_grwt_5.setValue(self.nextlist[str(self.pagenum*5+4)+"GS"].gr_wt)
                self.Gold_ntwt_5.setValue(self.nextlist[str(self.pagenum*5+4)+"GS"].nt_wt)
                self.Gold_BillAmount_5.setValue(self.nextlist[str(self.pagenum*5+4)+"GS"].amount)

    def SilverPrevious(self):
        if self.pagenum < 1:
            SilverPreviousError=QtWidgets.QMessageBox()
            SilverPreviousError.setIcon(QMessageBox.Warning)
            SilverPreviousError.setWindowTitle("Already on the first page")
            SilverPreviousError.setText("As there is no previous page we cannot display it.")
            SilverPreviousError.setStandardButtons(QMessageBox.Ok)
            retval=SilverPreviousError.exec_()
            return
        else:   
            if self.Silver_itemname.text() != '' and self.Silver_Itemid.value()!=0 and self.Silver_purity.text() != '' and self.Silver_grwt.value() != 0.000 and self.Silver_ntwt.value() != 0.000 and self.Silver_BillAmount.value() != 0:
                self.nextlist[str(self.pagenum*5)+"SS"]=((SilverSell(self.Silver_custname.text(), self.Silver_phnumber.text(), self.Silver_itemname.text(), self.Silver_Itemid.value(), self.Silver_grwt.value(), self.Silver_ntwt.value(), self.Silver_BillAmount.value(), self.Silver_purity.text(), date.today())))
            if self.Silver_itemname_2.text() != '' and self.Silver_Itemid_2.value()!=0 and self.Silver_purity_2.text() != '' and self.Silver_grwt_2.value() != 0.000 and self.Silver_ntwt_2.value() != 0.000 and self.Silver_BillAmount.value() != 0:
                self.nextlist[str(self.pagenum*5+1)+"SS"]=(SilverSell(self.Silver_custname.text(), self.Silver_phnumber.text(), self.Silver_itemname_2.text(), self.Silver_Itemid_2.value(), self.Silver_grwt_2.value(), self.Silver_ntwt_2.value(), self.Silver_BillAmount_2.value(), self.Silver_purity_2.text(), date.today()))        
            if self.Silver_itemname_3.text() != '' and self.Silver_Itemid_3.value()!=0 and self.Silver_purity_3.text() != '' and self.Silver_grwt_3.value() != 0.000 and self.Silver_ntwt_3.value() != 0.000 and self.Silver_BillAmount_3.value() != 0:
                self.nextlist[str(self.pagenum*5+2)+"SS"]=(SilverSell(self.Silver_custname.text(), self.Silver_phnumber.text(), self.Silver_itemname_3.text(), self.Silver_Itemid_3.value(), self.Silver_grwt_3.value(), self.Silver_ntwt_3.value(), self.Silver_BillAmount_3.value(), self.Silver_purity_3.text(), date.today()))
            if self.Silver_itemname_4.text() != '' and self.Silver_Itemid_4.value()!=0 and self.Silver_purity_4.text() != '' and self.Silver_grwt_4.value() != 0.000 and self.Silver_ntwt_4.value() != 0.000 and self.Silver_BillAmount_4.value() != 0:
                self.nextlist[str(self.pagenum*5+3)+"SS"]=(SilverSell(self.Silver_custname.text(), self.Silver_phnumber.text(), self.Silver_itemname_4.text(), self.Silver_Itemid_4.value(), self.Silver_grwt_4.value(), self.Silver_ntwt_4.value(), self.Silver_BillAmount_4.value(), self.Silver_purity_4.text(), date.today()))
            if self.Silver_itemname_5.text() != '' and self.Silver_Itemid_5.value()!=0 and self.Silver_purity_5.text() != '' and self.Silver_grwt_5.value() != 0.000 and self.Silver_ntwt_5.value() != 0.000 and self.Silver_BillAmount_5.value() != 0:
                self.nextlist[str(self.pagenum*5+4)+"SS"]=(SilverSell(self.Silver_custname.text(), self.Silver_phnumber.text(), self.Silver_itemname_5.text(), self.Silver_Itemid_5.value(), self.Silver_grwt_5.value(), self.Silver_ntwt_5.value(), self.Silver_BillAmount_5.value(), self.Silver_purity_5.text(), date.today()))
            self.pagenum-=1
            self.clearQlineedit()
            if (str(self.pagenum*5)+"SS") in self.nextlist.keys():
                self.Silver_itemname.setText(self.nextlist[str(self.pagenum*5)+"SS"].pr_name)
                self.Silver_Itemid.setValue(self.nextlist[str(self.pagenum*5)+"SS"].id)
                self.Silver_purity.setText(self.nextlist[str(self.pagenum*5)+"SS"].purity)
                self.Silver_grwt.setValue(self.nextlist[str(self.pagenum*5)+"SS"].gr_wt)
                self.Silver_ntwt.setValue(self.nextlist[str(self.pagenum*5)+"SS"].nt_wt)
                self.Silver_BillAmount.setValue(self.nextlist[str(self.pagenum*5)+"SS"].amount)
            if (str(self.pagenum*5+1)+"SS") in self.nextlist.keys():
                self.Silver_itemname_2.setText(self.nextlist[str(self.pagenum*5+1)+"SS"].pr_name)
                self.Silver_Itemid_2.setValue(self.nextlist[str(self.pagenum*5+1)+"SS"].id)
                self.Silver_purity_2.setText(self.nextlist[str(self.pagenum*5+1)+"SS"].purity)
                self.Silver_grwt_2.setValue(self.nextlist[str(self.pagenum*5+1)+"SS"].gr_wt)
                self.Silver_ntwt_2.setValue(self.nextlist[str(self.pagenum*5+1)+"SS"].nt_wt)
                self.Silver_BillAmount_2.setValue(self.nextlist[str(self.pagenum*5+1)+"SS"].amount)
            if (str(self.pagenum*5+2)+"SS") in self.nextlist.keys():
                self.Silver_itemname_3.setText(self.nextlist[str(self.pagenum*5+2)+"SS"].pr_name)
                self.Silver_Itemid_3.setValue(self.nextlist[str(self.pagenum*5+2)+"SS"].id)
                self.Silver_purity_3.setText(self.nextlist[str(self.pagenum*5+2)+"SS"].purity)
                self.Silver_grwt_3.setValue(self.nextlist[str(self.pagenum*5+2)+"SS"].gr_wt)
                self.Silver_ntwt_3.setValue(self.nextlist[str(self.pagenum*5+2)+"SS"].nt_wt)
                self.Silver_BillAmount_3.setValue(self.nextlist[str(self.pagenum*5+1)+"SS"].amount)
            if (str(self.pagenum*5+3)+"SS") in self.nextlist.keys():
                self.Silver_itemname_4.setText(self.nextlist[str(self.pagenum*5+3)+"SS"].pr_name)
                self.Silver_Itemid_4.setValue(self.nextlist[str(self.pagenum*5+3)+"SS"].id)
                self.Silver_purity_4.setText(self.nextlist[str(self.pagenum*5+3)+"SS"].purity)
                self.Silver_grwt_4.setValue(self.nextlist[str(self.pagenum*5+3)+"SS"].gr_wt)
                self.Silver_ntwt_4.setValue(self.nextlist[str(self.pagenum*5+3)+"SS"].nt_wt)
                self.Silver_BillAmount_4.setValue(self.nextlist[str(self.pagenum*5+3)+"SS"].amount)
            if (str(self.pagenum*5+4)+"SS") in self.nextlist.keys():
                self.Silver_itemname_5.setText(self.nextlist[str(self.pagenum*5+4)+"SS"].pr_name)
                self.Silver_Itemid_5.setValue(self.nextlist[str(self.pagenum*5+4)+"SS"].id)
                self.Silver_purity_5.setText(self.nextlist[str(self.pagenum*5+4)+"SS"].purity)
                self.Silver_grwt_5.setValue(self.nextlist[str(self.pagenum*5+4)+"SS"].gr_wt)
                self.Silver_ntwt_5.setValue(self.nextlist[str(self.pagenum*5+4)+"SS"].nt_wt)
                self.Silver_BillAmount_5.setValue(self.nextlist[str(self.pagenum*5+4)+"SS"].amount)

    def SilverNext(self):
        if self.Silver_itemname.text() != '' and self.Silver_Itemid.value()!=0 and self.Silver_purity.text() != '' and self.Silver_grwt.value() != 0.000 and self.Silver_ntwt.value() != 0.000 and self.Silver_BillAmount.value() != 0:
            self.nextlist[str(self.pagenum*5)+"SS"]=((SilverSell(self.Silver_custname.text(), self.Silver_phnumber.text(), self.Silver_itemname.text(), self.Silver_Itemid.value(), self.Silver_grwt.value(), self.Silver_ntwt.value(), self.Silver_BillAmount.value(), self.Silver_purity.text(), date.today())))
        if self.Silver_itemname_2.text() != '' and self.Silver_Itemid_2.value()!=0 and self.Silver_purity_2.text() != '' and self.Silver_grwt_2.value() != 0.000 and self.Silver_ntwt_2.value() != 0.000 and self.Silver_BillAmount.value() != 0:
            self.nextlist[str(self.pagenum*5+1)+"SS"]=(SilverSell(self.Silver_custname.text(), self.Silver_phnumber.text(), self.Silver_itemname_2.text(), self.Silver_Itemid_2.value(), self.Silver_grwt_2.value(), self.Silver_ntwt_2.value(), self.Silver_BillAmount_2.value(), self.Silver_purity_2.text(), date.today()))        
        if self.Silver_itemname_3.text() != '' and self.Silver_Itemid_3.value()!=0 and self.Silver_purity_3.text() != '' and self.Silver_grwt_3.value() != 0.000 and self.Silver_ntwt_3.value() != 0.000 and self.Silver_BillAmount_3.value() != 0:
            self.nextlist[str(self.pagenum*5+2)+"SS"]=(SilverSell(self.Silver_custname.text(), self.Silver_phnumber.text(), self.Silver_itemname_3.text(), self.Silver_Itemid_3.value(), self.Silver_grwt_3.value(), self.Silver_ntwt_3.value(), self.Silver_BillAmount_3.value(), self.Silver_purity_3.text(), date.today()))
        if self.Silver_itemname_4.text() != '' and self.Silver_Itemid_4.value()!=0 and self.Silver_purity_4.text() != '' and self.Silver_grwt_4.value() != 0.000 and self.Silver_ntwt_4.value() != 0.000 and self.Silver_BillAmount_4.value() != 0:
            self.nextlist[str(self.pagenum*5+3)+"SS"]=(SilverSell(self.Silver_custname.text(), self.Silver_phnumber.text(), self.Silver_itemname_4.text(), self.Silver_Itemid_4.value(), self.Silver_grwt_4.value(), self.Silver_ntwt_4.value(), self.Silver_BillAmount_4.value(), self.Silver_purity_4.text(), date.today()))
        if self.Silver_itemname_5.text() != '' and self.Silver_Itemid_5.value()!=0 and self.Silver_purity_5.text() != '' and self.Silver_grwt_5.value() != 0.000 and self.Silver_ntwt_5.value() != 0.000 and self.Silver_BillAmount_5.value() != 0:
            self.nextlist[str(self.pagenum*5+4)+"SS"]=(SilverSell(self.Silver_custname.text(), self.Silver_phnumber.text(), self.Silver_itemname_5.text(), self.Silver_Itemid_5.value(), self.Silver_grwt_5.value(), self.Silver_ntwt_5.value(), self.Silver_BillAmount_5.value(), self.Silver_purity_5.text(), date.today()))
        self.pagenum+=1
        self.clearQlineedit()
        if (str(self.pagenum*5)+"SS") in self.nextlist.keys():
            self.Silver_itemname.setText(self.nextlist[str(self.pagenum*5)+"SS"].pr_name)
            self.Silver_Itemid.setValue(self.nextlist[str(self.pagenum*5)+"SS"].id)
            self.Silver_purity.setText(self.nextlist[str(self.pagenum*5)+"SS"].purity)
            self.Silver_grwt.setValue(self.nextlist[str(self.pagenum*5)+"SS"].gr_wt)
            self.Silver_ntwt.setValue(self.nextlist[str(self.pagenum*5)+"SS"].nt_wt)
            self.Silver_BillAmount.setValue(self.nextlist[str(self.pagenum*5)+"SS"].amount)
        if (str(self.pagenum*5+1)+"SS") in self.nextlist.keys():
            self.Silver_itemname_2.setText(self.nextlist[str(self.pagenum*5+1)+"SS"].pr_name)
            self.Silver_Itemid_2.setValue(self.nextlist[str(self.pagenum*5+1)+"SS"].id)
            self.Silver_purity_2.setText(self.nextlist[str(self.pagenum*5+1)+"SS"].purity)
            self.Silver_grwt_2.setValue(self.nextlist[str(self.pagenum*5+1)+"SS"].gr_wt)
            self.Silver_ntwt_2.setValue(self.nextlist[str(self.pagenum*5+1)+"SS"].nt_wt)
            self.Silver_BillAmount_2.setValue(self.nextlist[str(self.pagenum*5+1)+"SS"].amount)
        if (str(self.pagenum*5+2)+"SS") in self.nextlist.keys():
            self.Silver_itemname_3.setText(self.nextlist[str(self.pagenum*5+2)+"SS"].pr_name)
            self.Silver_Itemid_3.setValue(self.nextlist[str(self.pagenum*5+2)+"SS"].id)
            self.Silver_purity_3.setText(self.nextlist[str(self.pagenum*5+2)+"SS"].purity)
            self.Silver_grwt_3.setValue(self.nextlist[str(self.pagenum*5+2)+"SS"].gr_wt)
            self.Silver_ntwt_3.setValue(self.nextlist[str(self.pagenum*5+2)+"SS"].nt_wt)
            self.Silver_BillAmount_3.setValue(self.nextlist[str(self.pagenum*5+2)+"SS"].amount)
        if (str(self.pagenum*5+3)+"SS") in self.nextlist.keys():
            self.Silver_itemname_4.setText(self.nextlist[str(self.pagenum*5+3)+"SS"].pr_name)
            self.Silver_Itemid_4.setValue(self.nextlist[str(self.pagenum*5+3)+"SS"].id)
            self.Silver_purity_4.setText(self.nextliststr[(self.pagenum*5+3)+"SS"].purity)
            self.Silver_grwt_4.setValue(self.nextlist[str(self.pagenum*5+3)+"SS"].gr_wt)
            self.Silver_ntwt_4.setValue(self.nextlist[str(self.pagenum*5+3)+"SS"].nt_wt)
            self.Silver_BillAmount_4.setValue(self.nextlist[str(self.pagenum*5+3)+"SS"].amount)
        if (str(self.pagenum*5+4)+"SS") in self.nextlist.keys():
            self.Silver_itemname_5.setText(self.nextlist[str(self.pagenum*5+4)+"SS"].pr_name)
            self.Silver_Itemid_5.setValue(self.nextlist[str(self.pagenum*5+4)+"SS"].id)
            self.Silver_purity_5.setText(self.nextlist[str(self.pagenum*5+4)+"SS"].purity)
            self.Silver_grwt_5.setValue(self.nextlist[str(self.pagenum*5+4)+"SS"].gr_wt)
            self.Silver_ntwt_5.setValue(self.nextlist[str(self.pagenum*5+4)+"SS"].nt_wt)
            self.Silver_BillAmount_5.setValue(self.nextlist[str(self.pagenum*5+4)+"SS"].amount)

    def OONext(self):
        if self.Old_Order_Amount.value()!=0 and self.Old_Order_Itemname!='' and self.Old_Order_grwt!= 0.000 and self.Old_Order_ntwt!= 0.000:
            self.nextlist[str(self.pagenum*5)+"OO"]=OldOrder(self.Old_Order_GS.currentText() ,self.Old_Order_Amount.value(), 
                            self.Old_Order_Itemname.text(), self.Old_Order_grwt.value(), self.Old_Order_ntwt.value())
        if self.Old_Order_Amount_2.value()!=0 and self.Old_Order_Itemname_2!='' and self.Old_Order_grwt_2!= 0.000 and self.Old_Order_ntwt_2!= 0.000:
            self.nextlist[str(self.pagenum*5+1)+"OO"]=OldOrder(self.Old_Order_GS_2.currentText() ,self.Old_Order_Amount_2.value(), 
                            self.Old_Order_Itemname_2.text(), self.Old_Order_grwt_2.value(), self.Old_Order_ntwt_2.value())
        if self.Old_Order_Amount_3.value()!=0 and self.Old_Order_Itemname_3!='' and self.Old_Order_grwt_3!= 0.000 and self.Old_Order_ntwt_3!= 0.000:
            self.nextlist[str(self.pagenum*5+2)+"OO"]=OldOrder(self.Old_Order_GS_3.currentText() ,self.Old_Order_Amount_3.value(), 
                            self.Old_Order_Itemname_3.text(), self.Old_Order_grwt_3.value(), self.Old_Order_ntwt_3.value())
        if self.Old_Order_Amount_4.value()!=0 and self.Old_Order_Itemname_4!='' and self.Old_Order_grwt_4!= 0.000 and self.Old_Order_ntwt_4!= 0.000:
            self.nextlist[str(self.pagenum*5+3)+"OO"]=OldOrder(self.Old_Order_GS_4.currentText() ,self.Old_Order_Amount_4.value(), 
                            self.Old_Order_Itemname_4.text(), self.Old_Order_grwt_k.value(), self.Old_Order_ntwt_4.value())
        if self.Old_Order_Amount_5.value()!=0 and self.Old_Order_Itemname_5!='' and self.Old_Order_grwt_5!= 0.000 and self.Old_Order_ntwt_5!= 0.000:
            self.nextlist[str(self.pagenum*5+4)+"OO"]=OldOrder(self.Old_Order_GS_5.currentText() ,self.Old_Order_Amount_5.value(), 
                            self.Old_Order_Itemname_5.text(), self.Old_Order_grwt_5.value(), self.Old_Order_ntwt_5.value())
        self.pagenum+=1
        self.clearQlineedit()
        if str(self.pagenum*5)+"OO" in self.nextlist.keys():
            self.Old_Order_GS.setCurrentText(self.nextlist[str(self.pagenum*5)+"OO"].type)
            self.Old_Order_Amount.setValue(self.nextlist[str(self.pagenum*5)+"OO"].amount)
            self.Old_Order_Itemname.setText(self.nextlist[str(self.pagenum*5)+"OO"].item)
            self.Old_Order_grwt.setValue(self.nextlist[str(self.pagenum*5)+"OO"].grwt)
            self.Old_Order_ntwt.setValue(self.nextlist[str(self.pagenum*5)+"OO"].ntwt)
        if str(self.pagenum*5+1)+"OO" in self.nextlist.keys():
            self.Old_Order_GS_2.setCurrentText(self.nextlist[str(self.pagenum*5+1)+"OO"].type)
            self.Old_Order_Amount_2.setValue(self.nextlist[str(self.pagenum*5+1)+"OO"].amount)
            self.Old_Order_Itemname_2.setText(self.nextlist[str(self.pagenum*5+1)+"OO"].item)
            self.Old_Order_grwt_2.setValue(self.nextlist[str(self.pagenum*5+1)+"OO"].grwt)
            self.Old_Order_ntwt_2.setValue(self.nextlist[str(self.pagenum*5+1)+"OO"].ntwt)
        if str(self.pagenum*5+2)+"OO" in self.nextlist.keys():
            self.Old_Order_GS_3.setCurrentText(self.nextlist[str(self.pagenum*5+2)+"OO"].type)
            self.Old_Order_Amount_3.setValue(self.nextlist[str(self.pagenum*5+2)+"OO"].amount)
            self.Old_Order_Itemname_3.setText(self.nextlist[str(self.pagenum*5+2)+"OO"].item)
            self.Old_Order_grwt_3.setValue(self.nextlist[str(self.pagenum*5+2)+"OO"].grwt)
            self.Old_Order_ntwt_3.setValue(self.nextlist[str(self.pagenum*5+2)+"OO"].ntwt)
        if str(self.pagenum*5+3)+"OO" in self.nextlist.keys():
            self.Old_Order_GS_4.setCurrentText(self.nextlist[str(self.pagenum*5+3)+"OO"].type)
            self.Old_Order_Amount_4.setValue(self.nextlist[str(self.pagenum*5+3)+"OO"].amount)
            self.Old_Order_Itemname_4.setText(self.nextlist[str(self.pagenum*5+3)+"OO"].item)
            self.Old_Order_grwt_4.setValue(self.nextlist[str(self.pagenum*5+3)+"OO"].grwt)
            self.Old_Order_ntwt_4.setValue(self.nextlist[str(self.pagenum*5+3)+"OO"].ntwt)
        if str(self.pagenum*5+4)+"OO" in self.nextlist.keys():
            self.Old_Order_GS_5.setCurrentText(self.nextlist[str(self.pagenum*5+4)+"OO"].type)
            self.Old_Order_Amount_5.setValue(self.nextlist[str(self.pagenum*5+4)+"OO"].amount)
            self.Old_Order_Itemname_5.setText(self.nextlist[str(self.pagenum*5+4)+"OO"].item)
            self.Old_Order_grwt_5.setValue(self.nextlist[str(self.pagenum*5+4)+"OO"].grwt)
            self.Old_Order_ntwt_5.setValue(self.nextlist[str(self.pagenum*5+4)+"OO"].ntwt)

    def OOPrevious(self):
        if  self.pagenum < 1:
            OOPreviousError=QtWidgets.QMessageBox()
            OOPreviousError.setIcon(QMessageBox.Warning)
            OOPreviousError.setWindowTitle("Already on the first page")
            OOPreviousError.setText("As there is no previous page we cannot display it.")
            OOPreviousError.setStandardButtons(QMessageBox.Ok)
            retval=OOPreviousError.exec_()
            return
        else:
            if self.Old_Order_Amount.value()!=0 and self.Old_Order_Itemname!='' and self.Old_Order_grwt!= 0.000 and self.Old_Order_ntwt!= 0.000:
                self.nextlist[str(self.pagenum*5)+"OO"]=OldOrder(self.Old_Order_GS.currentText() ,self.Old_Order_Amount.value(), 
                            self.Old_Order_Itemname.text(), self.Old_Order_grwt.value(), self.Old_Order_ntwt.value())
            if self.Old_Order_Amount_2.value()!=0 and self.Old_Order_Itemname_2!='' and self.Old_Order_grwt_2!= 0.000 and self.Old_Order_ntwt_2!= 0.000:
                self.nextlist[str(self.pagenum*5+1)+"OO"]=OldOrder(self.Old_Order_GS_2.currentText() ,self.Old_Order_Amount_2.value(), 
                            self.Old_Order_Itemname_2.text(), self.Old_Order_grwt_2.value(), self.Old_Order_ntwt_2.value())
            if self.Old_Order_Amount_3.value()!=0 and self.Old_Order_Itemname_3!='' and self.Old_Order_grwt_3!= 0.000 and self.Old_Order_ntwt_3!= 0.000:
                self.nextlist[str(self.pagenum*5+2)+"OO"]=OldOrder(self.Old_Order_GS_3.currentText() ,self.Old_Order_Amount_3.value(), 
                            self.Old_Order_Itemname_3.text(), self.Old_Order_grwt_3.value(), self.Old_Order_ntwt_3.value())
            if self.Old_Order_Amount_4.value()!=0 and self.Old_Order_Itemname_4!='' and self.Old_Order_grwt_4!= 0.000 and self.Old_Order_ntwt_4!= 0.000:
                self.nextlist[str(self.pagenum*5+3)+"OO"]=OldOrder(self.Old_Order_GS_4.currentText() ,self.Old_Order_Amount_4.value(), 
                            self.Old_Order_Itemname_4.text(), self.Old_Order_grwt_k.value(), self.Old_Order_ntwt_4.value())
            if self.Old_Order_Amount_5.value()!=0 and self.Old_Order_Itemname_5!='' and self.Old_Order_grwt_5!= 0.000 and self.Old_Order_ntwt_5!= 0.000:
                self.nextlist[str(self.pagenum*5+4)+"OO"]=OldOrder(self.Old_Order_GS_5.currentText() ,self.Old_Order_Amount_5.value(), 
                            self.Old_Order_Itemname_5.text(), self.Old_Order_grwt_5.value(), self.Old_Order_ntwt_5.value())
            self.pagenum+=1
            self.clearQlineedit()
            if str(self.pagenum*5)+"OO" in self.nextlist.keys():
                self.Old_Order_GS.setCurrentText(self.nextlist[str(self.pagenum*5)+"OO"].type)
                self.Old_Order_Amount.setValue(self.nextlist[str(self.pagenum*5)+"OO"].amount)
                self.Old_Order_Itemname.setText(self.nextlist[str(self.pagenum*5)+"OO"].item)
                self.Old_Order_grwt.setValue(self.nextlist[str(self.pagenum*5)+"OO"].grwt)
                self.Old_Order_ntwt.setValue(self.nextlist[str(self.pagenum*5)+"OO"].ntwt)
            if str(self.pagenum*5+1)+"OO" in self.nextlist.keys():
                self.Old_Order_GS_2.setCurrentText(self.nextlist[str(self.pagenum*5+1)+"OO"].type)
                self.Old_Order_Amount_2.setValue(self.nextlist[str(self.pagenum*5+1)+"OO"].amount)
                self.Old_Order_Itemname_2.setText(self.nextlist[str(self.pagenum*5+1)+"OO"].item)
                self.Old_Order_grwt_2.setValue(self.nextlist[str(self.pagenum*5+1)+"OO"].grwt)
                self.Old_Order_ntwt_2.setValue(self.nextlist[str(self.pagenum*5+1)+"OO"].ntwt)
            if str(self.pagenum*5+2)+"OO" in self.nextlist.keys():
                self.Old_Order_GS_3.setCurrentText(self.nextlist[str(self.pagenum*5+2)+"OO"].type)
                self.Old_Order_Amount_3.setValue(self.nextlist[str(self.pagenum*5+2)+"OO"].amount)
                self.Old_Order_Itemname_3.setText(self.nextlist[str(self.pagenum*5+2)+"OO"].item)
                self.Old_Order_grwt_3.setValue(self.nextlist[str(self.pagenum*5+2)+"OO"].grwt)
                self.Old_Order_ntwt_3.setValue(self.nextlist[str(self.pagenum*5+2)+"OO"].ntwt)
            if str(self.pagenum*5+3)+"OO" in self.nextlist.keys():
                self.Old_Order_GS_4.setCurrentText(self.nextlist[str(self.pagenum*5+3)+"OO"].type)
                self.Old_Order_Amount_4.setValue(self.nextlist[str(self.pagenum*5+3)+"OO"].amount)
                self.Old_Order_Itemname_4.setText(self.nextlist[str(self.pagenum*5+3)+"OO"].item)
                self.Old_Order_grwt_4.setValue(self.nextlist[str(self.pagenum*5+3)+"OO"].grwt)
                self.Old_Order_ntwt_4.setValue(self.nextlist[str(self.pagenum*5+3)+"OO"].ntwt)
            if str(self.pagenum*5+4)+"OO" in self.nextlist.keys():
                self.Old_Order_GS_5.setCurrentText(self.nextlist[str(self.pagenum*5+4)+"OO"].type)
                self.Old_Order_Amount_5.setValue(self.nextlist[str(self.pagenum*5+4)+"OO"].amount)
                self.Old_Order_Itemname_5.setText(self.nextlist[str(self.pagenum*5+4)+"OO"].item)
                self.Old_Order_grwt_5.setValue(self.nextlist[str(self.pagenum*5+4)+"OO"].grwt)
                self.Old_Order_ntwt_5.setValue(self.nextlist[str(self.pagenum*5+4)+"OO"].ntwt)
       
    def VC_Next(self):
        if self.VC_Itemname.text()!= '' and self.VC_Amount.value() != 0 and self.VC_grwt.value() != 0.000 and self.VC_ntwt.value() != 0.000:
            self.nextlist[str(self.pagenum*5)+"VC"]=VC(self.VC_GS.currentText(), self.VC_Itemname.text(), self.VC_Amount.value(), self.VC_grwt.value(), self.VC_ntwt.value())
        if self.VC_Itemname_2.text()!= '' and self.VC_Amount_2.value() != 0 and self.VC_grwt_2.value() != 0.000 and self.VC_ntwt_2.value() != 0.000:
            self.nextlist[str(self.pagenum*5+1)+"VC"]=VC(self.VC_GS_2.currentText(), self.VC_Itemname_2.text(), self.VC_Amount_2.value(), self.VC_grwt_2.value(), self.VC_ntwt_2.value())
        if self.VC_Itemname_3.text()!= '' and self.VC_Amount_3.value() != 0 and self.VC_grwt_3.value() != 0.000 and self.VC_ntwt_3.value() != 0.000:
            self.nextlist[str(self.pagenum*5+2)+"VC"]=VC(self.VC_GS_3.currentText(), self.VC_Itemname_3.text(), self.VC_Amount_3.value(), self.VC_grwt_3.value(), self.VC_ntwt_3.value())
        if self.VC_Itemname_4.text()!= '' and self.VC_Amount_4.value() != 0 and self.VC_grwt_4.value() != 0.000 and self.VC_ntwt_4.value() != 0.000:
            self.nextlist[str(self.pagenum*5+3)+"VC"]=VC(self.VC_GS_4.currentText(), self.VC_Itemname_4.text(), self.VC_Amount_4.value(), self.VC_grwt_4.value(), self.VC_ntwt_4.value())
        if self.VC_Itemname_5.text()!= '' and self.VC_Amount_5.value() != 0 and self.VC_grwt_5.value() != 0.000 and self.VC_ntwt_5.value() != 0.000:
            self.nextlist[str(self.pagenum*5+4)+"VC"]=VC(self.VC_GS_5.currentText(), self.VC_Itemname_5.text(), self.VC_Amount_5.value(), self.VC_grwt_5.value(), self.VC_ntwt_5.value())
        self.pagenum+=1
        self.clearQlineedit()
        if str(self.pagenum*5)+"VC" in self.nextlist.keys():
            self.VC_GS.setCurrentText(self.nextlist[str(self.pagenum*5)+"VC"].type)
            self.VC_Itemname.setText(self.nextlist[str(self.pagenum*5)+"VC"].item)
            self.VC_Amount.setValue(self.nextlist[str(self.pagenum*5)+"VC"].amount)
            self.VC_grwt.setValue(self.nextlist[str(self.pagenum*5)+"VC"].grwt)
            self.VC_ntwt.setValue(self.nextlist[str(self.pagenum*5)+"VC"].ntwt)
        if str(self.pagenum*5+1)+"VC" in self.nextlist.keys():
            self.VC_GS_2.setCurrentText(self.nextlist[str(self.pagenum*5+1)+"VC"].type)
            self.VC_Itemname_2.setText(self.nextlist[str(self.pagenum*5+1)+"VC"].item)
            self.VC_Amount_2.setValue(self.nextlist[str(self.pagenum*5+1)+"VC"].amount)
            self.VC_grwt_2.setValue(self.nextlist[str(self.pagenum*5+1)+"VC"].grwt)
            self.VC_ntwt_2.setValue(self.nextlist[str(self.pagenum*5+1)+"VC"].ntwt)
        if str(self.pagenum*5+2)+"VC" in self.nextlist.keys():
            self.VC_GS_3.setCurrentText(self.nextlist[str(self.pagenum*5+2)+"VC"].type)
            self.VC_Itemname_3.setText(self.nextlist[str(self.pagenum*5+2)+"VC"].item)
            self.VC_Amount_3.setValue(self.nextlist[str(self.pagenum*5+2)+"VC"].amount)
            self.VC_grwt_3.setValue(self.nextlist[str(self.pagenum*5+2)+"VC"].grwt)
            self.VC_ntwt_3.setValue(self.nextlist[str(self.pagenum*5+2)+"VC"].ntwt)
        if str(self.pagenum*5+3)+"VC" in self.nextlist.keys():
            self.VC_GS_4.setCurrentText(self.nextlist[str(self.pagenum*5+3)+"VC"].type)
            self.VC_Itemname_4.setText(self.nextlist[str(self.pagenum*5+3)+"VC"].item)
            self.VC_Amount_4.setValue(self.nextlist[str(self.pagenum*5+3)+"VC"].amount)
            self.VC_grwt_4.setValue(self.nextlist[str(self.pagenum*5+3)+"VC"].grwt)
            self.VC_ntwt_4.setValue(self.nextlist[str(self.pagenum*5+3)+"VC"].ntwt)
        if str(self.pagenum*5+4)+"VC" in self.nextlist.keys():
            self.VC_GS_5.setCurrentText(self.nextlist[str(self.pagenum*5+4)+"VC"].type)
            self.VC_Itemname_5.setText(self.nextlist[str(self.pagenum*5+4)+"VC"].item)
            self.VC_Amount_5.setValue(self.nextlist[str(self.pagenum*5+4)+"VC"].amount)
            self.VC_grwt_5.setValue(self.nextlist[str(self.pagenum*5+4)+"VC"].grwt)
            self.VC_ntwt_5.setValue(self.nextlist[str(self.pagenum*5+4)+"VC"].ntwt)

    def VC_Previous(self):
        if self.pagenum < 1:
            VCPreviousError=QtWidgets.QMessageBox()
            VCPreviousError.setIcon(QMessageBox.Warning)
            VCPreviousError.setWindowTitle("Already on the first page")
            VCPreviousError.setText("As there is no previous page we cannot display it.")
            VCPreviousError.setStandardButtons(QMessageBox.Ok)
            retval=VCPreviousError.exec_()
            return
        else:
            if self.VC_Itemname.text()!= '' and self.VC_Amount.value() != 0 and self.VC_grwt.value() != 0.000 and self.VC_ntwt.value() != 0.000:
                self.nextlist[str(self.pagenum*5)+"VC"]=VC(self.VC_GS.currentText(), self.VC_Itemname.text(), self.VC_Amount.value(), self.VC_grwt.value(), self.VC_ntwt.value())
            if self.VC_Itemname_2.text()!= '' and self.VC_Amount_2.value() != 0 and self.VC_grwt_2.value() != 0.000 and self.VC_ntwt_2.value() != 0.000:
                self.nextlist[str(self.pagenum*5+1)+"VC"]=VC(self.VC_GS_2.currentText(), self.VC_Itemname_2.text(), self.VC_Amount_2.value(), self.VC_grwt_2.value(), self.VC_ntwt_2.value())
            if self.VC_Itemname_3.text()!= '' and self.VC_Amount_3.value() != 0 and self.VC_grwt_3.value() != 0.000 and self.VC_ntwt_3.value() != 0.000:
                self.nextlist[str(self.pagenum*5+2)+"VC"]=VC(self.VC_GS_3.currentText(), self.VC_Itemname_3.text(), self.VC_Amount_3.value(), self.VC_grwt_3.value(), self.VC_ntwt_3.value())
            if self.VC_Itemname_4.text()!= '' and self.VC_Amount_4.value() != 0 and self.VC_grwt_4.value() != 0.000 and self.VC_ntwt_4.value() != 0.000:
                self.nextlist[str(self.pagenum*5+3)+"VC"]=VC(self.VC_GS_4.currentText(), self.VC_Itemname_4.text(), self.VC_Amount_4.value(), self.VC_grwt_4.value(), self.VC_ntwt_4.value())
            if self.VC_Itemname_5.text()!= '' and self.VC_Amount_5.value() != 0 and self.VC_grwt_5.value() != 0.000 and self.VC_ntwt_5.value() != 0.000:
                self.nextlist[str(self.pagenum*5+4)+"VC"]=VC(self.VC_GS_5.currentText(), self.VC_Itemname_5.text(), self.VC_Amount_5.value(), self.VC_grwt_5.value(), self.VC_ntwt_5.value())
            self.pagenum+=1
            self.clearQlineedit()
            if str(self.pagenum*5)+"VC" in self.nextlist.keys():
                self.VC_GS.setCurrentText(self.nextlist[str(self.pagenum*5)+"VC"].type)
                self.VC_Itemname.setText(self.nextlist[str(self.pagenum*5)+"VC"].item)
                self.VC_Amount.setValue(self.nextlist[str(self.pagenum*5)+"VC"].amount)
                self.VC_grwt.setValue(self.nextlist[str(self.pagenum*5)+"VC"].grwt)
                self.VC_ntwt.setValue(self.nextlist[str(self.pagenum*5)+"VC"].ntwt)
            if str(self.pagenum*5+1)+"VC" in self.nextlist.keys():
                self.VC_GS_2.setCurrentText(self.nextlist[str(self.pagenum*5+1)+"VC"].type)
                self.VC_Itemname_2.setText(self.nextlist[str(self.pagenum*5+1)+"VC"].item)
                self.VC_Amount_2.setValue(self.nextlist[str(self.pagenum*5+1)+"VC"].amount)
                self.VC_grwt_2.setValue(self.nextlist[str(self.pagenum*5+1)+"VC"].grwt)
                self.VC_ntwt_2.setValue(self.nextlist[str(self.pagenum*5+1)+"VC"].ntwt)
            if str(self.pagenum*5+2)+"VC" in self.nextlist.keys():
                self.VC_GS_3.setCurrentText(self.nextlist[str(self.pagenum*5+2)+"VC"].type)
                self.VC_Itemname_3.setText(self.nextlist[str(self.pagenum*5+2)+"VC"].item)
                self.VC_Amount_3.setValue(self.nextlist[str(self.pagenum*5+2)+"VC"].amount)
                self.VC_grwt_3.setValue(self.nextlist[str(self.pagenum*5+2)+"VC"].grwt)
                self.VC_ntwt_3.setValue(self.nextlist[str(self.pagenum*5+2)+"VC"].ntwt)
            if str(self.pagenum*5+3)+"VC" in self.nextlist.keys():
                self.VC_GS_4.setCurrentText(self.nextlist[str(self.pagenum*5+3)+"VC"].type)
                self.VC_Itemname_4.setText(self.nextlist[str(self.pagenum*5+3)+"VC"].item)
                self.VC_Amount_4.setValue(self.nextlist[str(self.pagenum*5+3)+"VC"].amount)
                self.VC_grwt_4.setValue(self.nextlist[str(self.pagenum*5+3)+"VC"].grwt)
                self.VC_ntwt_4.setValue(self.nextlist[str(self.pagenum*5+3)+"VC"].ntwt)
            if str(self.pagenum*5+4)+"VC" in self.nextlist.keys():
                self.VC_GS_5.setCurrentText(self.nextlist[str(self.pagenum*5+4)+"VC"].type)
                self.VC_Itemname_5.setText(self.nextlist[str(self.pagenum*5+4)+"VC"].item)
                self.VC_Amount_5.setValue(self.nextlist[str(self.pagenum*5+4)+"VC"].amount)
                self.VC_grwt_5.setValue(self.nextlist[str(self.pagenum*5+4)+"VC"].grwt)
                self.VC_ntwt_5.setValue(self.nextlist[str(self.pagenum*5+4)+"VC"].ntwt)

    def GP_Previous(self):
        if self.pagenum < 1:
            GPPreviousError=QtWidgets.QMessageBox()
            GPPreviousError.setIcon(QMessageBox.Warning)
            GPPreviousError.setWindowTitle("Already on the first page")
            GPPreviousError.setText("As there is no previous page we cannot display it.")
            GPPreviousError.setStandardButtons(QMessageBox.Ok)
            retval=GPPreviousError.exec_()
            return
        else:
            if self.GP_Itemname.text()!='' and self.GP_grwt.value()!=0.0 and self.GP_ntwt.value()!=0.0 and self.GP_Amount!=0:
                self.nextlist[str(self.pagenum*5)+"GP"]=purchase('Gold Purchase', self.GP_Itemname.text(), self.GP_grwt.value(), 
                self.GP_ntwt.value(), self.GP_Amount.value())
            if self.GP_Itemname_2.text()!='' and self.GP_grwt_2.value()!=0.0 and self.GP_ntwt_2.value()!=0.0 and self.GP_Amount_2!=0:
                self.nextlist[str(self.pagenum*5+1)+"GP"]=purchase('Gold Purchase', self.GP_Itemname_2.text(), self.GP_grwt_2.value(), 
                self.GP_ntwt_2.value(), self.GP_Amount_2.value())
            if self.GP_Itemname_3.text()!='' and self.GP_grwt_3.value()!=0.0 and self.GP_ntwt_3.value()!=0.0 and self.GP_Amount_3!=0:
                self.nextlist[str(self.pagenum*5+2)+"GP"]=purchase('Gold Purchase', self.GP_Itemname_3.text(), self.GP_grwt_3.value(), 
                self.GP_ntwt_3.value(), self.GP_Amount_3.value())
            if self.GP_Itemname_4.text()!='' and self.GP_grwt_4.value()!=0.0 and self.GP_ntwt_4.value()!=0.0 and self.GP_Amount_4!=0:
                self.nextlist[str(self.pagenum*5+3)+"GP"]=purchase('Gold Purchase', self.GP_Itemname_4.text(), self.GP_grwt_4.value(), 
                self.GP_ntwt_4.value(), self.GP_Amount_4.value())
            if self.GP_Itemname_5.text()!='' and self.GP_grwt_5.value()!=0.0 and self.GP_ntwt_5.value()!=0.0 and self.GP_Amount_5!=0:
                self.nextlist[str(self.pagenum*5+4)+"GP"]=purchase('Gold Purchase', self.GP_Itemname_5.text(), self.GP_grwt_5.value(), 
                self.GP_ntwt_5.value(), self.GP_Amount_5.value())
            self.pagenum-=1
            self.clearQlineedit()
            if str(self.pagenum*5)+"GP" in self.nextlist.keys():
                self.GP_Itemname.setText(self.nextlist[str(self.pagenum*5)+"GP"].item)
                self.GP_grwt.setValue(self.nextlist[str(self.pagenum*5)+"GP"].grwt)
                self.GP_ntwt.setValue(self.nextlist[str(self.pagenum*5)+"GP"].ntwt)
                self.GP_Amount.setValue(self.nextlist[str(self.pagenum*5)+"GP"].amount)
            if str(self.pagenum*5+1)+"GP" in self.nextlist.keys():
                self.GP_Itemname_2.setText(self.nextlist[str(self.pagenum*5+1)+"GP"].item)
                self.GP_grwt_2.setValue(self.nextlist[str(self.pagenum*5+1)+"GP"].grwt)
                self.GP_ntwt_2.setValue(self.nextlist[str(self.pagenum*5+1)+"GP"].ntwt)
                self.GP_Amount_2.setValue(self.nextlist[str(self.pagenum*5+1)+"GP"].amount)
            if str(self.pagenum*5+2)+"GP" in self.nextlist.keys():
                self.GP_Itemname_3.setText(self.nextlist[str(self.pagenum*5+2)+"GP"].item)
                self.GP_grwt_3.setValue(self.nextlist[str(self.pagenum*5+2)+"GP"].grwt)
                self.GP_ntwt_3.setValue(self.nextlist[str(self.pagenum*5+2)+"GP"].ntwt)
                self.GP_Amount_3.setValue(self.nextlist[str(self.pagenum*5+2)+"GP"].amount)
            if str(self.pagenum*5+3)+"GP" in self.nextlist.keys():
                self.GP_Itemname_4.setText(self.nextlist[str(self.pagenum*5+3)+"GP"].item)
                self.GP_grwt_4.setValue(self.nextlist[str(self.pagenum*5+3)+"GP"].grwt)
                self.GP_ntwt_4.setValue(self.nextlist[str(self.pagenum*5+3)+"GP"].ntwt)
                self.GP_Amount_4.setValue(self.nextlist[str(self.pagenum*5+3)+"GP"].amount)
            if str(self.pagenum*5+4)+"GP" in self.nextlist.keys():
                self.GP_Itemname_5.setText(self.nextlist[str(self.pagenum*5+4)+"GP"].item)
                self.GP_grwt_5.setValue(self.nextlist[str(self.pagenum*5+4)+"GP"].grwt)
                self.GP_ntwt_5.setValue(self.nextlist[str(self.pagenum*5+4)+"GP"].ntwt)
                self.GP_Amount_5.setValue(self.nextlist[str(self.pagenum*5+4)+"GP"].amount)

    def GP_Next(self):
        if self.GP_Itemname.text()!='' and self.GP_grwt.value()!=0.0 and self.GP_ntwt.value()!=0.0 and self.GP_Amount!=0:
            self.nextlist[str(self.pagenum*5)+"GP"]=purchase('Gold Purchase', self.GP_Itemname.text(), self.GP_grwt.value(), 
            self.GP_ntwt.value(), self.GP_Amount.value())
        if self.GP_Itemname_2.text()!='' and self.GP_grwt_2.value()!=0.0 and self.GP_ntwt_2.value()!=0.0 and self.GP_Amount_2!=0:
            self.nextlist[str(self.pagenum*5+1)+"GP"]=purchase('Gold Purchase', self.GP_Itemname_2.text(), self.GP_grwt_2.value(), 
            self.GP_ntwt_2.value(), self.GP_Amount_2.value())
        if self.GP_Itemname_3.text()!='' and self.GP_grwt_3.value()!=0.0 and self.GP_ntwt_3.value()!=0.0 and self.GP_Amount_3!=0:
            self.nextlist[str(self.pagenum*5+2)+"GP"]=purchase('Gold Purchase', self.GP_Itemname_3.text(), self.GP_grwt_3.value(), 
            self.GP_ntwt_3.value(), self.GP_Amount_3.value())
        if self.GP_Itemname_4.text()!='' and self.GP_grwt_4.value()!=0.0 and self.GP_ntwt_4.value()!=0.0 and self.GP_Amount_4!=0:
            self.nextlist[str(self.pagenum*5+3)+"GP"]=purchase('Gold Purchase', self.GP_Itemname_4.text(), self.GP_grwt_4.value(), 
            self.GP_ntwt_4.value(), self.GP_Amount_4.value())
        if self.GP_Itemname_5.text()!='' and self.GP_grwt_5.value()!=0.0 and self.GP_ntwt_5.value()!=0.0 and self.GP_Amount_5!=0:
            self.nextlist[str(self.pagenum*5+4)+"GP"]=purchase('Gold Purchase', self.GP_Itemname_5.text(), self.GP_grwt_5.value(), 
            self.GP_ntwt_5.value(), self.GP_Amount_5.value())
        self.pagenum+=1
        self.clearQlineedit()
        if str(self.pagenum*5)+"GP" in self.nextlist.keys():
            self.GP_Itemname.setText(self.nextlist[str(self.pagenum*5)+"GP"].item)
            self.GP_grwt.setValue(self.nextlist[str(self.pagenum*5)+"GP"].grwt)
            self.GP_ntwt.setValue(self.nextlist[str(self.pagenum*5)+"GP"].ntwt)
            self.GP_Amount.setValue(self.nextlist[str(self.pagenum*5)+"GP"].amount)
        if str(self.pagenum*5+1)+"GP" in self.nextlist.keys():
            self.GP_Itemname_2.setText(self.nextlist[str(self.pagenum*5+1)+"GP"].item)
            self.GP_grwt_2.setValue(self.nextlist[str(self.pagenum*5+1)+"GP"].grwt)
            self.GP_ntwt_2.setValue(self.nextlist[str(self.pagenum*5+1)+"GP"].ntwt)
            self.GP_Amount_2.setValue(self.nextlist[str(self.pagenum*5+1)+"GP"].amount)
        if str(self.pagenum*5+2)+"GP" in self.nextlist.keys():
            self.GP_Itemname_3.setText(self.nextlist[str(self.pagenum*5+2)+"GP"].item)
            self.GP_grwt_3.setValue(self.nextlist[str(self.pagenum*5+2)+"GP"].grwt)
            self.GP_ntwt_3.setValue(self.nextlist[str(self.pagenum*5+2)+"GP"].ntwt)
            self.GP_Amount_3.setValue(self.nextlist[str(self.pagenum*5+2)+"GP"].amount)
        if str(self.pagenum*5+3)+"GP" in self.nextlist.keys():
            self.GP_Itemname_4.setText(self.nextlist[str(self.pagenum*5+3)+"GP"].item)
            self.GP_grwt_4.setValue(self.nextlist[str(self.pagenum*5+3)+"GP"].grwt)
            self.GP_ntwt_4.setValue(self.nextlist[str(self.pagenum*5+3)+"GP"].ntwt)
            self.GP_Amount_4.setValue(self.nextlist[str(self.pagenum*5+3)+"GP"].amount)
        if str(self.pagenum*5+4)+"GP" in self.nextlist.keys():
            self.GP_Itemname_5.setText(self.nextlist[str(self.pagenum*5+4)+"GP"].item)
            self.GP_grwt_5.setValue(self.nextlist[str(self.pagenum*5+4)+"GP"].grwt)
            self.GP_ntwt_5.setValue(self.nextlist[str(self.pagenum*5+4)+"GP"].ntwt)
            self.GP_Amount_5.setValue(self.nextlist[str(self.pagenum*5+4)+"GP"].amount)

    def SP_Previous(self):
        if self.pagenum < 1:
            SPPreviousError=QtWidgets.QMessageBox()
            SPPreviousError.setIcon(QMessageBox.Warning)
            SPPreviousError.setWindowTitle("Already on the first page")
            SPPreviousError.setText("As there is no previous page we cannot display it.")
            SPPreviousError.setStandardButtons(QMessageBox.Ok)
            retval=SPPreviousError.exec_()
            return
        else:
            if self.SP_Itemname.text()!='' and self.SP_grwt.value()!=0.0 and self.SP_ntwt.value()!=0.0 and self.SP_Amount!=0:
                self.nextlist[str(self.pagenum*5)+"SP"]=purchase('Silver Purchase', self.SP_Itemname.text(), self.SP_grwt.value(), 
                self.SP_ntwt.value(), self.SP_Amount.value())
            if self.SP_Itemname_2.text()!='' and self.SP_grwt_2.value()!=0.0 and self.SP_ntwt_2.value()!=0.0 and self.SP_Amount_2!=0:
                self.nextlist[str(self.pagenum*5+1)+"SP"]=purchase('Silver Purchase', self.SP_Itemname_2.text(), self.SP_grwt_2.value(), 
                self.SP_ntwt_2.value(), self.SP_Amount_2.value())
            if self.SP_Itemname_3.text()!='' and self.SP_grwt_3.value()!=0.0 and self.SP_ntwt_3.value()!=0.0 and self.SP_Amount_3!=0:
                self.nextlist[str(self.pagenum*5+2)+"SP"]=purchase('Silver Purchase', self.SP_Itemname_3.text(), self.SP_grwt_3.value(), 
                self.SP_ntwt_3.value(), self.SP_Amount_3.value())
            if self.SP_Itemname_4.text()!='' and self.SP_grwt_4.value()!=0.0 and self.SP_ntwt_4.value()!=0.0 and self.SP_Amount_4!=0:
                self.nextlist[str(self.pagenum*5+3)+"SP"]=purchase('Silver Purchase', self.SP_Itemname_4.text(), self.SP_grwt_4.value(), 
                self.SP_ntwt_4.value(), self.SP_Amount_4.value())
            if self.SP_Itemname_5.text()!='' and self.SP_grwt_5.value()!=0.0 and self.SP_ntwt_5.value()!=0.0 and self.SP_Amount_5!=0:
                self.nextlist[str(self.pagenum*5+4)+"SP"]=purchase('Silver Purchase', self.SP_Itemname_5.text(), self.SP_grwt_5.value(), 
                self.SP_ntwt_5.value(), self.SP_Amount_5.value())
            self.pagenum-=1
            self.clearQlineedit()
            if str(self.pagenum*5)+"SP" in self.nextlist.keys():
                self.SP_Itemname.setText(self.nextlist[str(self.pagenum*5)+"SP"].item)
                self.SP_grwt.setValue(self.nextlist[str(self.pagenum*5)+"SP"].grwt)
                self.SP_ntwt.setValue(self.nextlist[str(self.pagenum*5)+"SP"].ntwt)
                self.SP_Amount.setValue(self.nextlist[str(self.pagenum*5)+"SP"].amount)
            if str(self.pagenum*5+1)+"SP" in self.nextlist.keys():
                self.SP_Itemname_2.setText(self.nextlist[str(self.pagenum*5+1)+"SP"].item)
                self.SP_grwt_2.setValue(self.nextlist[str(self.pagenum*5+1)+"SP"].grwt)
                self.SP_ntwt_2.setValue(self.nextlist[str(self.pagenum*5+1)+"SP"].ntwt)
                self.SP_Amount_2.setValue(self.nextlist[str(self.pagenum*5+1)+"SP"].amount)
            if str(self.pagenum*5+2)+"SP" in self.nextlist.keys():
                self.SP_Itemname_3.setText(self.nextlist[str(self.pagenum*5+2)+"SP"].item)
                self.SP_grwt_3.setValue(self.nextlist[str(self.pagenum*5+2)+"SP"].grwt)
                self.SP_ntwt_3.setValue(self.nextlist[str(self.pagenum*5+2)+"SP"].ntwt)
                self.SP_Amount_3.setValue(self.nextlist[str(self.pagenum*5+2)+"SP"].amount)
            if str(self.pagenum*5+3)+"SP" in self.nextlist.keys():
                self.SP_Itemname_4.setText(self.nextlist[str(self.pagenum*5+3)+"SP"].item)
                self.SP_grwt_4.setValue(self.nextlist[str(self.pagenum*5+3)+"SP"].grwt)
                self.SP_ntwt_4.setValue(self.nextlist[str(self.pagenum*5+3)+"SP"].ntwt)
                self.SP_Amount_4.setValue(self.nextlist[str(self.pagenum*5+3)+"SP"].amount)
            if str(self.pagenum*5+4)+"SP" in self.nextlist.keys():
                self.SP_Itemname_5.setText(self.nextlist[str(self.pagenum*5+4)+"SP"].item)
                self.SP_grwt_5.setValue(self.nextlist[str(self.pagenum*5+4)+"SP"].grwt)
                self.SP_ntwt_5.setValue(self.nextlist[str(self.pagenum*5+4)+"SP"].ntwt)
                self.SP_Amount_5.setValue(self.nextlist[str(self.pagenum*5+4)+"SP"].amount)

    def SP_Next(self):
        if self.SP_Itemname.text()!='' and self.SP_grwt.value()!=0.0 and self.SP_ntwt.value()!=0.0 and self.SP_Amount!=0:
            self.nextlist[str(self.pagenum*5)+"SP"]=purchase('Silver Purchase', self.SP_Itemname.text(), self.SP_grwt.value(), 
            self.SP_ntwt.value(), self.SP_Amount.value())
        if self.SP_Itemname_2.text()!='' and self.SP_grwt_2.value()!=0.0 and self.SP_ntwt_2.value()!=0.0 and self.SP_Amount_2!=0:
            self.nextlist[str(self.pagenum*5+1)+"SP"]=purchase('Silver Purchase', self.SP_Itemname_2.text(), self.SP_grwt_2.value(), 
            self.SP_ntwt_2.value(), self.SP_Amount_2.value())
        if self.SP_Itemname_3.text()!='' and self.SP_grwt_3.value()!=0.0 and self.SP_ntwt_3.value()!=0.0 and self.SP_Amount_3!=0:
            self.nextlist[str(self.pagenum*5+2)+"SP"]=purchase('Silver Purchase', self.SP_Itemname_3.text(), self.SP_grwt_3.value(), 
            self.SP_ntwt_3.value(), self.SP_Amount_3.value())
        if self.SP_Itemname_4.text()!='' and self.SP_grwt_4.value()!=0.0 and self.SP_ntwt_4.value()!=0.0 and self.SP_Amount_4!=0:
            self.nextlist[str(self.pagenum*5+3)+"SP"]=purchase('Silver Purchase', self.SP_Itemname_4.text(), self.SP_grwt_4.value(), 
            self.SP_ntwt_4.value(), self.SP_Amount_4.value())
        if self.SP_Itemname_5.text()!='' and self.SP_grwt_5.value()!=0.0 and self.SP_ntwt_5.value()!=0.0 and self.SP_Amount_5!=0:
            self.nextlist[str(self.pagenum*5+4)]=purchase('Silver Purchase', self.SP_Itemname_5.text(), self.SP_grwt_5.value(), 
            self.SP_ntwt_5.value(), self.SP_Amount_5.value())
        self.pagenum+=1
        self.clearQlineedit()
        if str(self.pagenum*5)+"SP" in self.nextlist.keys():
            self.SP_Itemname.setText(self.nextlist[str(self.pagenum*5)+"SP"].item)
            self.SP_grwt.setValue(self.nextlist[str(self.pagenum*5)+"SP"].grwt)
            self.SP_ntwt.setValue(self.nextlist[str(self.pagenum*5)+"SP"].ntwt)
            self.SP_Amount.setValue(self.nextlist[str(self.pagenum*5)+"SP"].amount)
        if str(self.pagenum*5+1)+"SP" in self.nextlist.keys():
            self.SP_Itemname_2.setText(self.nextlist[str(self.pagenum*5+1)+"SP"].item)
            self.SP_grwt_2.setValue(self.nextlist[str(self.pagenum*5+1)+"SP"].grwt)
            self.SP_ntwt_2.setValue(self.nextlist[str(self.pagenum*5+1)+"SP"].ntwt)
            self.SP_Amount_2.setValue(self.nextlist[str(self.pagenum*5+1)+"SP"].amount)
        if str(self.pagenum*5+2)+"SP" in self.nextlist.keys():
            self.SP_Itemname_3.setText(self.nextlist[str(self.pagenum*5+2)+"SP"].item)
            self.SP_grwt_3.setValue(self.nextlist[str(self.pagenum*5+2)+"SP"].grwt)
            self.SP_ntwt_3.setValue(self.nextlist[str(self.pagenum*5+2)+"SP"].ntwt)
            self.SP_Amount_3.setValue(self.nextlist[str(self.pagenum*5+2)+"SP"].amount)
        if str(self.pagenum*5+3)+"SP" in self.nextlist.keys():
            self.SP_Itemname_4.setText(self.nextlist[str(self.pagenum*5+3)+"SP"].item)
            self.SP_grwt_4.setValue(self.nextlist[str(self.pagenum*5+3)+"SP"].grwt)
            self.SP_ntwt_4.setValue(self.nextlist[str(self.pagenum*5+3)+"SP"].ntwt)
            self.SP_Amount_4.setValue(self.nextlist[str(self.pagenum*5+3)+"SP"].amount)
        if str(self.pagenum*5+4)+"SP" in self.nextlist.keys():
            self.SP_Itemname_5.setText(self.nextlist[str(self.pagenum*5+4)+"SP"].item)
            self.SP_grwt_5.setValue(self.nextlist[str(self.pagenum*5+4)+"SP"].grwt)
            self.SP_ntwt_5.setValue(self.nextlist[str(self.pagenum*5+4)+"SP"].ntwt)
            self.SP_Amount_5.setValue(self.nextlist[str(self.pagenum*5+4)+"SP"].amount)

    def clearQlineedit(self):
        GolddictText={}
        GolddictText[0]=self.Gold_itemname
        GolddictText[1]=self.Gold_itemname_2
        GolddictText[2]=self.Gold_itemname_3
        GolddictText[3]=self.Gold_itemname_4
        GolddictText[4]=self.Gold_itemname_5
        GolddictText[5]=self.Gold_Itemid 
        GolddictText[6]=self.Gold_Itemid_2
        GolddictText[7]=self.Gold_Itemid_3
        GolddictText[8]=self.Gold_Itemid_4
        GolddictText[9]=self.Gold_Itemid_5
        GolddictText[10]=self.Gold_purity
        GolddictText[11]=self.Gold_purity_2
        GolddictText[12]=self.Gold_purity_3
        GolddictText[13]=self.Gold_purity_4
        GolddictText[14]=self.Gold_purity_5
        GolddictText[15]=self.Gold_grwt
        GolddictText[16]=self.Gold_grwt_2
        GolddictText[17]=self.Gold_grwt_3
        GolddictText[18]=self.Gold_grwt_4
        GolddictText[19]=self.Gold_grwt_5
        GolddictText[20]=self.Gold_ntwt
        GolddictText[21]=self.Gold_ntwt_2
        GolddictText[22]=self.Gold_ntwt_3
        GolddictText[23]=self.Gold_ntwt_4
        GolddictText[24]=self.Gold_ntwt_5
        GolddictText[25]=self.Gold_BillAmount
        GolddictText[26]=self.Gold_BillAmount_2
        GolddictText[27]=self.Gold_BillAmount_3
        GolddictText[28]=self.Gold_BillAmount_4
        GolddictText[29]=self.Gold_BillAmount_5
        GolddictText[30]=self.Gold_total

        SilverdictText={}
        SilverdictText[0]=self.Silver_itemname
        SilverdictText[1]=self.Silver_itemname_2
        SilverdictText[2]=self.Silver_itemname_3
        SilverdictText[3]=self.Silver_itemname_4
        SilverdictText[4]=self.Silver_itemname_5
        SilverdictText[5]=self.Silver_Itemid 
        SilverdictText[6]=self.Silver_Itemid_2
        SilverdictText[7]=self.Silver_Itemid_3
        SilverdictText[8]=self.Silver_Itemid_4
        SilverdictText[9]=self.Silver_Itemid_5
        SilverdictText[10]=self.Silver_purity
        SilverdictText[11]=self.Silver_purity_2
        SilverdictText[12]=self.Silver_purity_3
        SilverdictText[13]=self.Silver_purity_4
        SilverdictText[14]=self.Silver_purity_5
        SilverdictText[15]=self.Silver_grwt
        SilverdictText[16]=self.Silver_grwt_2
        SilverdictText[17]=self.Silver_grwt_3
        SilverdictText[18]=self.Silver_grwt_4
        SilverdictText[19]=self.Silver_grwt_5
        SilverdictText[20]=self.Silver_ntwt
        SilverdictText[21]=self.Silver_ntwt_2
        SilverdictText[22]=self.Silver_ntwt_3
        SilverdictText[23]=self.Silver_ntwt_4
        SilverdictText[24]=self.Silver_ntwt_5
        SilverdictText[25]=self.Silver_BillAmount
        SilverdictText[26]=self.Silver_BillAmount_2
        SilverdictText[27]=self.Silver_BillAmount_3
        SilverdictText[28]=self.Silver_BillAmount_4
        SilverdictText[29]=self.Silver_BillAmount_5
        SilverdictText[30]=self.Silver_total

        OOdictText={}
        OOdictText[0]=self.Old_Order_Deposit
        OOdictText[1]=self.Old_Order_Amount
        OOdictText[2]=self.Old_Order_Amount_2
        OOdictText[3]=self.Old_Order_Amount_3
        OOdictText[4]=self.Old_Order_Amount_4
        OOdictText[5]=self.Old_Order_Amount_5
        OOdictText[6]=self.Old_Order_Itemname
        OOdictText[7]=self.Old_Order_Itemname_2
        OOdictText[8]=self.Old_Order_Itemname_3
        OOdictText[9]=self.Old_Order_Itemname_4
        OOdictText[10]=self.Old_Order_Itemname_5
        OOdictText[11]=self.Old_Order_grwt
        OOdictText[12]=self.Old_Order_grwt_2
        OOdictText[13]=self.Old_Order_grwt_3
        OOdictText[14]=self.Old_Order_grwt_4
        OOdictText[15]=self.Old_Order_grwt_5
        OOdictText[16]=self.Old_Order_ntwt
        OOdictText[17]=self.Old_Order_ntwt_2
        OOdictText[18]=self.Old_Order_ntwt_3
        OOdictText[19]=self.Old_Order_ntwt_4
        OOdictText[20]=self.Old_Order_ntwt_5
        OOdictText[21]=self.Old_Order_Total
        OOdictText[22]=self.Old_Order_Deposit

        NOdictText={}
        NOdictText[0]=self.New_Order_EstAmount
        NOdictText[1]=self.New_Order_EstAmount_2
        NOdictText[2]=self.New_Order_EstAmount_3
        NOdictText[3]=self.New_Order_EstAmount_4
        NOdictText[4]=self.New_Order_EstAmount_5
        NOdictText[5]=self.New_Order_Adv
        NOdictText[6]=self.New_Order_Adv_2
        NOdictText[7]=self.New_Order_Adv_3
        NOdictText[8]=self.New_Order_Adv_4
        NOdictText[9]=self.New_Order_Adv_5
        NOdictText[10]=self.New_Order_Itemname
        NOdictText[11]=self.New_Order_Itemname_2
        NOdictText[12]=self.New_Order_Itemname_3
        NOdictText[13]=self.New_Order_Itemname_4
        NOdictText[14]=self.New_Order_Itemname_5
        NOdictText[15]=self.New_Order_grwt
        NOdictText[16]=self.New_Order_grwt_2
        NOdictText[17]=self.New_Order_grwt_3
        NOdictText[18]=self.New_Order_grwt_4
        NOdictText[19]=self.New_Order_grwt_5
        NOdictText[20]=self.New_Order_ntwt
        NOdictText[21]=self.New_Order_ntwt_2
        NOdictText[22]=self.New_Order_ntwt_3
        NOdictText[23]=self.New_Order_ntwt_4
        NOdictText[24]=self.New_Order_ntwt_5
        NOdictText[25]=self.New_Order_total
        

        ShreedictText={}
        ShreedictText[0]=self.Shree_name
        ShreedictText[1]=self.Shree_amount

        VCdictText={}
        VCdictText[0]=self.VC_Itemname
        VCdictText[1]=self.VC_Itemname_2
        VCdictText[2]=self.VC_Itemname_3
        VCdictText[3]=self.VC_Itemname_4
        VCdictText[4]=self.VC_Itemname_5
        VCdictText[5]=self.VC_Amount
        VCdictText[6]=self.VC_Amount_2
        VCdictText[7]=self.VC_Amount_3
        VCdictText[8]=self.VC_Amount_4
        VCdictText[9]=self.VC_Amount_5
        VCdictText[10]=self.VC_Amount_6
        VCdictText[11]=self.VC_grwt
        VCdictText[12]=self.VC_grwt_2
        VCdictText[13]=self.VC_grwt_3
        VCdictText[14]=self.VC_grwt_4
        VCdictText[15]=self.VC_grwt_5
        VCdictText[16]=self.VC_ntwt
        VCdictText[17]=self.VC_ntwt_2
        VCdictText[18]=self.VC_ntwt_3
        VCdictText[19]=self.VC_ntwt_4
        VCdictText[20]=self.VC_ntwt_5
        VCdictText[21]=self.VC_total

        GPdictText={}
        GPdictText[0]=self.GP_Itemname
        GPdictText[1]=self.GP_Itemname_2
        GPdictText[2]=self.GP_Itemname_3
        GPdictText[3]=self.GP_Itemname_4
        GPdictText[4]=self.GP_Itemname_5
        GPdictText[5]=self.GP_grwt
        GPdictText[6]=self.GP_grwt_2
        GPdictText[7]=self.GP_grwt_3
        GPdictText[8]=self.GP_grwt_4
        GPdictText[9]=self.GP_grwt_5
        GPdictText[10]=self.GP_ntwt
        GPdictText[11]=self.GP_ntwt_2
        GPdictText[12]=self.GP_ntwt_3
        GPdictText[13]=self.GP_ntwt_4
        GPdictText[14]=self.GP_ntwt_5
        GPdictText[15]=self.GP_Amount
        GPdictText[16]=self.GP_Amount_2
        GPdictText[17]=self.GP_Amount_3
        GPdictText[18]=self.GP_Amount_4
        GPdictText[19]=self.GP_Amount_5
        GPdictText[20]=self.GP_total

        SPdictText={}
        SPdictText[0]=self.SP_Itemname
        SPdictText[1]=self.SP_Itemname_2
        SPdictText[2]=self.SP_Itemname_3
        SPdictText[3]=self.SP_Itemname_4
        SPdictText[4]=self.SP_Itemname_5
        SPdictText[5]=self.SP_grwt
        SPdictText[6]=self.SP_grwt_2
        SPdictText[7]=self.SP_grwt_3
        SPdictText[8]=self.SP_grwt_4
        SPdictText[9]=self.SP_grwt_5
        SPdictText[10]=self.SP_ntwt
        SPdictText[11]=self.SP_ntwt_2
        SPdictText[12]=self.SP_ntwt_3
        SPdictText[13]=self.SP_ntwt_4
        SPdictText[14]=self.SP_ntwt_5
        SPdictText[15]=self.SP_Amount
        SPdictText[16]=self.SP_Amount_2
        SPdictText[17]=self.SP_Amount_3
        SPdictText[18]=self.SP_Amount_4
        SPdictText[19]=self.SP_Amount_5
        SPdictText[20]=self.SP_total

        if self.stackedWidget.currentIndex() ==1:
            for key in GolddictText.keys():
                try:
                    GolddictText[key].setValue(0)
                except:
                    GolddictText[key].clear()
            print('Gold')
        elif self.stackedWidget.currentIndex() ==2:
            print('Silver')
            for key in SilverdictText.keys():
                try:
                    SilverdictText[key].setValue(0)
                except:
                    SilverdictText[key].clear()
        elif self.stackedWidget.currentIndex() == 3:
            print('OO')
            for key in OOdictText.keys():
                try:
                    OOdictText[key].setValue(0)
                except:
                    OOdictText[key].clear
        elif self.stackedWidget.currentIndex() == 4:
            print('NO')
            for key in NOdictText.keys():
                try:
                    NOdictText[key].setValue(0)
                except:
                    NOdictText[key].clear
        elif self.stackedWidget.currentIndex() == 5:
            print('Misc')
            for key in ShreedictText.keys():
                try:
                    ShreedictText[key].setValue(0)
                except:
                    ShreedictText[key].clear
        elif self.stackedWidget.currentIndex() == 6:
            print('VC')
            for key in VCdictText.keys():
                try:
                    VCdictText[key].setValue(0)
                except:
                    VCdictText[key].clear
        elif self.stackedWidget.currentIndex() == 7:
            print('GP')
            for key in GPdictText.keys():
                try:
                    GPdictText[key].setValue(0)
                except:
                    GPdictText[key].clear()
        elif self.stackedWidget.currentIndex() == 8:
            print('SP')
            for key in SPdictText.keys():
                try:
                    SPdictText[key].setValue(0)
                except:
                    SPdictText[key].clear

    def Radioclear(self):
        Radiodict={}
        Radiodict[0]=self.Gold_Cardmachine
        Radiodict[1]=self.Gold_Cardmachine_2
        Radiodict[2]=self.Gold_Cardmachine_3
        Radiodict[3]=self.Gold_Cardmachine_4
        Radiodict[4]=self.UPI_BharatPe
        Radiodict[5]=self.UPI_BharatPe_2
        Radiodict[6]=self.UPI_BharatPe_3
        Radiodict[7]=self.UPI_BharatPe_4
        Radiodict[8]=self.UPI_BharatPe_5
        Radiodict[9]=self.UPI_GPay
        Radiodict[10]=self.UPI_GPay_2
        Radiodict[11]=self.UPI_GPay_3
        Radiodict[12]=self.UPI_GPay_4
        Radiodict[13]=self.UPI_GPay_5
        Radiodict[14]=self.UPI_Other
        Radiodict[15]=self.UPI_Other_2
        Radiodict[16]=self.UPI_Other_3
        Radiodict[17]=self.UPI_Other_4
        Radiodict[18]=self.UPI_Other_5
        Radiodict[19]=self.Silver_Cardmachine
        Radiodict[20]=self.Silver_Cardmachine_2
        Radiodict[21]=self.Silver_Cardmachine_3
        Radiodict[22]=self.Silver_Cardmachine_4
        Radiodict[23]=self.Old_Order_Cardmachine
        Radiodict[24]=self.Old_Order_Cardmachine_2
        Radiodict[25]=self.Old_Order_Cardmachine_3
        Radiodict[26]=self.Old_Order_Cardmachine_4
        Radiodict[27]=self.New_Order_Cardmachine
        Radiodict[28]=self.New_Order_Cardmachine_2
        Radiodict[29]=self.New_Order_Cardmachine_3
        Radiodict[30]=self.New_Order_Cardmachine_4
        Radiodict[31]=self.Shree_plus
        Radiodict[32]=self.Shree_minus
        Radiodict[33]=self.Old_Order_Sale
        Radiodict[34]=self.New_Order_Goods
        Radiodict[35]=self.VC_Saleconvert
        Radiodict[36]=self.VC_Cardmachine
        Radiodict[37]=self.VC_Cardmachine_2
        Radiodict[38]=self.VC_Cardmachine_3
        Radiodict[39]=self.VC_Cardmachine_4
        Radiodict[40]=self.GP_Cash
        Radiodict[41]=self.GP_Cheque
        Radiodict[42]=self.GP_Other
        Radiodict[43]=self.SP_Cash
        Radiodict[44]=self.SP_Cheque
        Radiodict[45]=self.SP_Other
        for key in Radiodict.keys():
            Radiodict[key].setChecked(False)

    def submitclear(self):
        Subclear={}
        Subclear[0]=self.Gold_custname
        Subclear[1]=self.Gold_phnumber
        Subclear[2]=self.Silver_custname
        Subclear[3]=self.Silver_phnumber
        Subclear[4]=self.Old_OrderName
        Subclear[5]=self.Old_Order_phnum
        Subclear[6]=self.New_Order_Name
        Subclear[7]=self.New_Order_phnum
        Subclear[8]=self.Shree_name
        Subclear[9]=self.Shree_amount
        Subclear[10]=self.VC_name
        Subclear[11]=self.VC_phnum
        Subclear[12]=self.GP_Name
        Subclear[13]=self.GP_phnum
        Subclear[14]=self.SP_Name
        Subclear[15]=self.SP_phnum
        Subclear[16]=self.Expense_name
        Subclear[17]=self.Expense_amount
        Subclear[18]=self.Cash
        Subclear[19]=self.Cash_2
        Subclear[20]=self.Cash_3
        Subclear[21]=self.Cash_4
        Subclear[22]=self.Cash_5
        Subclear[23]=self.Cash_6
        Subclear[24]=self.Cash_7
        Subclear[25]=self.Card
        Subclear[26]=self.Card_2
        Subclear[27]=self.Card_3
        Subclear[28]=self.Card_4
        Subclear[29]=self.Card_5
        Subclear[30]=self.UPI
        Subclear[31]=self.UPI_2
        Subclear[32]=self.UPI_3
        Subclear[33]=self.UPI_4
        Subclear[34]=self.UPI_5
        Subclear[35]=self.Cheque
        Subclear[36]=self.Cheque_2
        Subclear[37]=self.Cheque_3
        Subclear[38]=self.Cheque_4
        Subclear[39]=self.Cheque_5
        Subclear[40]=self.Cheque_6
        Subclear[41]=self.Cheque_7
        Subclear[42]=self.ChequeNo
        Subclear[43]=self.ChequeNo_2
        Subclear[44]=self.ChequeNo_3
        Subclear[45]=self.ChequeNo_4
        Subclear[46]=self.ChequeNo_5
        Subclear[47]=self.ChequeNo_6
        Subclear[48]=self.ChequeNo_7
        Subclear[49]=self.URDitemname
        Subclear[50]=self.URDitemname_2
        Subclear[51]=self.URDitemname_3
        Subclear[52]=self.URDitemname_4
        Subclear[53]=self.URDitemname_5
        Subclear[54]=self.URD_grwt
        Subclear[55]=self.URD_grwt_2
        Subclear[56]=self.URD_grwt_3
        Subclear[57]=self.URD_grwt_4
        Subclear[58]=self.URD_grwt_5
        Subclear[59]=self.URD_ntwt
        Subclear[60]=self.URD_ntwt_2
        Subclear[61]=self.URD_ntwt_3
        Subclear[62]=self.URD_ntwt_4
        Subclear[63]=self.URD_ntwt_5
        Subclear[64]=self.URDAmount
        Subclear[65]=self.URDAmount_2
        Subclear[66]=self.URDAmount_3
        Subclear[67]=self.URDAmount_4
        Subclear[68]=self.URDAmount_5
        Subclear[69]=self.DebtAmount
        Subclear[70]=self.DebtAmount_2
        Subclear[71]=self.DebtAmount_3
        Subclear[72]=self.DebtAmount_4
        Subclear[73]=self.DebtAmount_5

        for key in Subclear.keys():
            try:
                Subclear[key].setValue(0)
            except:
                Subclear[key].clear()

    def GoldSell_withmessage(self):
        if self.Gold_itemname.text() != '' and self.Gold_Itemid.value()!=0 and self.Gold_purity.text() != '' and self.Gold_grwt.value() != 0.000 and self.Gold_ntwt.value() != 0.000 and self.Gold_BillAmount.value() != 0:
            self.nextlist[str(self.pagenum*5)+"GS"]=((GoldSell(self.Gold_custname.text(), self.Gold_phnumber.text(), self.Gold_itemname.text(), self.Gold_Itemid.value(), self.Gold_grwt.value(), self.Gold_ntwt.value(), self.Gold_BillAmount.value(), self.Gold_purity.text(), date.today())))
        if self.Gold_itemname_2.text() != '' and self.Gold_Itemid_2.value()!=0 and self.Gold_purity_2.text() != '' and self.Gold_grwt_2.value() != 0.000 and self.Gold_ntwt_2.value() != 0.000 and self.Gold_BillAmount.value() != 0:
            self.nextlist[str(self.pagenum*5+1)+"GS"]=(GoldSell(self.Gold_custname.text(), self.Gold_phnumber.text(), self.Gold_itemname_2.text(), self.Gold_Itemid_2.value(), self.Gold_grwt_2.value(), self.Gold_ntwt_2.value(), self.Gold_BillAmount_2.value(), self.Gold_purity_2.text(), date.today()))        
        if self.Gold_itemname_3.text() != '' and self.Gold_Itemid_3.value()!=0 and self.Gold_purity_3.text() != '' and self.Gold_grwt_3.value() != 0.000 and self.Gold_ntwt_3.value() != 0.000 and self.Gold_BillAmount_3.value() != 0:
            self.nextlist[str(self.pagenum*5+2)+"GS"]=(GoldSell(self.Gold_custname.text(), self.Gold_phnumber.text(), self.Gold_itemname_3.text(), self.Gold_Itemid_3.value(), self.Gold_grwt_3.value(), self.Gold_ntwt_3.value(), self.Gold_BillAmount_3.value(), self.Gold_purity_3.text(), date.today()))
        if self.Gold_itemname_4.text() != '' and self.Gold_Itemid_4.value()!=0 and self.Gold_purity_4.text() != '' and self.Gold_grwt_4.value() != 0.000 and self.Gold_ntwt_4.value() != 0.000 and self.Gold_BillAmount_4.value() != 0:
            self.nextlist[str(self.pagenum*5+3)+"GS"]=(GoldSell(self.Gold_custname.text(), self.Gold_phnumber.text(), self.Gold_itemname_4.text(), self.Gold_Itemid_4.value(), self.Gold_grwt_4.value(), self.Gold_ntwt_4.value(), self.Gold_BillAmount_4.value(), self.Gold_purity_4.text(), date.today()))
        if self.Gold_itemname_5.text() != '' and self.Gold_Itemid_5.value()!=0 and self.Gold_purity_5.text() != '' and self.Gold_grwt_5.value() != 0.000 and self.Gold_ntwt_5.value() != 0.000 and self.Gold_BillAmount_5.value() != 0:
            self.nextlist[str(self.pagenum*5+4)+"GS"]=(GoldSell(self.Gold_custname.text(), self.Gold_phnumber.text(), self.Gold_itemname_5.text(), self.Gold_Itemid_5.value(), self.Gold_grwt_5.value(), self.Gold_ntwt_5.value(), self.Gold_BillAmount_5.value(), self.Gold_purity_5.text(), date.today()))
        temp_cname=self.Gold_custname.text()
        if self.checkBox.isChecked(): temp_cname+=" (adj)"
        temp_items_name=''
        temp_items_id=''
        temp_purity=''
        temp_grwt=float(0)
        temp_ntwt=float(0)
        temp_cardmachine=None
        temp_UPItype=None
        if self.GoldCardgroup.checkedButton()!=None:
            temp_cardmachine=self.GoldCardgroup.checkedButton().text()
        if self.GoldUPIgroup.checkedButton()!=None:
            temp_UPItype=self.GoldUPIgroup.checkedButton().text()
        
        for key in self.nextlist.keys():
            if "GS" in key:
                temp_items_name =', '.join([temp_items_name, self.nextlist[key].pr_name])
                temp_items_id = ', '.join([temp_items_id, str(self.nextlist[key].id)])
                temp_purity = ', '.join([temp_purity, self.nextlist[key].purity])
                temp_grwt+=self.nextlist[key].gr_wt
                temp_ntwt+=self.nextlist[key].nt_wt
        temp_items_name=temp_items_name[2:]
        temp_items_id=temp_items_id[2:]
        temp_purity=temp_purity[2:]

        if self.ui.URDpass==[]:
            if self.comboBox.currentText()=='G':
                URDlist=[self.URDAmount.value() ,self.URDitemname.text(), self.URD_grwt.value(), self.URD_ntwt.value(), 0.0, 0.0]
            else:
                URDlist=[self.URDAmount_2.value() ,self.URDitemname.text(), 0.0, 0.0, self.URD_grwt.value(), self.URD_ntwt.value()]
        else:
            URDlist=self.ui.URDpass
        temp_items_name=temp_items_name[2:]
        temp_items_id=temp_items_id[2:]
        temp_purity=temp_purity[2:]
        Bill_store(Bill(temp_cname, self.Gold_phnumber.text(), temp_items_name, temp_items_id, temp_purity, temp_grwt, 
                    temp_ntwt, 0.000, 0.000, 'Gold Sale', self.Gold_total.value(), self.Cash.value(), self.Card.value(), temp_cardmachine, 
                    self.UPI.value(), temp_UPItype, self.Cheque.value(), self.ChequeNo.text(), self.DebtAmount.value(), URDlist[0], 
                    URDlist[1], URDlist[2], URDlist[3], URDlist[4], URDlist[5], 0, '', date.today()), self.nextlist)

        self.clearQlineedit()
        self.Radioclear()
        self.submitclear()
        self.nextlist.clear()
        Goldconfirm=QtWidgets.QMessageBox()
        Goldconfirm.setIcon(QMessageBox.Information)
        Goldconfirm.setWindowTitle("Confirmation of Data Entry")
        Goldconfirm.setText("The Gold Sale details have been entered")
        Goldconfirm.setStandardButtons(QMessageBox.Ok)
        retval=Goldconfirm.exec_()

    def SilverSell_withmessage(self):
        if self.Silver_itemname.text() != '' and self.Silver_purity.text() != '' and self.Silver_grwt.value() != 0.000 and self.Silver_ntwt.value() != 0.000 and self.Silver_BillAmount.value() != 0:
            self.nextlist[str(self.pagenum*5)+"SS"]=((SilverSell(self.Silver_custname.text(), self.Silver_phnumber.text(), self.Silver_itemname.text(), self.Silver_Itemid.value(), self.Silver_grwt.value(), self.Silver_ntwt.value(), self.Silver_BillAmount.value(), self.Silver_purity.text(), date.today())))
        if self.Silver_itemname_2.text() != '' and self.Silver_purity_2.text() != '' and self.Silver_grwt_2.value() != 0.000 and self.Silver_ntwt_2.value() != 0.000 and self.Silver_BillAmount.value() != 0:
            self.nextlist[str(self.pagenum*5+1)+"SS"]=(SilverSell(self.Silver_custname.text(), self.Silver_phnumber.text(), self.Silver_itemname_2.text(), self.Silver_Itemid_2.value(), self.Silver_grwt_2.value(), self.Silver_ntwt_2.value(), self.Silver_BillAmount_2.value(), self.Silver_purity_2.text(), date.today()))        
        if self.Silver_itemname_3.text() != '' and self.Silver_purity_3.text() != '' and self.Silver_grwt_3.value() != 0.000 and self.Silver_ntwt_3.value() != 0.000 and self.Silver_BillAmount_3.value() != 0:
            self.nextlist[str(self.pagenum*5+2)+"SS"]=(SilverSell(self.Silver_custname.text(), self.Silver_phnumber.text(), self.Silver_itemname_3.text(), self.Silver_Itemid_3.value(), self.Silver_grwt_3.value(), self.Silver_ntwt_3.value(), self.Silver_BillAmount_3.value(), self.Silver_purity_3.text(), date.today()))
        if self.Silver_itemname_4.text() != '' and self.Silver_purity_4.text() != '' and self.Silver_grwt_4.value() != 0.000 and self.Silver_ntwt_4.value() != 0.000 and self.Silver_BillAmount_4.value() != 0:
            self.nextlist[str(self.pagenum*5+3)+"SS"]=(SilverSell(self.Silver_custname.text(), self.Silver_phnumber.text(), self.Silver_itemname_4.text(), self.Silver_Itemid_4.value(), self.Silver_grwt_4.value(), self.Silver_ntwt_4.value(), self.Silver_BillAmount_4.value(), self.Silver_purity_4.text(), date.today()))
        if self.Silver_itemname_5.text() != '' and self.Silver_purity_5.text() != '' and self.Silver_grwt_5.value() != 0.000 and self.Silver_ntwt_5.value() != 0.000 and self.Silver_BillAmount_5.value() != 0:
            self.nextlist[str(self.pagenum*5+4)+"SS"]=(SilverSell(self.Silver_custname.text(), self.Silver_phnumber.text(), self.Silver_itemname_5.text(), self.Silver_Itemid_5.value(), self.Silver_grwt_5.value(), self.Silver_ntwt_5.value(), self.Silver_BillAmount_5.value(), self.Silver_purity_5.text(), date.today()))
        temp_cname=self.Silver_custname.text()
        if self.checkBox_2.isChecked(): temp_cname+=" (adj)"
        temp_items_name=''
        temp_items_id=''
        temp_purity=''
        temp_grwt=float(0)
        temp_ntwt=float(0)
        temp_cardmachine=None
        temp_UPItype=None
        if self.SilverCardgroup.checkedButton()!=None:
            temp_cardmachine=self.SilverCardgroup.checkedButton().text()
        if self.SilverUPIgroup.checkedButton()!=None:
            temp_UPItype=self.SilverUPIgroup.checkedButton().text()

        for key in self.nextlist.keys():
            if "SS" in key:
                temp_items_name =', '.join([temp_items_name,self.nextlist[key].pr_name])
                temp_items_id = ', '.join([temp_items_id, str(self.nextlist[key].id)])
                temp_purity = ', '.join([temp_purity, self.nextlist[key].purity])
                temp_grwt+=self.nextlist[key].gr_wt
                temp_ntwt+=self.nextlist[key].nt_wt
        temp_items_name=temp_items_name[2:]
        temp_items_id=temp_items_id[2:]
        temp_purity=temp_purity[2:]
        if self.ui.URDpass==[]:
            if self.comboBox_2.currentText()=='G':
                URDlist=[self.URDitemname.text(), self.URD_grwt.value(), self.URD_ntwt.value(), 0.0, 0.0]
            else:
                URDlist=[self.URDitemname.text(), 0.0, 0.0, self.URD_grwt.value(), self.URD_ntwt.value()]
        else:
            URDlist=self.ui.URDpass
        Bill_store(Bill(temp_cname ,self.Silver_phnumber.text(), temp_items_name, str(temp_items_id), temp_purity, 0.000, 0.000, 
                    temp_grwt, temp_ntwt,'Silver Sale', self.Silver_total.value(), self.Cash.value(), self.Card.value(), temp_cardmachine, self.UPI.value(),
                    temp_UPItype, self.Cheque.value(), self.ChequeNo.text(), self.DebtAmount.value(), self.URDAmount.value(), URDlist[0],
                    URDlist[1], URDlist[2], URDlist[3], URDlist[4], 0, '', date.today()), self.nextlist)
        self.clearQlineedit()
        self.Radioclear()
        self.submitclear()
        self.nextlist.clear()
        Silverconfirm=QtWidgets.QMessageBox()
        Silverconfirm.setIcon(QMessageBox.Information)
        Silverconfirm.setWindowTitle("Confirmation of Data Entry")
        Silverconfirm.setText("The Silver Sale details have been entered")
        Silverconfirm.setStandardButtons(QMessageBox.Ok)
        retval=Silverconfirm.exec_()

    def Old_Order_submit(self):
        temp_cardmachine=None
        temp_UPItype=None
        temp_cname=self.Old_OrderName.text()
        if self.checkBox_3.isChecked(): temp_cname+=' (adj)'
        if self.OOCardgroup.checkedButton()!=None:
            temp_cardmachine=self.OOCardgroup.checkedButton().text()
        if self.OOUPIgroup.checkedButton()!=None:
            temp_UPItype=self.OOUPIgroup.checkedButton().text()

        if self.Old_Order_Sale.isChecked():
            if self.Old_Order_Amount.value()!=0 and self.Old_Order_Itemname.text()!='' and self.Old_Order_grwt.value()!=0.000 and self.Old_Order_ntwt.value()!=0.000:
                self.nextlist[str(self.pagenum*5)+"OO"]=OldOrder(self.Old_Order_GS.currentText(), self.Old_Order_Itemname.text(),
                                                            self.Old_Order_Amount.value(), self.Old_Order_grwt.value(),
                                                            self.Old_Order_ntwt.value())
            if self.Old_Order_Amount_2.value()!=0 and self.Old_Order_Itemname_2.text()!='' and self.Old_Order_grwt_2.value()!=0.000 and self.Old_Order_ntwt_2.value()!=0.000:
                self.nextlist[str(self.pagenum*5+1)+"OO"]=OldOrder(self.Old_Order_GS_2.currentText(), self.Old_Order_Itemname_2.text(),
                                                            self.Old_Order_Amount_2.value(), self.Old_Order_grwt_2.value(),
                                                            self.Old_Order_ntwt_2.value())
            if self.Old_Order_Amount_3.value()!=0 and self.Old_Order_Itemname_3.text()!='' and self.Old_Order_grwt_3.value()!=0.000 and self.Old_Order_ntwt_3.value()!=0.000:
                self.nextlist[str(self.pagenum*5+2)+"OO"]=OldOrder(self.Old_Order_GS_3.currentText(), self.Old_Order_Itemname_3.text(),
                                                            self.Old_Order_Amount_3.value(), self.Old_Order_grwt_3.value(),
                                                            self.Old_Order_ntwt_3.value())
            if self.Old_Order_Amount_4.value()!=0 and self.Old_Order_Itemname_4.text()!='' and self.Old_Order_grwt_4.value()!=0.000 and self.Old_Order_ntwt_4.value()!=0.000:
                self.nextlist[str(self.pagenum*5+3)+"OO"]=OldOrder(self.Old_Order_GS_4.currentText(), self.Old_Order_Itemname_4.text(),
                                                            self.Old_Order_Amount_4.value(), self.Old_Order_grwt_4.value(),
                                                            self.Old_Order_ntwt_4.value())
            if self.Old_Order_Amount_5.value()!=0 and self.Old_Order_Itemname_5.text()!='' and self.Old_Order_grwt_5.value()!=0.000 and self.Old_Order_ntwt_5.value()!=0.000:
                self.nextlist[str(self.pagenum*5+4)+"OO"]=OldOrder(self.Old_Order_GS_5.currentText(), self.Old_Order_Itemname_5.text(),
                                                            self.Old_Order_Amount_5.value(), self.Old_Order_grwt_5.value(),
                                                            self.Old_Order_ntwt_5.value())
            temp_items_name=''
            temp_goldgrwt=float(0)
            temp_goldntwt=float(0)
            temp_silvergrwt=float(0)
            temp_silverntwt=float(0)
            for key in self.nextlist.keys():
                if "OO" in key:
                    temp_items_name=', '.join([str(temp_items_name), self.nextlist[key].item])
                    if self.nextlist[key].type == 'G':
                        temp_goldgrwt+=self.nextlist[key].grwt
                        temp_goldntwt+=self.nextlist[key].ntwt
                    else:
                        temp_silvergrwt+=self.nextlist[key].grwt
                        temp_silverntwt+=self.nextlist[key].ntwt
            temp_items_name=temp_items_name[2:]
            if self.ui.URDpass==[]:
                if self.comboBox_3.currentText()=='G':
                    URDlist=[self.URDitemname.text(), self.URD_grwt.value(), self.URD_ntwt.value(), 0.0, 0.0]
                else:
                    URDlist=[self.URDitemname.text(), 0.0, 0.0, self.URD_grwt.value(), self.URD_ntwt.value()]
            else:
                URDlist=self.ui.URDpass

            Bill_store(Bill(temp_cname , self.Old_Order_phnum.text(), temp_items_name, '', '', temp_goldgrwt, temp_goldntwt,
                        temp_silvergrwt, temp_silverntwt, 'Old Order', self.Old_Order_Total.value(), self.Cash_3.value(), self.Card_3.value(), 
                        temp_cardmachine, self.UPI_3.value(), temp_UPItype, self.Cheque_3.value(), self.ChequeNo_3.text(),
                        self.DebtAmount_3.value(), self.URDAmount_3.value(), URDlist[0], URDlist[1], URDlist[2], URDlist[3],
                        URDlist[4], 0, '', date.today()), self.nextlist)
        else:
            if self.ui.URDpass==[]:
                if self.comboBox_3.currentText()=='G':
                    URDlist=[self.URDitemname.text(), self.URD_grwt.value(), self.URD_ntwt.value(), 0.0, 0.0]
                else:
                    URDlist=[self.URDitemname.text(), 0.0, 0.0, self.URD_grwt.value(), self.URD_ntwt.value()]
            else:
                URDlist=self.ui.URDpass

            Bill_store(Bill(temp_cname ,self.Old_Order_phnum.text(), '', '', '', 0.000, 0.000, 0.000, 0.000, 'Old Order', 
                            self.Old_Order_Deposit.value(), self.Cash_3.value(),self.Card_3.value(), temp_cardmachine, 
                            self.UPI_3.value(), temp_UPItype, self.Cheque_3.value(),self.ChequeNo_3.text(), self.DebtAmount_3.value(), 
                            self.URDAmount_3.value(), URDlist[0], URDlist[1], URDlist[2], URDlist[3], URDlist[4], 0, '', date.today()), self.nextlist)
        self.clearQlineedit()
        self.nextlist.clear()
        self.Radioclear()
        self.submitclear()
        OOconfirm=QtWidgets.QMessageBox()
        OOconfirm.setIcon(QMessageBox.Information)
        OOconfirm.setWindowTitle("Confirmation of Data Entry")
        OOconfirm.setText("The Old Order details have been entered")
        OOconfirm.setStandardButtons(QMessageBox.Ok)
        retval=OOconfirm.exec_()
    
    def New_Order_submit(self):
        temp_cardmachine=None
        temp_UPItype=None
        temp_cname=self.New_Order_Name.text()
        if self.checkBox_4.isChecked(): temp_cname+=" (adj)"
        if self.NOCardgroup.checkedButton()!=None:
            temp_cardmachine=self.NOCardgroup.checkedButton().text()
        if self.NOCardgroup.checkedButton()!=None:
            temp_UPItype=self.NOUPIgroup.checkedButton().text()

        if self.New_Order_Goods.isChecked():
            if self.New_Order_EstAmount.value()!=0 and self.New_Order_Adv.value() !=0 and self.New_Order_Itemname.text() !='' and self.New_Order_grwt.value()!=0.0 and self.New_Order_ntwt.value()!=0.0:
                if self.New_Order_GS.currentText()=='G':
                    self.nextlist[str(self.pagenum*5)+"NO"]=NO(self.New_Order_EstAmount.value(), self.New_Order_Adv.value(),
                    self.New_Order_Itemname.text(), self.New_Order_grwt.value(), self.New_Order_ntwt.value(), 0.0, 0.0)
                else:
                    self.nextlist[str(self.pagenum*5)+"NO"]=NO(self.New_Order_EstAmount.value(), self.New_Order_Adv.value(), 
                    self.New_Order_Itemname.text(), 0.0, 0.0, self.New_Order_grwt.value(), self.New_Order_ntwt.value())
            if self.New_Order_EstAmount_2.value()!=0 and self.New_Order_Adv_2.value() !=0 and self.New_Order_Itemname_2.text() !='' and self.New_Order_grwt_2.value()!=0.0 and self.New_Order_ntwt_2.value()!=0.0:
                if self.New_Order_GS_2.currentText()=='G':
                    self.nextlist[str(self.pagenum*5+1)+"NO"]=NO(self.New_Order_EstAmount_2.value(), self.New_Order_Adv_2.value(),
                    self.New_Order_Itemname_2.text(), self.New_Order_grwt_2.value(), self.New_Order_ntwt_2.value(), 0.0, 0.0)
                else:
                    self.nextlist[str(self.pagenum*5+1)+"NO"]=NO(self.New_Order_EstAmount_2.value(), self.New_Order_Adv_2.value(), 
                    self.New_Order_Itemname_2.text(), 0.0, 0.0, self.New_Order_grwt_2.value(), self.New_Order_ntwt_2.value())
            if self.New_Order_EstAmount_3.value()!=0 and self.New_Order_Adv_3.value() !=0 and self.New_Order_Itemname_3.text() !='' and self.New_Order_grwt_3.value()!=0.0 and self.New_Order_ntwt_3.value()!=0.0:
                if self.New_Order_GS_3.currentText()=='G':
                    self.nextlist[str(self.pagenum*5+2)+"NO"]=NO(self.New_Order_EstAmount_3.value(), self.New_Order_Adv_3.value(),
                    self.New_Order_Itemname_3.text(), self.New_Order_grwt_3.value(), self.New_Order_ntwt_3.value(), 0.0, 0.0)
                else:
                    self.nextlist[str(self.pagenum*5+2)+"NO"]=NO(self.New_Order_EstAmount_3.value(), self.New_Order_Adv_3.value(), 
                    self.New_Order_Itemname_3.text(), 0.0, 0.0, self.New_Order_grwt_3.value(), self.New_Order_ntwt_3.value())
            if self.New_Order_EstAmount_4.value()!=0 and self.New_Order_Adv_4.value() !=0 and self.New_Order_Itemname_4.text() !='' and self.New_Order_grwt_4.value()!=0.0 and self.New_Order_ntwt_4.value()!=0.0:
                if self.New_Order_GS_4.currentText()=='G':
                    self.nextlist[str(self.pagenum*5+3)+"NO"]=NO(self.New_Order_EstAmount_4.value(), self.New_Order_Adv_4.value(),
                    self.New_Order_Itemname_4.text(), self.New_Order_grwt_4.value(), self.New_Order_ntwt_4.value(), 0.0, 0.0)
                else:
                    self.nextlist[str(self.pagenum*5+3)+"NO"]=NO(self.New_Order_EstAmount_4.value(), self.New_Order_Adv_4.value(), 
                    self.New_Order_Itemname_4.text(), 0.0, 0.0, self.New_Order_grwt_4.value(), self.New_Order_ntwt_4.value())
            if self.New_Order_EstAmount_5.value()!=0 and self.New_Order_Adv_5.value() !=0 and self.New_Order_Itemname_5.text() !='' and self.New_Order_grwt_5.value()!=0.0 and self.New_Order_ntwt_5.value()!=0.0:
                if self.New_Order_GS_5.currentText()=='G':
                    self.nextlist[str(self.pagenum*5+4)+"NO"]=NO(self.New_Order_EstAmount_5.value(), self.New_Order_Adv_5.value(),
                    self.New_Order_Itemname_5.text(), self.New_Order_grwt_5.value(), self.New_Order_ntwt_5.value(), 0.0, 0.0)
                else:
                    self.nextlist[str(self.pagenum*5+4)+"NO"]=NO(self.New_Order_EstAmount_5.value(), self.New_Order_Adv_5.value(), 
                    self.New_Order_Itemname_5.text(), 0.0, 0.0, self.New_Order_grwt_5.value(), self.New_Order_ntwt_5.value())
            temp_itemname=''
            temp_est=0
            temp_adv=0
            temp_goldgrwt=float(0)
            temp_goldntwt=float(0)
            temp_silvergrwt=float(0)
            temp_silverntwt=float(0)
            for key in self.nextlist.keys():
                if "NO" in key:
                    temp_itemname=', '.join([temp_itemname, self.nextlist[key].item])
                    temp_est+=self.nextlist[key].Est
                    temp_adv+=self.nextlist[key].Adv
                    temp_goldgrwt+=self.nextlist[key].Ggrwt
                    temp_goldntwt+=self.nextlist[key].Gntwt
                    temp_silvergrwt+=self.nextlist[key].Sgrwt
                    temp_silverntwt+=self.nextlist[key].Sntwt
            temp_itemname=temp_itemname[2:]
            if self.ui.URDpass==[]:
                if self.comboBox_4.currentText()=='G':
                    URDlist=[self.URDitemname.text(), self.URD_grwt.value(), self.URD_ntwt.value(), 0.0, 0.0]
                else:
                    URDlist=[self.URDitemname.text(), 0.0, 0.0, self.URD_grwt.value(), self.URD_ntwt.value()]
            else:
                URDlist=self.ui.URDpass

            Bill_store(Bill(temp_cname ,self.New_Order_phnum.text(), temp_itemname, temp_est, '', temp_goldgrwt,
                        temp_goldntwt, temp_silvergrwt, temp_silverntwt, 'New Order', temp_adv, self.Cash_4.value(), self.Card_4.value(),
                        temp_cardmachine, self.UPI_4.value(), temp_UPItype, self.Cheque_4.value(), self.ChequeNo_4.text(), 
                        self.DebtAmount_4.value(), self.URDAmount_4.value(), URDlist[0], URDlist[1], URDlist[2], URDlist[3], 
                        URDlist[4], 0, '', date.today()), self.nextlist)
        else:
            if self.ui.URDpass==[]:
                if self.comboBox_4.currentText()=='G':
                    URDlist=[self.URDitemname.text(), self.URD_grwt.value(), self.URD_ntwt.value(), 0.0, 0.0]
                else:
                    URDlist=[self.URDitemname.text(), 0.0, 0.0, self.URD_grwt.value(), self.URD_ntwt.value()]
            else:
                URDlist=self.ui.URDpass

            Bill_store(Bill(temp_cname , self.New_Order_phnum.text(), '', self.New_Order_EstAmount.value(), '', 0.0, 0.0, 0.0, 0.0,
                        'New Order', self.New_Order_total.value(), self.Cash_4.value(), self.Card_4.value(), temp_cardmachine, self.UPI_4.value(),
                        temp_UPItype, self.Cheque_4.value(), self.ChequeNo_4.text(), self.DebtAmount_4.value(), self.URDAmount_4.value(),
                        URDlist[0], URDlist[1], URDlist[2], URDlist[3], URDlist[4], 0, '', date.today()), self.nextlist)
        self.clearQlineedit()
        self.Radioclear()
        self.submitclear()
        self.nextlist.clear()
        NOconfirm=QtWidgets.QMessageBox()
        NOconfirm.setIcon(QMessageBox.Information)
        NOconfirm.setWindowTitle("Confirmation of Data Entry")
        NOconfirm.setText("The Old Order details have been entered")
        NOconfirm.setStandardButtons(QMessageBox.Ok)
        retval=NOconfirm.exec_()

    def Shree_submit(self):
        temp_type=None
        if self.Shgroup.checkedButton() != None:
            temp_type=self.Shgroup.checkedButton().text()
        if temp_type=='+':
            Bill_store(Bill(self.Shree_name.text(), '', '', '', '', 0.0, 0.0, 0.0, 0.0, 'Misc plus', self.Shree_amount.value(), 
                        self.Shree_amount.value(), 0, None, 0, None, 0, None, 0, 0, '', 0.0, 0.0, 0.0, 0.0, 0, '', date.today()), self.nextlist)
        elif temp_type=='-':
            Bill_store(Bill(self.Shree_name.text(), '', '', '', '', 0.0, 0.0, 0.0, 0.0, 'Misc minus', self.Shree_amount.value(), 
                        self.Shree_amount.value(), 0, None, 0, None, 0, None, 0, 0, '', 0.0, 0.0, 0.0, 0.0, 0, '', date.today()), self.nextlist)
        self.clearQlineedit()
        self.Radioclear()
        self.submitclear()
        self.nextlist.clear()
        Shconfirm=QtWidgets.QMessageBox()
        Shconfirm.setIcon(QMessageBox.Information)
        Shconfirm.setWindowTitle("Confirmation of Data Entry")
        Shconfirm.setText("The details have been entered")
        Shconfirm.setStandardButtons(QMessageBox.Ok)
        retval=Shconfirm.exec_()

    def VC_submit(self):
        temp_cardmachine=None
        temp_UPItype=None
        temp_cname=self.VC_name.text()
        if self.checkBox_5.isChecked(): temp_cname+=" (adj)"
        if self.ui.URDpass==[]:
            if self.comboBox_5.currentText()=='G':
                URDlist=[self.URDitemname.text(), self.URD_grwt.value(), self.URD_ntwt.value(), 0.0, 0.0]
            else:
                URDlist=[self.URDitemname.text(), 0.0, 0.0, self.URD_grwt.value(), self.URD_ntwt.value()]
        else:
            URDlist=self.ui.URDpass

        if self.VCCardgroup.checkedButton() != None:
            temp_cardmachine=self.VCCardgroup.checkedButton().text()
        if self.VCUPIgroup.checkedButton() != None:
            temp_UPItype=self.VCUPIgroup.checkedButton().text()
        if self.VC_Stacked.currentIndex()==0:
            Bill_store(Bill(temp_cname , self.VC_phnum.text(), '', '', '', 0.0, 0.0, 0.0, 0.0, 'VC', self.VC_Amount.value(), 
            self.Cash_5.value(), self.Card_5.value(), temp_cardmachine, self.UPI_5.value(), temp_UPItype, self.Cheque_5.value(),
            self.ChequeNo_5.text(), self.DebtAmount_5.value(), self.URDAmount_5.value(), URDlist[0], URDlist[1], URDlist[2], URDlist[3],
            URDlist[4], 0, '', date.today()), self.nextlist)
        else:
            if self.VC_Itemname.text()!='' and self.VC_Amount_2.value() != 0 and self.VC_grwt.value() != 0.0 and self.VC_ntwt.value() != 0.0:
                self.nextlist[str(self.pagenum*5)+"VC"]=VC(self.VC_GS.currentText(), self.VC_Itemname.text(), self.VC_Amount_2.value(), 
                self.VC_grwt.value(), self.VC_ntwt.value())
            if self.VC_Itemname_2.text()!='' and self.VC_Amount_3.value() != 0 and self.VC_grwt_2.value() != 0.0 and self.VC_ntwt_2.value() != 0.0:
                self.nextlist[str(self.pagenum*5+1)+"VC"]=VC(self.VC_GS_2.currentText(), self.VC_Itemname_2.text(), self.VC_Amount_3.value(), 
                self.VC_grwt_2.value(), self.VC_ntwt_2.value())
            if self.VC_Itemname_3.text()!='' and self.VC_Amount_4.value() != 0 and self.VC_grwt_3.value() != 0.0 and self.VC_ntwt_3.value() != 0.0:
                self.nextlist[str(self.pagenum*5+2)+"VC"]=VC(self.VC_GS_3.currentText(), self.VC_Itemname_3.text(), self.VC_Amount_4.value(), 
                self.VC_grwt_3.value(), self.VC_ntwt_3.value())
            if self.VC_Itemname_4.text()!='' and self.VC_Amount_5.value() != 0 and self.VC_grwt_4.value() != 0.0 and self.VC_ntwt_4.value() != 0.0:
                self.nextlist[str(self.pagenum*5+3)+"VC"]=VC(self.VC_GS_4.currentText(), self.VC_Itemname_4.text(), self.VC_Amount_5.value(), 
                self.VC_grwt_4.value(), self.VC_ntwt_4.value())
            if self.VC_Itemname_5.text()!='' and self.VC_Amount_6.value() != 0 and self.VC_grwt_5.value() != 0.0 and self.VC_ntwt_5.value() != 0.0:
                self.nextlist[str(self.pagenum*5+4)+"VC"]=VC(self.VC_GS_5.currentText(), self.VC_Itemname_5.text(), self.VC_Amount_6.value(), 
                self.VC_grwt_5.value(), self.VC_ntwt_5.value())
            temp_itemname=''
            temp_amount=0
            temp_goldgrwt=0.0
            temp_goldntwt=0.0
            temp_silvergrwt=0.0
            temp_silverntwt=0.0
            for key in self.nextlist.keys():
                if "VC" in key:
                    temp_itemname=', '.join([temp_itemname, self.nextlist[key].item])
                    temp_amount+=self.nextlist[key].amount
                    if self.nextlist[key].type=='G':
                        temp_goldgrwt+=self.nextlist[key].grwt
                        temp_goldntwt+=self.nextlist[key].ntwt
                    elif  self.nextlist[key].type ==  'S':
                        temp_silvergrwt+=self.nextlist[key].grwt
                        temp_silverntwt+=self.nextlist[key].ntwt
            Bill_store(Bill(temp_cname , self.VC_phnum.text(), temp_itemname, '', '', temp_goldgrwt, temp_goldntwt, 
            temp_silvergrwt, temp_silverntwt, 'VC', temp_amount,  self.Cash_5.value(), self.Card_5.value(), temp_cardmachine,
            self.UPI_5.value(), temp_UPItype, self.Cheque_5.value(), self.ChequeNo_5.text(), self.DebtAmount_5.value(),
            self.URDAmount_5.value(), URDlist[0], URDlist[1], URDlist[2], URDlist[3], URDlist[4], 0, '', date.today()), self.nextlist)   
        self.clearQlineedit()
        self.Radioclear()
        self.submitclear()
        self.nextlist.clear()
        VCconfirm=QtWidgets.QMessageBox()
        VCconfirm.setIcon(QMessageBox.Information)
        VCconfirm.setWindowTitle("Confirmation of Data Entry")
        VCconfirm.setText("The details have been entered")
        VCconfirm.setStandardButtons(QMessageBox.Ok)
        retval=VCconfirm.exec_()

    def GP_submit(self):
        if self.GP_Itemname.text()!='' and self.GP_grwt.value()!=0.0 and self.GP_ntwt.value()!=0.0 and self.GP_Amount!=0:
            self.nextlist[str(self.pagenum*5)+"GP"]=purchase('Gold Purchase', self.GP_Itemname.text(), self.GP_grwt.value(), 
            self.GP_ntwt.value(), self.GP_Amount.value())
        if self.GP_Itemname_2.text()!='' and self.GP_grwt_2.value()!=0.0 and self.GP_ntwt_2.value()!=0.0 and self.GP_Amount_2!=0:
            self.nextlist[str(self.pagenum*5+1)+"GP"]=purchase('Gold Purchase', self.GP_Itemname_2.text(), self.GP_grwt_2.value(), 
            self.GP_ntwt_2.value(), self.GP_Amount_2.value())
        if self.GP_Itemname_3.text()!='' and self.GP_grwt_3.value()!=0.0 and self.GP_ntwt_3.value()!=0.0 and self.GP_Amount_3!=0:
            self.nextlist[str(self.pagenum*5+2)+"GP"]=purchase('Gold Purchase', self.GP_Itemname_3.text(), self.GP_grwt_3.value(), 
            self.GP_ntwt_3.value(), self.GP_Amount_3.value())
        if self.GP_Itemname_4.text()!='' and self.GP_grwt_4.value()!=0.0 and self.GP_ntwt_4.value()!=0.0 and self.GP_Amount_4!=0:
            self.nextlist[str(self.pagenum*5+3)+"GP"]=purchase('Gold Purchase', self.GP_Itemname_4.text(), self.GP_grwt_4.value(), 
            self.GP_ntwt_4.value(), self.GP_Amount_4.value())
        if self.GP_Itemname_5.text()!='' and self.GP_grwt_5.value()!=0.0 and self.GP_ntwt_5.value()!=0.0 and self.GP_Amount_5!=0:
            self.nextlist[str(self.pagenum*5+4)+"GP"]=purchase('Gold Purchase', self.GP_Itemname_5.text(), self.GP_grwt_5.value(), 
            self.GP_ntwt_5.value(), self.GP_Amount_5.value())

        temp_itemname=''
        temp_grwt=0.0
        temp_ntwt=0.0
        temp_amount=0
        temp_cash=0
        temp_cheque=[0, '']
        temp_other=[0, '']
        if self.GP_Cash.isChecked():
            temp_cash=self.Cash_6.value()
        if self.GP_Cheque.isChecked():
            temp_cheque=[self.Cheque_6.value(), self.ChequeNo_6.text()]
        if self.GP_Other.isChecked():
            temp_other=[self.Other_Amount.value(), self.Other_Name.text()]
        for key in self.nextlist.keys():
            if "GP" in key:
                temp_itemname=', '.join([temp_itemname, self.nextlist[key].item])
                temp_grwt+=self.nextlist[key].grwt
                temp_ntwt+=self.nextlist[key].ntwt
                temp_amount+=self.nextlist[key].amount
        temp_itemname=temp_itemname[2:]
        Bill_store(Bill(self.GP_Name.text(), self.GP_phnum.text(), temp_itemname, '', '', 0.0, 0.0, 0.0, 0.0, 'Gold Purchase', 
        temp_amount, temp_cash, 0, None, 0, None, temp_cheque[0], temp_cheque[1], 0, 0, '', temp_grwt, temp_ntwt, 0.0, 0.0, temp_other[0], 
        temp_other[1], date.today()), self.nextlist)
        self.clearQlineedit()
        self.Radioclear()
        self.submitclear()
        self.nextlist.clear()
        GPconfirm=QtWidgets.QMessageBox()
        GPconfirm.setIcon(QMessageBox.Information)
        GPconfirm.setWindowTitle("Confirmation of Data Entry")
        GPconfirm.setText("The details have been entered")
        GPconfirm.setStandardButtons(QMessageBox.Ok)
        retval=GPconfirm.exec_()

    def SP_submit(self):
        if self.SP_Itemname.text()!='' and self.SP_grwt.value()!=0.0 and self.SP_ntwt.value()!=0.0 and self.SP_Amount!=0:
            self.nextlist[str(self.pagenum*5)+"SP"]=purchase('Silver Purchase', self.SP_Itemname.text(), self.SP_grwt.value(), 
            self.SP_ntwt.value(), self.SP_Amount.value())
        if self.SP_Itemname_2.text()!='' and self.SP_grwt_2.value()!=0.0 and self.SP_ntwt_2.value()!=0.0 and self.SP_Amount_2!=0:
            self.nextlist[str(self.pagenum*5+1)+"SP"]=purchase('Silver Purchase', self.SP_Itemname_2.text(), self.SP_grwt_2.value(), 
            self.SP_ntwt_2.value(), self.SP_Amount_2.value())
        if self.SP_Itemname_3.text()!='' and self.SP_grwt_3.value()!=0.0 and self.SP_ntwt_3.value()!=0.0 and self.SP_Amount_3!=0:
            self.nextlist[str(self.pagenum*5+2)+"SP"]=purchase('Silver Purchase', self.SP_Itemname_3.text(), self.SP_grwt_3.value(), 
            self.SP_ntwt_3.value(), self.SP_Amount_3.value())
        if self.SP_Itemname_4.text()!='' and self.SP_grwt_4.value()!=0.0 and self.SP_ntwt_4.value()!=0.0 and self.SP_Amount_4!=0:
            self.nextlist[str(self.pagenum*5+3)+"SP"]=purchase('Silver Purchase', self.SP_Itemname_4.text(), self.SP_grwt_4.value(), 
            self.SP_ntwt_4.value(), self.SP_Amount_4.value())
        if self.SP_Itemname_5.text()!='' and self.SP_grwt_5.value()!=0.0 and self.SP_ntwt_5.value()!=0.0 and self.SP_Amount_5!=0:
            self.nextlist[str(self.pagenum*5+4)+"SP"]=purchase('Silver Purchase', self.SP_Itemname_5.text(), self.SP_grwt_5.value(), 
            self.SP_ntwt_5.value(), self.SP_Amount_5.value())
        temp_itemname=''
        temp_grwt=0.0
        temp_ntwt=0.0
        temp_amount=0
        temp_cash=0
        temp_cheque=[0, '']
        temp_other=[0, '']
        if self.SP_Cash.isChecked():
            temp_cash=self.Cash_7.value()
        if self.SP_Cheque.isChecked():
            temp_cheque=[self.Cheque_7.value(), self.ChequeNo_7.text()]
        if self.SP_Other.isChecked():
            temp_other=[self.Other_Amount_2.value(), self.Other_Name_2.text()]
        for key in self.nextlist.keys():
            if "SP" in key:
                temp_itemname=', '.join([temp_itemname, self.nextlist[key].item])
                temp_grwt+=self.nextlist[key].grwt
                temp_ntwt+=self.nextlist[key].ntwt
                temp_amount+=self.nextlist[key].amount
        temp_itemname=temp_itemname[2:]
        Bill_store(Bill(self.SP_Name.text(), self.SP_phnum.text(), temp_itemname, '', '', 0.0, 0.0, 0.0, 0.0, 'Silver Purchase', 
        temp_amount, temp_cash, 0, None, 0, None, temp_cheque[0], temp_cheque[1], 0, 0, '', 0.0, 0.0, temp_grwt, temp_ntwt, temp_other[0], 
        temp_other[1], date.today()), self.nextlist)
        self.clearQlineedit()
        self.Radioclear()
        self.submitclear()
        self.nextlist.clear()
        SPconfirm=QtWidgets.QMessageBox()
        SPconfirm.setIcon(QMessageBox.Information)
        SPconfirm.setWindowTitle("Confirmation of Data Entry")
        SPconfirm.setText("The details have been entered")
        SPconfirm.setStandardButtons(QMessageBox.Ok)
        retval=SPconfirm.exec_()

    def Expense_submit(self):
        Bill_store(Bill(self.Expense_name.text(), '', '', '', '', 0.0, 0.0, 0.0, 0.0, 'Expense', self.Expense_amount.value(),
                     self.Expense_amount.value(), 0, None, 0, None, 0, None, 0, 0, '', 0.0, 0.0, 0.0, 0.0, 0, '', date.today()), self.nextlist)
        self.clearQlineedit()
        self.Radioclear()
        self.submitclear()
        self.nextlist.clear()
        Exconfirm=QtWidgets.QMessageBox()
        Exconfirm.setIcon(QMessageBox.Information)
        Exconfirm.setWindowTitle("Confirmation of Data Entry")
        Exconfirm.setText("The details have been entered")
        Exconfirm.setStandardButtons(QMessageBox.Ok)
        retval=Exconfirm.exec_()
    
    def update_payment(self):
        if self.stackedWidget.currentIndex()==1:
            temp_cash=self.Gold_total.value()-self.Card.value()-self.Cheque.value()-self.UPI.value()-self.URDAmount.value()-self.DebtAmount.value()
            self.Cash.setValue(temp_cash)
        elif self.stackedWidget.currentIndex()==2:
            temp_cash=self.Silver_total.value()-self.Card_2.value()-self.Cheque_2.value()-self.UPI_2.value()-self.URDAmount_2.value()-self.DebtAmount_2.value()
            self.Cash_2.setValue(temp_cash)
        elif self.stackedWidget.currentIndex()==3:
            if self.Old_Order_Sale.isChecked():
                temp_cash=self.Old_Order_Total.value()-self.Card_3.value()-self.Cheque_3.value()-self.UPI_3.value()-self.URDAmount_3.value()-self.DebtAmount_3.value()
            else:
                temp_cash=self.Old_Order_Deposit.value()-self.Card_3.value()-self.Cheque_3.value()-self.UPI_3.value()-self.URDAmount_3.value()-self.DebtAmount_3.value()
            self.Cash_3.setValue(temp_cash)
        elif self.stackedWidget.currentIndex()==4:
            temp_cash=self.New_Order_total.value()-self.Card_4.value()-self.Cheque_4.value()-self.UPI_4.value()-self.URDAmount_4.value()-self.DebtAmount_4.value()
            self.Cash_4.setValue(temp_cash)
        elif self.stackedWidget.currentIndex()==6:
            if self.VC_Saleconvert.isChecked():
                temp_cash=self.VC_total.value()-self.Card_5.value()-self.Cheque_5.value()-self.UPI_5.value()-self.URDAmount_5.value()-self.DebtAmount_5.value()
            else:
                temp_cash=self.VC_Amount.value()-self.Card_5.value()-self.Cheque_5.value()-self.UPI_5.value()-self.URDAmount_5.value()-self.DebtAmount_5.value()
            self.Cash_5.setValue(temp_cash)
        elif self.stackedWidget.currentIndex()==7 and self.GP_Cash.isChecked():
            temp_cash=self.GP_total.value()
            if self.GP_Cheque.isChecked():
                temp_cash-=self.Cheque_6.value()
            if self.GP_Other.isChecked():
                temp_cash-=self.Other_Amount
            self.Cash_6.setValue(temp_cash)
        elif self.stackedWidget.currentIndex()==8 and self.SP_Cash.isChecked():
            temp_cash=self.SP_total.value()
            if self.SP_Cheque.isChecked():
                temp_cash-=self.Cheque_7.value()
            if self.SP_Other.isChecked():
                temp_cash-=self.Other_Amount_2.value()
            self.Cash_7.setValue(temp_cash)


if __name__=='__main__':
    import sys
    app=QtWidgets.QApplication(sys.argv)
    window=MainWindow()
    sys.exit(app.exec_())
