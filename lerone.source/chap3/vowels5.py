import time

#This is really powerful, to be able to iterate though a Hash map/dictionary effortlessly

vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Please enter a word to search for vowels: ")
found = {}

for letter in word:
    if letter in vowels:
        if letter not in found:
            found[letter] = 0
        found[letter] += 1
        

print('Using items') 
start = time.time()  
for k, v in sorted(found.items()):
    print(k, 'was found' ,v, 'time(s)' )
end = time.time()   
print('Using dictionary.items() takes', end - start , 'ms')
