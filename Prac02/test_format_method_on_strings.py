__author__ = 'Cue'

s1 = 'Chicken & Egg'
num1 = 123.456

print('s1 has',len(s1),'characters')
print('s1=' + s1)
print()
print('Use 20 spaces with the format of 20s')
print('s1={t:20s}, num1={n:.2f}'.format(t=s1, n=num1))
print('s1={:20s}, num1={:.2f}'.format(s1, num1))

print('Use 20 spaces with right justify with the format of 20s')
print('s1={t:>20s}, num1={n:.2f}'.format(t=s1, n=num1))

