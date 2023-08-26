from Backend import Bill_store
from Transaction import Bill
from datetime import date, timedelta
import random

cardtype=['mSwipe', 'Bharatpe', 'Gpay', 'Other']
upitype=['Bharatpe', 'Gpay', 'Other']
def GS_gen(num):
    for i in range(num):
        payment_num=random.randint(1,6)
        payments=random.sample([0, 1, 2, 3, 4, 5], payment_num)
        name='dummy'+str(i)
        ph_num=random.randint(1000000000, 9999999999)
        purity= '916' if random.randint(0, 2)!= 1 else '750'
        grwt=round(random.random()*10, 3)
        ntwt= round(grwt if random.randint(0,10) != 1 else grwt*random.random(), 3)
        amount=int(round(5000*ntwt))
        temp_card=cardtype[random.randint(0,3)]
        temp_upi=upitype[random.randint(0,2)]
        chequeno=random.randint(100000,999999)
        cash, card, upi, cheque, debt, other= 0, 0, 0, 0, 0, 0
        for idx, items in enumerate(payments):
            if items==0:
                if idx < payment_num-1:
                    cash=round(amount*random.random())
                    amount-=cash
                if idx==payment_num-1:
                    cash=amount
                    amount=0
                    print(0)
            elif items==1:
                if idx < payment_num-1:
                    card=round(amount*random.random())
                    amount-=card
                if idx==payment_num-1:
                    card=amount
                    amount-=card
                    print(1)
            elif items==2:
                if idx < payment_num-1:
                    upi=round(amount*random.random())
                    amount-=upi
                if idx == payment_num-1:
                    upi=amount
                    amount=0
                    print(2)
            elif items==3:
                if idx < payment_num-1:
                    cheque=round(amount*random.random())
                    amount-=cheque
                if idx == payment_num-1:
                    cheque=amount
                    amount=0
                    print(3)
            elif items==4:
                if idx < payment_num-1:
                    debt=round(amount*random.random())
                    amount-=debt
                if idx == payment_num-1:
                    debt=amount
                    amount=0
                    print(4)
            elif items==5:
                if idx < payment_num-1:
                    other=round(amount*random.random())
                    amount-=other
                if idx== payment_num-1:
                    other=amount
                    amount=0
                    print(5)
        amount=int(round(ntwt*5000))

        Bill_store(Bill(name, ph_num, 'EAR', '', purity, grwt, ntwt, 0.0, 0.0, 'Gold Sale', amount, cash, card, temp_card, upi, temp_upi, 
        cheque, chequeno, debt, 0, '', 0.0, 0.0, 0.0, 0.0, other, 'NEFT', date.today()))

def GS_gen_days(num, day, dte=date.today()):
    for time_d in range(day):
        for i in range(num):
            payment_num=random.randint(1,6)
            payments=random.sample([0, 1, 2, 3, 4, 5], payment_num)
            name='dummy'+str(i)
            ph_num=random.randint(1000000000, 9999999999)
            purity= '916' if random.randint(0, 2)!= 1 else '750'
            grwt=round(random.random()*10, 3)
            ntwt= round(grwt if random.randint(0,10) != 1 else grwt*random.random(), 3)
            amount=int(round(5000*ntwt))
            temp_card=cardtype[random.randint(0,3)]
            temp_upi=upitype[random.randint(0,2)]
            chequeno=random.randint(100000,999999)
            cash, card, upi, cheque, debt, other= 0, 0, 0, 0, 0, 0
            for idx, items in enumerate(payments):
                if items==0:
                    if idx < payment_num-1:
                        cash=round(amount*random.random())
                        amount-=cash
                    if idx==payment_num-1:
                        cash=amount
                        amount=0
                        print(0)
                elif items==1:
                    if idx < payment_num-1:
                        card=round(amount*random.random())
                        amount-=card
                    if idx==payment_num-1:
                        card=amount
                        amount-=card
                        print(1)
                elif items==2:
                    if idx < payment_num-1:
                        upi=round(amount*random.random())
                        amount-=upi
                    if idx == payment_num-1:
                        upi=amount
                        amount=0
                        print(2)
                elif items==3:
                    if idx < payment_num-1:
                        cheque=round(amount*random.random())
                        amount-=cheque
                    if idx == payment_num-1:
                        cheque=amount
                        amount=0
                        print(3)
                elif items==4:
                    if idx < payment_num-1:
                        debt=round(amount*random.random())
                        amount-=debt
                    if idx == payment_num-1:
                        debt=amount
                        amount=0
                        print(4)
                elif items==5:
                    if idx < payment_num-1:
                        other=round(amount*random.random())
                        amount-=other
                    if idx== payment_num-1:
                        other=amount
                        amount=0
                        print(5)
            amount=int(round(ntwt*5000))
            dte+=timedelta(days=1)
            Bill_store(Bill(name, ph_num, '', '', purity, grwt, ntwt, 0.0, 0.0, 'Gold Sale', amount, cash, card, temp_card, upi, temp_upi, 
            cheque, chequeno, debt, 0, '', 0.0, 0.0, 0.0, 0.0, other, 'NEFT', dte))


