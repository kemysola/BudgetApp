class Budget:
    def __init__(self,category,balance =100000):
        self.category = category
        self.balance = balance
    
#The deposit method.......................
    def deposit(self):
        amount_deposit = int(input('Kindly enter the amount: \n'))
        if(amount_deposit <= 0):
            print('not valid')
            self.deposit()
        else:
            print(f'\n Transaction Successful, you have deposited {amount_deposit} into the {self.category} \n'.title())
            self.balance = amount_deposit
            print(f'Your current budget balance for {self.category} is #{self.balance + amount_deposit :#,.2f} \n'.title())
        return self.balance   

#The withdrawal method ...................
    def withdrawal(self):
        amount_withdrawn = int(input('How much would you  like to withdraw? \n'))
        if(amount_withdrawn <= 0):
            print('Kindly enter a valid amount')
            self.withdrawal()

        elif(amount_withdrawn > self.balance):
            print('You do not have sufficient funds to carry on this transactions')
            self.withdrawal() 
        else:
            print(f'Transaction Successful, you have withdrawn {amount_withdrawn:#,.2f} from the {self.category} \n'.title())
            print(f'Your current budget for {self.category} is #{self.balance - amount_withdrawn:#,.2f} \n'.title())
        return self.balance

#The balance method ........................
    def user_balance(self):
        print(f'Your available balance is {self.balance:#,.2f}\n'.title())
        return self.balance

#The transfer method........................
    def transfer(self):
        amount_transfered = int(input('Kindly enter the amount you would like to transfer : \n\t'.title()))
        if(amount_transfered > self.balance):
            print('Sorry you do not have sufficient funds for this transaction')
            print('Please try again')
            self.transfer()
        else:
                transfer_category = int(input('Kindly enter the category you would like to transfer into:  \n\t 1.Food\n\t 2.Clothing\n\t 3.Entertainment\n\t \n'.title()))
                categories =['Food Budget','Clothing Budget','Entertainment Budget']
                if(transfer_category == 1):

                    print(f'transfered to {amount_transfered:#,.2f} into the {categories[0]}  \n'.title())
                    print(f'Your new balance is {self.balance - amount_transfered:#,.2f}.\n'.title())
                elif(transfer_category ==2): 
                    print(f'transfered to {amount_transfered:#,.2f} into the {categories[1]}  \n'.title())
                    print(f'Your new balance is {self.balance - amount_transfered:#,.2f}.\n')
                
                elif(transfer_category ==3): 
                    print(f'transfered to {amount_transfered:#,.2f} into the {categories[2]}  \n'.title())
                    print(f'Your new balance is {self.balance - amount_transfered:#,.2f}.\n'.title())
                else: 
                    print('Kindly enter a valid option')
                    self.transfer()
        return self.balance
        
#instance of the object........
food = Budget('Food Budget')
clothing = Budget('Clothing Budget')
entertainment = Budget('Entertainment Budget')


#To test the methods#

#food.deposit()
#clothing.deposit()
entertainment.transfer()
#food.balance()
#food.withdrawal()




