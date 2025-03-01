def menu_display():
    print(" Taco Palace Menu\n"
          "1. Taco\n"
          "2. Burrito\n"
          "3. Nachos\n"
          "4. Soft Drink\n"
          "5.Quit\n")

def food_price(option):
    price = [5.00, 6.45, 3.39, 2.45]
    return price[option-1]


print('Welcome to Taco Palace, please view the menu below and enter the number that represents your selection\n')

total_price = 0
user_selection = 0
food_ordered = []

while user_selection != 5:

    menu_display()

    user_selection = int(input("User entered: "))

    if user_selection == 1:
        print("You selected Taco\n")
        total_price += food_price(user_selection)
        food_ordered.append("Taco")

    elif user_selection == 2:
        print ("You selected a Burrito\n")
        total_price += food_price(user_selection)
        food_ordered.append("Burrito")

    elif user_selection == 3:
        print ("You selected a Nachos\n")
        total_price += food_price(user_selection)
        food_ordered.append("Nachos")

    elif user_selection == 4:
        print ("You selected a Soft Drink\n")
        total_price += food_price(user_selection)
        food_ordered.append("Soft Drink")

print("\nYou ordered:")

for food in food_ordered:
    print(food)

print ("your total is {}".format(total_price))



