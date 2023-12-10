#CTI-110
#P4HW2- Salary Calculator
#Elizabeth Garcia
#11/27/2023
#

count = 0
total_ovt_pay =0
total_reg_pay = 0
total_gross_pay = 0

employee = input("Enter employee's name or 'Done' to terminate: ")
while employee != 'Done':
      count +=1
      hours_worked = float(input("How many hours did " +employee+ " work? "))
      
      pay_rate = float(input("What is " +employee+"'s pay rate? "))

      
      if hours_worked >40:
        ovt_pay_rate = pay_rate * 1.5
        reg_hours_pay = pay_rate * 40
        ovt_hrs = hours_worked - 40
        ovt_pay = ovt_hrs * ovt_pay_rate
        gross_pay = reg_hours_pay + ovt_pay

      else:
        hours_worked <=40
        reg_hours_pay = pay_rate * hours_worked
        ovt_hrs = 0
        ovt_pay = 0
        gross_pay = reg_hours_pay + ovt_pay

      total_ovt_pay = total_ovt_pay + ovt_pay
      total_reg_pay = total_reg_pay + reg_hours_pay
      total_gross_pay = total_gross_pay + gross_pay



      print('--------------------------------------')
      print('Employee name:   ')
      print()
      print('Hours worked     Pay Rate    OverTime    OverTime Pay     RegHour Pay     Gross Pay')
      print('----------------------------------------------------------------------------------------')


      print(f'{hours_worked:<15.1f}{pay_rate:<15.1f}{ovt_hrs:<15.1f}{ovt_pay:<15.2f}{reg_hours_pay:<15.2f}{gross_pay:<15.2f}')
      employee=input("Enter employee's name or 'Done' to terminate: ")

gross_pay = hours_worked * pay_rate



ovt_time = []
reg_hours_pay = []
gross_pay = []

print('Total number of eployees entered: $', str(count))
print('Total amount paid for overtime: $' ,total_ovt_pay)
print('Total amount paid for regular hours: $', total_reg_pay)
print('Total amount paid in gross: $', total_gross_pay)
