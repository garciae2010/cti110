
##Travel Expenses
##09/17/2023
##CTI-110 P1HW2 - Travel Expences
##Elizabeth Garcia


print("This program calculates and displays travel expenses")
print()
budget = float(input("Enter Budget: "))
print()
destination = input("Enter your travel destination:")
print()
gas = float(input("How much do you think you will spend on gas?"))
print()
hotel = float(input("Approximately, how much will you need for accomodation/hotel?"))
print()
food = float(input("Last, how much do you need for food?"))
print()


print('-----------Travel Expenses-----------')
print("Location:",destination)
print('Initial Budget:',budget)
print()
print('Fuel:',gas)
print('Accomodation:',hotel)
print('Food:',food)
print()
print('Remaining Balance:',budget-gas-hotel-food)
