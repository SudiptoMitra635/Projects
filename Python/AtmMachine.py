class Atm:
    # constructor
    def __init__(self): 
        # this function will be called when a object of this class will be created
        self.pin = ''
        self.balance = 0
        self.menu()
    def menu(self):
        user_input = input("""
            Hi how can I help you?
            1. Press 1 to create pin
            2. Press 2 to change pin
            3. Press 3 to check balance
            4. Press 4 to withdraw
            5. Anything else to exit
            """)
        if user_input == '1':
            #create pin
            self.create_pin()
        elif user_input == '2':
            #check change pin
            self.change_pin()
        elif user_input == '3':
            #check balance
            self.check_balance()
        elif user_input == '4':
            #withdraw
            self.withdraw()
        else:
            exit()
    
    def create_pin(self):
        user_pin = input('Enter your pin: ')
        self.pin = user_pin

        user_balance = int(input('Enter your balance: '))
        self.balance = user_balance

        print('Pin created successfully!')
        self.menu()
    
    def change_pin(self):
        old_pin = input('Enter old pin:')
        if old_pin == self.pin:
            #change the pin
            new_pin = input('Enter new pin: ')
            self.pin = new_pin

        else:
            print('Tumse na ho payega')
        self.menu()
    
    def check_balance(self):
        user_pin = input('Enter your pin: ')
        if user_pin == self.pin:
            print('your balance is ', self.balance)
        else:
            print('Chal nikal dkbose')
        self.menu()

    def withdraw(self):
        user_pin = input('Enter your pin: ')
        if user_pin == self.pin:
            withdrawl_amount = int(input('Enter the amount: '))
            if withdrawl_amount <= self.balance:
                self.balance -= withdrawl_amount
                print('Withdrawl successfully')
                print('Balance:', self.balance)
            else:
                print('Haat gareeb!')
        else:
            print('Chal sale chor')
        self.menu()

obj = Atm()
