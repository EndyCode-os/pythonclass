class Seat: #create the seat attributes
    def __init__(self, name, seat_class, taken):
        self.name = name
        self.seat_class = seat_class
        self.taken = taken


class Airplane: #create airplane attribute and method
    def __init__(self, list_seats):
        self.list_seats = list_seats

    def display_seat(self): # display all seat and their status
        print("Seat Availability:")
        for seat in self.list_seats:
            status = "Taken" if seat.taken else "Available"
            print(f"Seat: {seat.name} | Class: {seat.seat_class} | Status: {status}")

    def book_seat(self, user_seat): # return the seat selected and the price. It also checks if the seat is available or not.
        for seat in self.list_seats:
            if seat.name == user_seat.upper():
                print(f"\nYou selected seat {seat.name}, Class: {seat.seat_class}")
                base_price = 100.00

                if seat.taken:
                    print("Seat is already taken. Please choose another.\n")
                    return seat, None

                if seat.seat_class == "Emergency":
                    confirm = input("Emergency seat. Agree to assist in emergency? (Y/N): ").upper()
                    if confirm != "Y":
                        print("You cannot select this seat without agreement.")
                        return seat, None
                    elif confirm == "Y":
                        print(f"Emergency seat. Price: $ {base_price}")

                elif seat.seat_class == "First":
                    base_price += 60
                    print(f"First Class seat. Additional $60 fee. Total price: ${base_price}")

                elif seat.seat_class == "Regular":
                    print(f"Regular seat. Price: ${base_price}")

                return (seat, base_price)

        print("Seat not found\n")
        return None, None

    def price_check(self, user_money, seat_price, seat_obj):#check price and book the flight if amount is sufficient
        if user_money >= seat_price:
            change = round(user_money - seat_price, 2)
            seat_obj.taken = True
            print(f"✅ Booking confirmed. Seat {seat_obj.name} is now reserved.")
            print(f"💵 Change returned: ${change}\n")
        else:
            print("❌ Not enough funds. Booking failed.\n")

#seat information
seat_1 = Seat("A1", "First", False)
seat_2 = Seat("A2", "First", False)
seat_3 = Seat("A3", "First", False)
seat_4 = Seat("A4", "First", False)
seat_5 = Seat("B1", "Regular", False)
seat_6 = Seat("B2", "Regular", False)
seat_7 = Seat("B3", "Regular", False)
seat_8 = Seat("B4", "Regular", False)
seat_9 = Seat("C1", "Regular", False)
seat_10 = Seat("C2", "Regular", False)
seat_11 = Seat("C3", "Regular", False)
seat_12 = Seat("C4", "Regular", False)
seat_13 = Seat("D1", "Regular", False)
seat_14 = Seat("D2", "Regular", False)
seat_15 = Seat("D3", "Regular", False)
seat_16 = Seat("D4", "Regular", False)
seat_17 = Seat("E1", "Emergency", False)
seat_18 = Seat("E2", "Emergency", False)
seat_19 = Seat("F1", "Emergency", False)
seat_20 = Seat("F2", "Emergency", False)

# create a list of seats
list_seat = [seat_1, seat_2, seat_3, seat_4, seat_5, seat_6, seat_7, seat_8, seat_9, seat_10, seat_11, seat_12, seat_13, seat_14, seat_15, seat_16, seat_17, seat_18, seat_19, seat_20]

plane = Airplane(list_seat)
start =  True

print("Welcome to our Airline\n")

while start: # start the program

    start_confirm = input("Press Y to book a seat or Q to quit: ").upper() # Ask to start the program or not
    if start_confirm == "Y":#start the program
        plane.display_seat()#display all seat
        user_seat = input("\nPlease enter the seat name you want: ") #Enter the name of the seat selected
        seat_obj, price_seat =plane.book_seat(user_seat) #return the seat selected and seat price
        #condition to avoid processing a seat already taken
        if price_seat is None:
            pass
        elif price_seat > 0:
            user_pay = float(input("Please enter the correct amount of money: "))
            plane.price_check(user_pay, price_seat, seat_obj)

    elif start_confirm == "Q": #To stop the program
        start = False
    else:
        print("Value entered is incorrect. Please choose the correct value\n")

print("Thank you for visiting and hope seeing you soon") # Bye and see you later. Have a good summer Mr. Gossai