import datetime
class category:
    def __init__(self, name):
        self.name = name
        self.ledger=[]     #it is a list, it will store all the objects of an existing category.

    def deposit (self, amount, description = "", date = None):
        transaction = {
            "amount": amount,
            "description": description,
            "date": datetime.date.today()
        } 
        self.ledger.append(transaction)
       # if description:
       #     print(date)
       #     print("transaction succesfully performed")
       #     print(transaction, amount)

    def withdraw (self, amount, description ="", date=None):
        if self.check_funds(amount):
            transaction = {"amount": -amount, "description": description, "date":date}
            self.ledger.append(transaction)
            return True
        return False
    
    def get_balance(self):
        balance = 0
        for transaction in self.ledger:
            balance += transaction["amount"]
            return balance 
        
    def check_funds(self,amount):
        return amount <= self.get_balance() #amount is the amount in the imput // get balance is the amount stered previously.
    
    def transfer (self, amount, destination_category):
        if self.check_funds(amount):
            if destination_category not in categories:
                categories[destination_category] = category(destination_category)
            if amount <= self.get_balance():
                self.ledger.append({"amount": - amount, "description": f"Transfer to {destination_category}" })
                categories[destination_category].ledger.append({"amount": amount, "description": f"Transfer from {self.name}" })
                return True
            else:
                print("Insufficient fund to transfer.")
                return False
        else:
            print("Not enough funds to perform transfer.")
            return False
        
    def __str__(self):
        title = f"{self.name.center(30, '*')}\n"
        items=""
        total=0
 


        for transaction in self.ledger:
            description = transaction["description"][:23]
            amount =  transaction ["amount"]
            total += amount
            items += f"{description:<23}{amount:>7.2f}\n"
        totalultm = float(total)

        output = "{}{} Total: {:.2f}".format(title, items, totalultm)
        return output

def create_spend_chart(categories):
    #total_withdrawals = sum(category.get_balance() for category_instance in categories.values())
    #------------------------------------------------------------------
    category_instances = categories.values()
    total_withdrawals = 0
    for category_instance in category_instances:
        withdrawals_for_category = category_instance.get_balance()
        total_withdrawals+= withdrawals_for_category

    #spent_percentages = [category.get_balance()/ total_withdrawals *100 for category_instance in categories.values() ]
    #----------------------------------------------------------------
    category_instances = categories.values()
    spent_percentages = []
    for category_instance in category_instances:
        withdrawals_for_category = category_instance.get_balance()
        spent_percentage = withdrawals_for_category / total_withdrawals *100
        spent_percentages.append(spent_percentage)


    chart = "Percentage spent by category\n"
    for i in range (100, -10, -10):
        chart += f"{i:3}| "
        for percentage in spent_percentages:
            if percentage >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

#    max_length = max (len (category.name)for category_instance in categories.values())
#--------------------------------------------------------------------------------
    category_instances = categories.values()
    max_length =0
    for category_instance in category_instances:
        category_name_length = len (category_instance.name)
        if category_name_length>max_length:
            max_length = category_name_length

    for i in range (max_length):
        chart += "    "
        for name in categories.keys():
            if i < len (name):
                chart += name[i] + "  "
            else:
                chart += "  "

        chart += "\n"

        return chart

categories = {}



def create_category():
    category_name = gtng
    categories[category_name] = category (category_name)

def operate_category(category_name):
    if category_name in categories:
        category = categories [category_name]



def operate_category(category_name):
    category_name = gtng
    category_action = input("Enter the category action (Deposit/withdraw/transfer/balance): ")
    category_action= category_action.lower()


    if category_name in categories:
        category = categories[category_name]
        
        if category_action == "deposit":
            amount = float (input("Enter the amount: "))
            description = input("enter description: ")
            category.deposit(amount, description)
            print(f"successfully deposited {amount} to {category_name} category.") 
        elif category_action == "withdraw":
            amount = float (input("Enter the amount: "))
            description = input("enter description: ")
            if category.withdraw(amount, description):
                print(f"Succesfully withdrew {amount} from {category_name} category.")
            else:
                print("Isufficient funds to perform withdrawal.")
        elif category_action=="transfer":
            amount = float (input("Enter the amount: "))
            destination_category = input("Enter the destination category name: ")
            destination_category = destination_category.lower()
            print("a donde va", destination_category)
            print("de donde viene",category_name)
            if category.transfer(amount,destination_category):
                print(f"Succefully transferred {amount} from {category_name}")
            else:
                print("insufficient funds to perform transfer.")
        elif category_action== "balance":
            print(categories[category_name])  # Print the category details
            
        else:
            print("Invalid category action.")
    else:
        print("Category not found.")
    print(categories)
    print(create_spend_chart(categories))


while True:
    action = input("Enter the category action (create/operate/Exit): ")
    action = action.lower()
    if action== "create":
        gtng = input("category: Food/Clothing/entertainment or  cancel: ")
        gtng = gtng.lower()
        if "food" in gtng or  "clothing" in gtng or "entertainment" in gtng: 
            create_category()
            operate_category(gtng)
        if "cancel" in gtng:
            break
        else:
            altac=input("Would you like to perform another action? yes/no: ")
            if altac == "no":
                break
            elif altac == "yes":
                continue
            else:
                print("Sorry, action not recongized, try again.")
            continue
    elif action == "operate":
        category_name1 = input("Enter the name of the category: ")
        category_name1 = category_name1.lower()
        print("operate I'm here 1", category_name1)
        if category_name1 in categories:
           gtng=category_name1
           operate_category(categories[category_name1])
           print(categories[category_name1])  # Print the category details
        else:
            print("Category not found, create the category first")
            continue
    elif action== "exit":
        break
    else:
        print("invalid action, please try again.")
        continue


print("Exit program")



