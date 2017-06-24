'''
Created on Jun 24, 2017

@author: ubuntu
'''

vowels = ['a', 'e', 'i', 'o', 'u']

word = input("enter word:")

found = []

for letter in word:
    if letter in vowels:
        found.append(letter)
        
if len(found) > 0:
    print("Here are the vowels:")
    for letter in found:
        print(letter)
else:
    print("There are no vowels in " + word)