def SS_gen(num):
    for i in range(num):
        payment_num=random.randint(1,6)
        payments=random.sample(list(range(6)), payment_num)
        name='dummy'+str(i)
        ph_num=random.randint(1000000000, 9999999999)
        grwt=round(random.random()*10, 3)
        purity='70%'
        ntwt= round(grwt if random.randint(0,10) != 1 else grwt*random.random(), 3)
        amount=int(round(5000*ntwt))
        temp_card=cardtype[random.randint(0,3)]
        temp_upi=upitype[random.randint(0,2)]
        chequeno=random.randint(100000,999999)
        cash, card, upi, cheque, debt, other= 0, 0, 0, 0, 0, 0
        for idx, items in enumerate(payments):
            if items==0:
                if idx < payment_num-1:
                    cash=round(amount*random.random())
                    amount-=cash
                if idx==payment_num-1:
                    cash=amount
                    amount=0
                    print(0)
            elif items==1:
                if idx < payment_num-1:
                    card=round(amount*random.random())
                    amount-=card
                if idx==payment_num-1:
                    card=amount
                    amount-=card
                    print(1)
            elif items==2:
                if idx < payment_num-1:
                    upi=round(amount*random.random())
                    amount-=upi
                if idx == payment_num-1:
                    upi=amount
                    amount=0
                    print(2)
            elif items==3:
                if idx < payment_num-1:
                    cheque=round(amount*random.random())
                    amount-=cheque
                if idx == payment_num-1:
                    cheque=amount
                    amount=0
                    print(3)
            elif items==4:
                if idx < payment_num-1:
                    debt=round(amount*random.random())
                    amount-=debt
                if idx == payment_num-1:
                    debt=amount
                    amount=0
                    print(4)
            elif items==5:
                if idx < payment_num-1:
                    other=round(amount*random.random())
                    amount-=other
                if idx== payment_num-1:
                    other=amount
                    amount=0
                    print(5)
        amount=int(round(ntwt*5000))

#Silver Sale dummy
        Bill_store(Bill(name, ph_num, '', '', purity, 0.0, 0.0, grwt, ntwt, 'Silver Sale', amount, cash, card, temp_card, upi, temp_upi, 
        cheque, chequeno, debt, 0, '', 0.0, 0.0, 0.0, 0.0, other, 'NEFT', date.today()))

