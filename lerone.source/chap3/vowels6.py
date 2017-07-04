import time

#This is really powerful, to be able to iterate though a Hash map/dictionary effortlessly
# Using set default to replace the common if/not in statements
vowels = {'a', 'e', 'i', 'o', 'u'}
word = input("Please enter a word to search for vowels: ")
found = {}

for letter in word:
    if letter in vowels:
        # Initialize(if needed)
        found.setdefault(letter, 0)
        found[letter] += 1
        
print('Using items') 
start = time.time()  
for k, v in sorted(found.items()):
    print(k, 'was found' ,v, 'time(s)' )
end = time.time()   
print('Using dictionary.items() takes', end - start , 'ms')
