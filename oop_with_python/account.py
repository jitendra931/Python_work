
#  question 2. Create Account class with 2 attributes - balance & account no. 
# Create methods for debit, credit & printing the balance

class account:

    def __init__(self,acc,bal):
        self.account_no = acc
        self.balance = bal

    def debit(self,amount):
        self.balance -= amount
        print("Rs.",amount,"was debited.")
        print("Total balance :",self.get_balance())
    
    def credit(self, amount):
        self.balance += amount
        print("Rs.",amount,"was credited.")
        print("Total balance :",self.get_balance())
    
    def get_balance(self):
        return self.balance

acc = account("50400100046212", 50000)
print(acc.account_no)
print(acc.balance)

acc.debit(1000)
acc.credit(800)
