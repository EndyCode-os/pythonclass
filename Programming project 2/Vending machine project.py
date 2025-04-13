class Beverage:

    def __init__(self, name, price):

        self.name = name
        self.price = price

class VendingMachine:

    def __init__(self, beverage_list):
        self.beverageList = beverage_list

    def display_item(self):
        n = 0
        print("Please select among the following beverages:\n")
        for beverage in self.beverageList:
            print(n,'.',beverage.name)
            n+=1
        choice = input("Select a drink by pressing the correct number: ")
        return choice

    def check_price(self, choice, money):

        remain_money = round(money - self.beverageList[choice].price, 3)

        if remain_money > 0:
            print(f"Thank you here your {self.beverageList[choice].name} and your change ${remain_money:.2f}\n")
            return False

        elif remain_money == 0:
            print(f"Thank you here your {self.beverageList[choice].name}. No change for you\n")
            return False

        else:
            print(f"\nSorry, but you broke. You have a balance of ${-1*remain_money}")
            return True



b1 = Beverage("Pepsi", 2.00)
b2 = Beverage ("Coca Cola",2.25)
b3 = Beverage("Sprite", 2.50)
b4 = Beverage ("Dr Pepper", 1.75)
b5 = Beverage ("Gatorade", 2.75)
b6 = Beverage ("Monster", 2.15)

list_beverage = [b1, b2, b3, b4, b5, b6]

machine = VendingMachine(list_beverage)

while True:

    user_choice = int(machine.display_item())

    if user_choice in range(len(list_beverage)):

        print(f"\nSelected item: {list_beverage[user_choice].name} \nPrice: ${list_beverage[user_choice].price}\n")
        user_money = float(input('Please add money:'))
        process_transaction = machine.check_price(user_choice, user_money)

        while process_transaction:

            user_decision = input("Enter R(to reset) or A(to add money): ").upper()
            if user_decision == "R":
                print(f"\nHere your ${user_money:.2f} back\n")
                process_transaction = False

            elif user_decision == "A":
                user_addMoney = float(input("Enter amount you want to add: $"))
                user_money+= user_addMoney
                process_transaction = machine.check_price(user_choice, user_money)

    else:
        print('\nPlease enter a valid number\n')
        continue
