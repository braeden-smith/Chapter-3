# Braeden Smith Chapter 3 Exercise 1

'''
Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
Enter Hours: 45
Enter Rate: 10
Pay: 475.0
'''

hours = float(input('Enter how many hours have you worked:' ))
rate = float(input('Enter how much your hourly wage is:' ))
if hours > 40:
  extra = float(hours) - 40
else:
    extra = 0
extra_pay = 0.5 * float(rate) * extra

pay = float(hours) * float(rate) + extra_pay

print ('Pay: '),
print pay
