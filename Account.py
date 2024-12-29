class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account = acc

    def debit (self,amount):
        self.balance -= amount
        print("Rs.",amount, "was debitd")
        print("total balance= ",self.get_balance())


    def credit (self,amount):
        self.balance += amount
        print("Rs.",amount,"was credited")
        print("total balance= ",self.get_balance())

    def get_balance(self):
        return self.balance             

acc1=Account(10000,89000)
acc1.debit(1000)
acc1.credit(40000)
acc1.credit(50000)
acc1.debit(20000)
acc1.credit(1000)