def Old_Order_gen(num):
    for i in range(num):
        payment_num=random.randint(1,6)
        payments=random.sample(list(range(6)), payment_num)
        name='olddummy'+str(i)
        ph_num=random.randint(1000000000, 9999999999)
        purity= ''
        temp_card=cardtype[random.randint(0,3)]
        temp_upi=upitype[random.randint(0,2)]
        chequeno=random.randint(100000,999999)
        cash, card, upi, cheque, debt, other= 0, 0, 0, 0, 0, 0
        urd, urd_gold, urd_silver =0, 0.0, 0.0
        itemname=''
        gold_grwt=0.0
        gold_ntwt=0.0
        silver_grwt=0.0
        silver_ntwt=0.0
        purity= ''
        if random.randint(0,5)==5:
            for i in range(5):
                tempgold_grwt=0.0
                tempsilver_grwt=0.0
                tempitemname=''
                if random.randint(0,1)==1:
                    temp_purity='916' if random.randint(0, 10)!=1 else '750'
                    tempgold_grwt=round(random.random(), 3)*10
                    gold_grwt+=tempgold_grwt
                    gold_ntwt+=gold_grwt if random.randint(0,10)!=1 else round(tempgold_grwt*random.random(), 3)
                    itemname=' ,'.join([itemname, tempitemname])
                    purity=' ,'.join([purity, temp_purity])
                else:
                    temp_purity='70%'
                    tempsilver_grwt=round(random.random(),3)*10
                    silver_grwt+=tempsilver_grwt
                    silver_ntwt+=silver_grwt if random.randint(0,10)!= 1 else round(tempsilver_grwt*random.random(), 3)
                    itemname=' ,'.join([itemname, tempitemname])
                    purity=' ,'.join([purity, temp_purity])

        amount=gold_ntwt*5000+silver_ntwt*4000
        for idx, items in enumerate(payments):
            if items==0:
                if idx < payment_num-1:
                    cash=round(amount*random.random())
                    amount-=cash
                if idx==payment_num-1:
                    cash=amount
                    amount=0
                    print(0)
            elif items==1:
                if idx < payment_num-1:
                    card=round(amount*random.random())
                    amount-=card
                if idx==payment_num-1:
                    card=amount
                    amount-=card
                    print(1)
            elif items==2:
                if idx < payment_num-1:
                    upi=round(amount*random.random())
                    amount-=upi
                if idx == payment_num-1:
                    upi=amount
                    amount=0
                    print(2)
            elif items==3:
                if idx < payment_num-1:
                    cheque=round(amount*random.random())
                    amount-=cheque
                if idx == payment_num-1:
                    cheque=amount
                    amount=0
                    print(3)
            elif items==4:
                if idx < payment_num-1:
                    debt=round(amount*random.random())
                    amount-=debt
                if idx == payment_num-1:
                    debt=amount
                    amount=0
                    print(4)
            elif items==5:
                if idx < payment_num-1:
                    urd=round(amount*random.random())
                    if random.randint(0,1)==0:
                        urd_gold=urd/5000
                    else:
                        urd_silver=urd/4000
                if idx== payment_num-1:
                    urd=amount
                    amount=0
                    if random.randint(0,1)==0:
                        urd_gold=urd/5000
                    else:
                        urd_silver=urd/4000
                    print(5)

        amount=gold_ntwt*5000+silver_ntwt*4000
#Old Order dummy
        Bill_store(Bill(name, ph_num, itemname, '', purity, gold_grwt, gold_ntwt, silver_grwt, silver_ntwt, 'Old Order', amount, cash, card, temp_card, upi, temp_upi, 
        cheque, chequeno, debt, urd, '', urd_gold, urd_gold, urd_silver, urd_silver, other, 'NEFT', date.today()))

