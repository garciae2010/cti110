# Grades
#CIT-110
#P2HW2-List
#Elizabeth Garcia
#10/21/2023
#

grades = []
module1 = float(input("Enter grade for Module 1: "))
grades.append(module1)
module2 = float(input("Enter grade for Module 2: "))
grades.append(module2)
module3 = float(input("Enter grade for Module 3: "))
grades.append(module3)
module4 = float(input("Enter grade for Module 4: "))
grades.append(module4)
module5 = float(input("Enter grade for Module 5: "))
grades.append(module5)
module6 = float(input("Enter grade for Module 6: "))
grades.append(module6)



avg = (65.5+88+78.5+90+61+92)/6

print('--------------Results----------')
print('Lowest Grade:',  module1)
print('Highest Grade:', module6)
print('Sum of Grades:',sum(grades))
print(f'Average:       {avg:.2f}')





