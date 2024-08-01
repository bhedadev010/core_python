class Bank:

    def openAccount(self, acno, cname, bala):
        self.a = acno
        self.c = cname
        self.b = bala
        print(f"Hello {cname}, Your account number is {acno}, Your balance is {bala}")



    def deposit(self, amount):
        self.b += amount

    def withdraw(self, amount):
        if amount <= self.b:
            self.b -= amount
        else:
            print("Insufficient Balance")

    def checkBalance(self):
        print("Balance :", self.b)


b1 = Bank()
b1.openAccount(101, "Dev", 2000)


while True:
    print("*" * 40)
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Balance")
    print("4. Exit")
    print("*"*40)

    choice = int(input("Enter choice :"))

    if choice == 1:
        dep = int(input("Enter Amount You Want To Deposit :"))
        b1.deposit(dep)
        print("*" * 40)

    elif choice == 2:
        wit = int(input("Enter Amount You Want To Withdraw :"))
        b1.withdraw(wit)
        print("*" * 40)

    elif choice == 3:
        print("Current Balance : \n")
        b1.checkBalance()
        print("*" * 40)

    elif choice == 4:
        print("Thank you for using our services")
        print("*" * 40)
        break

    else:
        print("Invalid Choice")
        print("*" * 40)