kwHours = int(input("Enter the KW hours used:\n"))
hours = 1000

if kwHours > hours:
    total_cost = hours * 0.07633 + (kwHours-hours)*0.09259
else:
    total_cost = kwHours*0.07633

print("Amount owed is ${}".format(total_cost))

