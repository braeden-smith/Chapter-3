#Braeden Smith Chapter 3 Excericse 2

'''
Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program:
Enter Hours: 20
Enter Rate: nine
Error, please enter numeric input
Enter Hours: forty
Error, please enter numeric input
'''

try:
  hours = float(input('Enter how many hours have you worked:' ))
  float(hours)>=0
except:
  print ('Please type in numerals only.')
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
