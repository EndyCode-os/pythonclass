def area(radius):
    area_circle = 3.14 * radius ** 2
    return area_circle

def total_due(money, tax):
    total_money = money + money* (tax/100)
    return total_money

def conversion(fahrenheit):
    conversion_celsius = (fahrenheit - 32) * (5 / 9)
    return conversion_celsius

print("Test Data - Area of a Circle")
r = int(input("Enter the radius: "))
print("The area of the circle is ", area(r), '\n')

print("Test Data - Taxes")
myMoney = int(input("Enter your amount of money: "))
myTax = int(input("Enter tax: "))
print("The total due is $", total_due(myMoney, myTax), "\n" )

print("Test Data - Temperature")
temperature = int(input("Enter the temperature (F): "))
print("The temperature is", conversion(temperature), "C")



