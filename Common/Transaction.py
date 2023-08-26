class GoldSell:
    def __init__(self, cust_name, ph_num, pr_name, id, gr_wt, nt_wt, amount, purity, date):
        self.cust_name=cust_name    #customer name
        self.ph_num=ph_num  #phone number
        self.pr_name=pr_name #product name
        self.id=id  #product id
        self.gr_wt=gr_wt # gross weight
        self.nt_wt=nt_wt # net weight
        self.amount=amount #final amount
        self.purity=purity #purity
        self.date=date  #date

    def __repr__(self) -> str:
        return f'GoldSell( customer name = {self.cust_name}, phone number = {self.ph_num}, product name = {self.pr_name},id = {self.id}, gross weight = {self.gr_wt}, net weight = {self.nt_wt}, amount = {self.amount})'

class SilverSell:
    def __init__(self, cust_name, ph_num, pr_name, id, gr_wt, nt_wt, amount, purity, date):
        self.cust_name=cust_name    #customer name
        self.ph_num=ph_num  #phone number
        self.pr_name=pr_name #product name
        self.id=id  #product id
        self.gr_wt=gr_wt # gross weight
        self.nt_wt=nt_wt # net weight
        self.amount=amount #final amount
        self.purity=purity #purity
        self.date=date  #date

class OldOrder:
    def __init__(self, type, item, amount, grwt, ntwt):
        self.type=type
        self.amount=amount
        self.item=item
        self.grwt=grwt
        self.ntwt=ntwt

class NO:
    def __init__(self, Est, Adv, item, Ggrwt, Gntwt, Sgrwt, Sntwt) -> None:
        self.Est=Est
        self.Adv=Adv
        self.item= item
        self.Ggrwt=Ggrwt
        self.Gntwt=Gntwt
        self.Sgrwt=Sgrwt
        self.Sntwt=Sntwt

class VC:
    def __init__(self, type, item, amount, grwt, ntwt):
        self.type=type
        self.item=item
        self.amount=amount
        self.grwt=grwt 
        self.ntwt=ntwt

class purchase:
    def __init__(self, ptype, item, grwt, ntwt, amount) -> None:
        self.type=ptype
        self.item=item
        self.grwt=grwt
        self.ntwt=ntwt
        self.amount=amount

class Bill:
    def __init__(self,cust_name, ph_num, items_name,  item_id, purity, gold_grwt, gold_ntwt, silver_grwt, silver_ntwt,trans_type, amount, cash,card, card_machine, UPI, UPI_type
                , cheque, cheque_num, debt, URD, URD_name, URD_goldgrwt, URD_goldntwt, URD_silvergrwt, URD_silverntwt, other, othername, date):
        self.cust_name=cust_name
        self.ph_num=ph_num
        self.items_name=items_name
        self.item_id=item_id
        self.purity=purity
        self.gold_grwt=gold_grwt
        self.gold_ntwt=gold_ntwt
        self.silver_grwt=silver_grwt
        self.silver_ntwt=silver_ntwt
        self.trans_type=trans_type
        self.amount=amount
        self.cash=cash
        self.card=card
        self.card_machine=card_machine
        self.UPI=UPI
        self.UPI_type=UPI_type
        self.cheque=cheque
        self.cheque_num=cheque_num
        self.debt=debt
        self.URD=URD
        self.URD_name=URD_name
        self.URD_goldgrwt=URD_goldgrwt
        self.URD_goldntwt=URD_goldntwt
        self.URD_silvergrwt=URD_silvergrwt
        self.URD_silverntwt=URD_silverntwt
        self.other=other
        self.othername=othername
        self.date=date

    def __repr__(self) -> str:
        return f'SilverSell( customer name = {self.cust_name}, phone number = {self.ph_num}, product name = {self.pr_name},id = {self.id}, gross weight = {self.gr_wt}, net weight = {self.nt_wt}, amount = {self.amount})'
