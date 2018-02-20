#Braeden Smith Chapter 3 Excercise 3

'''
Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following table:
Score   Grade
>= 0.9     A
>= 0.8     B
>= 0.7     C
>= 0.6     D
< 0.6    F
'''

try:
  if num >=1.00000001:
    print('Error: only numbers 0.0 to 1.0')
  elif num >= .9:
    print('This grade is an A')
  elif num >= .8:
    print('This grade is an B')
  elif num >= .7:
    print('This grade is an C')
  elif num >= .6:
    print('This grade is an D')
  elif num <= .59:
    print('This grade is an F')
  elif num >= 0:
    print('Error')
except:
  print ('error_msg_invalid')
  num = input('Enter a score between 0.0 and 1.0: ')
