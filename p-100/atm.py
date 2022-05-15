class Bank(object):
    def __init__(self, branch, card_number, pin_number,):
        self.branch = branch
        self.card_number =card_number 
        self.pipin_number =pin_number

    def withdraw (self):
        print("You can withdraw your money")
    def balance (self):
        print("you have ₹ 50,00,000 in your account")
    
sbi = Bank("gurgaon", "123456", "654321")

print(sbi.withdraw())