__author__ = 'Cue'

vowels = ['a', 'e', 'i', 'o', 'u']
vowel_count = 0

name = input('Enter your name: ')
l = len(name)
for i in range(0, l):
    if name[i].lower() in vowels:
        vowel_count += 1
print('Out of {} letters, {} has {} vowels'.format(l, name, vowel_count))
