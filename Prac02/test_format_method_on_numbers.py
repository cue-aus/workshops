__author__ = 'Cue'

num1 = 123
print('num1='+ str(num1))
print('output 2 leading spaces with the format of 5d')
print('num1={n:5d}'.format(n=num1))
print('{:5d}'.format(num1))

num2 = 123.456
print()
print('num2='+ str(num2))
print('output 2 decimal places with the format of .2f')
print('num2={n:.2f}'.format(n=num2))
print('output the number with 4 spaces, \
a dot and 2 decimal places with the format of 7.2f')
print('num2={n:7.2f}'.format(n=num2))

item = '128GB SSD'
price = 123.50
print('{0:10s}costs ${1:<7.2f}AUD'.format(item, price))
print('{0:10s}costs ${1:7.2f}AUD'.format(item, price))

x = "Bob"
y = 34.9993
print("!{0:8} owes {1:.1f} to {0}.".format(x, y))