def New_Order_gen(num):
    for i in range(num):
        payment_num=random.randint(1,6)
        payments=random.sample(list(range(6)), payment_num)
        name='olddummy'+str(i)
        ph_num=random.randint(1000000000, 9999999999)
        purity= ''
        grwt=round(random.random()*10, 3)
        ntwt= round(grwt if random.randint(0,10) != 1 else grwt*random.random(), 3)
        amount=int(round(5000*ntwt))
        temp_card=cardtype[random.randint(0,3)]
        temp_upi=upitype[random.randint(0,2)]
        chequeno=random.randint(100000,999999)
        cash, card, upi, cheque, debt, other= 0, 0, 0, 0, 0, 0
        urd, urd_gold, urd_silver =0, 0.0, 0.0
        for idx, items in enumerate(payments):
            if items==0:
                if idx < payment_num-1:
                    cash=round(amount*random.random())
                    amount-=cash
                if idx==payment_num-1:
                    cash=amount
                    amount=0
                    print(0)
            elif items==1:
                if idx < payment_num-1:
                    card=round(amount*random.random())
                    amount-=card
                if idx==payment_num-1:
                    card=amount
                    amount-=card
                    print(1)
            elif items==2:
                if idx < payment_num-1:
                    upi=round(amount*random.random())
                    amount-=upi
                if idx == payment_num-1:
                    upi=amount
                    amount=0
                    print(2)
            elif items==3:
                if idx < payment_num-1:
                    cheque=round(amount*random.random())
                    amount-=cheque
                if idx == payment_num-1:
                    cheque=amount
                    amount=0
                    print(3)
            elif items==4:
                if idx < payment_num-1:
                    debt=round(amount*random.random())
                    amount-=debt
                if idx == payment_num-1:
                    debt=amount
                    amount=0
                    print(4)
            elif items==5:
                if idx < payment_num-1:
                    urd=round(amount*random.random())
                    if random.randint(0,1)==0:
                        urd_gold=urd/5000
                    else:
                        urd_silver=urd/4000
                if idx== payment_num-1:
                    urd=amount
                    amount=0
                    if random.randint(0,1)==0:
                        urd_gold=urd/5000
                    else:
                        urd_silver=urd/4000
                    print(5)
        amount=int(round(ntwt*5000))
        itemname=''
        gold_grwt=0.0
        gold_ntwt=0.0
        silver_grwt=0.0
        silver_ntwt=0.0
        purity= ''
        if random.randint(0,5)==5:
            for i in range(5):
                tempgold_grwt=0.0
                tempsilver_grwt=0.0
                tempitemname=''
                if random.randint(0,1)==1:
                    temp_purity='916' if random.randint(0, 10)!=1 else '750'
                    tempgold_grwt=round(random.random(), 3)*10
                    gold_grwt+=tempgold_grwt
                    gold_ntwt+=gold_grwt if random.randint(0,10)!=1 else round(tempgold_grwt*random.random(), 3)
                    itemname=' ,'.join([itemname, tempitemname])
                    purity=' ,'.join([purity, temp_purity])
                else:
                    temp_purity='70%'
                    tempsilver_grwt=round(random.random(),3)*10
                    silver_grwt+=tempsilver_grwt
                    silver_ntwt+=silver_grwt if random.randint(0,10)!= 1 else round(tempsilver_grwt*random.random(), 3)
                    itemname=' ,'.join([itemname, tempitemname])
                    purity=' ,'.join([purity, temp_purity])
        Bill_store(Bill(name, ph_num, itemname, '', purity, gold_grwt, gold_ntwt, silver_grwt, silver_ntwt, 'New Order', amount, cash, card, temp_card, upi, temp_upi, 
        cheque, chequeno, debt, urd, '', urd_gold, urd_gold, urd_silver, urd_silver, other, 'NEFT', date.today()))

def Shree_gen(num):
    for i in range(num):
        name='shreedummy'+str(i)
        amount=random.randint(100, 10000)
        if random.randint(0,1)==1:
            Bill_store(Bill(name, '', '', '', '', 0.0, 0.0, 0.0, 0.0, 'Misc plus', amount, amount, 0, None, 0, None, 0, '', 0, 0, '', 0.0, 0.0,
            0.0, 0.0, 0, '', date.today()))
        else:
            Bill_store(Bill(name, '', '', '', '', 0.0, 0.0, 0.0, 0.0, 'Misc minus', amount, amount, 0, None, 0, None, 0, '', 0, 0, '', 0.0, 0.0,
            0.0, 0.0, 0, '', date.today()))

