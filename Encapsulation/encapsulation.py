#Encapsulation is a way of securing the fields by restricting direct access by 
# making them private and are accessed by public methods
class BankAccount():
    def __init__(self,name,balance,id,password):
        self.name = name # here name is a public field
        self.__balance = balance # here __balance is a private field can only be accessed directly in the class not by object
        self.__id = id
        self.__password = password
    def account_info(self): # get method to view fields
        i = input("Enter your account id: ")
        p = input("Enter your account password: ")
        if i != self.__id or p != self.__password:
            print("Invalid Input Access Denied !!!. ")
        else:
            print(f"--{self.name}'s Account Info--")
            print(f"Account Id:  {self.__id}")
            print(f"Balance : {self.__balance}")
    def deposit(self,amount): # set method to alter the value of fields
        i = input("Enter your account id: ")
        p = input("Enter your account password: ")
        if i != self.__id or p != self.__password:
            print("Invalid Input Access Denied !!!. ")
        else: 
            if amount > 0:
                self.__balance += amount
                print("Deposite Successfull")
                print(f"Current Total Balance: {self.__balance}")
            else:
                print("Deposite UnSuccessfull due to Invalid Amount")
    def withdraw(self,amount):  # set method to alter the value of fields        
        i = input("Enter your account id: ")
        p = input("Enter your account password: ")
        if i != self.__id or p != self.__password:
            print("Invalid Input Access Denied !!!. ")
        else: 
            if amount > 0 and amount <= self.__balance:
                self.__balance -= amount
                print("Withdraw Successfull")
                print(f"Current Total Balace: {self.__balance}")
            else:
                print("Withdraw UnSuccessfull due to Invalid Amount")

A = BankAccount("Umer",1000,"11111","1234")
# print(A.__balance) will cause error as it is private can't directly be accessed
A.account_info()
A.deposit(2000)
A.withdraw(549)
A.withdraw(-12)
A.account_info()
