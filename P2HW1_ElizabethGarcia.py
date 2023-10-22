#Add on to P1HW2
#10/14/2023
#CTI-110 P2HW1-Travel
#Elizabeth Garcia
#




print("This program calculates and displays travel expenses")
print()
budget = float(input("Enter Budget: "))
print()
destination = input("Enter your travel destination:")
print()
gas = float(input("How much do you think you will spend on gas? "))
print()
hotel = float(input("Approximately, how much will you need for accomodation/hotel? "))
print()
food = float(input("Last, how much do you need for food? "))
print()


print('-----------Travel Expenses-----------')
print(f"Location:",'       ',destination)
print(f'Initial Budget: ','  $',budget)
print(f'Fuel:','             $',gas)
print(f'Accomodation:','     $', hotel)
print(f'Food:','             $',food)
print('------------------------------------')
print()
print('Remaining Balance:',budget-gas-hotel-food)