def VC_gen(num):
    for i in range(num):
        name='VCdummy'+str(i)
        ph_num=random.randint(1000000000, 9999999999)
        gold_grwt, gold_ntwt, silver_grwt, silver_ntwt= 0.0, 0.0, 0.0, 0.0
        amount=5000 if random.randint(0, 10)!=1 else 5000+random.randint(100, 10000)
        finamount=amount
        purity=''
        temp_card, temp_upi=None, None
        payment_num=random.randint(1,6)
        payments=random.sample(list(range(6)), payment_num)
        chequeno=''
        cash, card, upi, cheque, debt, other= 0, 0, 0, 0, 0, 0
        urd, urd_gold, urd_silver =0, 0.0, 0.0
        if amount>5000:
            if random.randint(0,1)==1:
                tempgold_grwt=round(random.random()*10, 3)
                gold_ntwt+=tempgold_grwt if random.randint(0,10)!=1 else round(tempgold_grwt*random.random(), 3)
                temp_purity='916' if random.randint(0,10)!=1 else '750'
                purity=', '.join(purity, temp_purity)
                gold_grwt+=tempgold_grwt
            else:
                tempsilver_grwt=round(random.random()*10, 3)
                purity=', '.join([purity, '70%'])
                silver_ntwt+=tempsilver_grwt if random.randint(0,10)!=1 else round(tempsilver_grwt*random.random(), 3)
                silver_grwt+=tempsilver_grwt
        for idx, items in enumerate(payments):
            if items==0:
                if idx < payment_num-1:
                    cash=round(amount*random.random())
                    amount-=cash
                if idx==payment_num-1:
                    cash=amount
                    amount=0
            elif items==1:
                if idx < payment_num-1:
                    card=round(amount*random.random())
                    temp_card=cardtype[random.randint(0,3)]
                    amount-=card
                if idx==payment_num-1:
                    card=amount
                    temp_card=cardtype[random.randint(0,3)]
                    amount-=card
            elif items==2:
                if idx < payment_num-1:
                    upi=round(amount*random.random())
                    temp_upi=upitype[random.randint(0,2)]
                    amount-=upi
                if idx == payment_num-1:
                    upi=amount
                    temp_upi=upitype[random.randint(0,2)]
                    amount=0
            elif items==3:
                if idx < payment_num-1:
                    cheque=round(amount*random.random())
                    chequeno=random.randint(100000,999999)
                    amount-=cheque
                if idx == payment_num-1:
                    cheque=amount
                    chequeno=random.randint(100000,999999)
                    amount=0
            elif items==4:
                if idx < payment_num-1:
                    debt=round(amount*random.random())
                    amount-=debt
                if idx == payment_num-1:
                    debt=amount
                    amount=0
            elif items==5:
                if idx < payment_num-1:
                    urd=round(amount*random.random())
                    if random.randint(0,1)==0:
                        urd_gold=urd/5000
                    else:
                        urd_silver=urd/4000
                if idx== payment_num-1:
                    urd=amount
                    amount=0
                    if random.randint(0,1)==0:
                        urd_gold=urd/5000
                    else:
                        urd_silver=urd/4000
        purity=purity[2:]
        Bill_store(Bill(name, ph_num, '', '', purity, gold_grwt, gold_ntwt, silver_grwt, silver_ntwt, 'VC', finamount, cash, card, temp_card, 
        upi, temp_upi, cheque, chequeno, debt, urd, '', urd_gold, urd_gold, urd_silver, urd_silver, other, 'NEFT', date.today()))

def GP_gen(num):
    for i in range(num):
        name='GPdummy'+str(i)
        ph_num=random.randint(1000000000, 9999999999)
        grwt=round(random.random()*10,3)
        ntwt= grwt if random.randint(0, 10) else round(grwt*random.random(), 3)
        amount=ntwt*5000
        Bill_store(Bill(name, ph_num, '', '', '', 0.0, 0.0, 0.0, 0.0, 'Gold Purchase', amount, amount, 0, None, 0, None, 0, '', 0, 0, '',
        grwt, ntwt, 0.0, 0.0, 0, '', date.today()))

def SP_gen(num):
    for i in range(num):
        name='SPdummy'+str(i)
        ph_num='SPdummy'+str(i)
        grwt=round(random.random()*10, 3)
        ntwt= grwt if random.randint(0, 10) else round(grwt*random.random(), 3)
        amount=ntwt*5000
        Bill_store(Bill(name, ph_num, '', '', '', 0.0, 0.0, 0.0, 0.0, 'Silver Purchase', amount, amount, 0, None, 0, None, 0, '', 0, 0, '',
        0.0, 0.0, grwt, ntwt, 0, '', date.today()))
        
if __name__=='__main__':
    # GS_gen(10)
    # SS_gen(5)
    # Old_Order_gen(5)
    # New_Order_gen(5)
    # Shree_gen(5)
    VC_gen(5)
    GP_gen(5)
    SP_gen(5)
