class calcROI():
    def __init__(self,monthly_income, total_expenses, closing_cost, cash_difference):
        self.monthly_income = 0
        self.total_expenses = 0
        self.closing_cost = 0
        self.cash_difference = 0
    
    def tell_income(self):
        print("Please respond to the following questions with numeric responses or type 'quit' to end the questionare.")
        response = input("How much would you charge your tenants per month in rent? ($): ")
        if response.lower() == "quit":
            raise QuitException
        self.monthly_income = float(response)
    
    def expense(self):
        expense_types = ["property taxs","insurance","basic utilities","hoa","lawn care","saving for possible vacancy","repairs", "saving for renovations", "property managment","mortgage payment"]
       
        self.total_expenses = 0

        for expense in expense_types:
            while True:
                current_expense = input(f"Enter estimated monthly cost of {expense}  ($): ")
                
                if current_expense.lower() == "quit":
                    raise QuitException
                
                try:
                    self.total_expenses += float(current_expense)
                    break
                except ValueError:
                    print("Invalid input. Please enter a numeric value or type 'quit' to exit.")
                
            
        print(f"Total estimated expenses: ${self.total_expenses:.2f}")
    
    def cashFlow(self):
        self.cash_difference = self.monthly_income - self.total_expenses
        return f"From out calculations, your monthly cash-flow is {self.cash_difference}."
    
    def calc_roi(self):
        self.closing_cost = 0
        print("To calculate your cash on cash return on investment we need to know a few more details abouth the purchase of this property.")
        sale_details=["a down payment", "closing costs", "possible repair costs", "any miscellaneous expenses"]
        for detail in sale_details:
            while True:  # Start an inner loop to keep asking for input until it's valid
                buying_details = input(f"To the best of your ability, what do you estimate you would pay for {detail} ($): ")
            
                if buying_details.lower() == "quit":
                    raise QuitException
            
                try:
                    self.closing_cost += float(buying_details)
                    break  # If input is a valid float, break out of the inner loop
                except ValueError:
                    print("Invalid input. Please enter a numeric value or type 'quit' to exit.")
        print("calculating your annual return on investment")
        roi=(self.cash_difference * 12)/self.closing_cost
        print(f"Your annual return on investment is {roi:.2f}%")
        

calculate = calcROI(1,1,1,1)

class QuitException(Exception):
    pass

def run():
    print("Hello, Thank you for choosing us to help you decide if this investment is worth it.")
    while True:
        response = input("Please type 'begin' to start, or 'stop' to end your session: ")

        if response.lower() == "stop":
            print("Thank you, see you next time.")
            break
        elif response.lower() == "begin":
            try:
                calculate.tell_income()
                calculate.expense()
                calculate.cashFlow()
                calculate.calc_roi()
            except QuitException:
                print("Exiting session. Thank you!")
                break  # Exit the while loop upon catching the exception
        else:
            print("Invalid command, please try again.")
    
run()
        