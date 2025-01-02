# This program is an example of a bank account using class and objects.
class Bankb:
    def __init__(self,balance,accno):
        self.balance = balance
        self.accno = accno

    def disp(self):
        print("Account details:")
        print("Account number:",self.accno)
        print("Balance:",self.balance)

    def credit(self,amount):
        self.balance += amount
        print("Amount",amount,"credited successfully!")
        print("New balance:",self.balance)

    def debit(self,amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print("Amount",amount,"debited successfully!")
            print("New balance:",self.balance)

a = int(input("Enter the balance:"))
b = int(input("Enter the account number:"))
acc1 = Bankb(a,b)

acc1.disp()

print("\nDo you want to continue?")
print("1.Continue\n2.Exit\n")
kh = int(input("Enter your choice:"))
if kh == 1:
  while True:
    print("Do you want to credit or debit?\n1.Credit\n2.Debit\n3.Exit")
    ch = int(input("Enter your choice:\n"))
    if ch == 1:
        c = int(input("Enter the amount to be credited:"))
        acc1.credit(c)
    elif ch == 2:
        d = int(input("Enter the amount to be debited:"))
        acc1.debit(d)
    elif ch == 3:
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
        continue
else:
    print("Exiting...")
