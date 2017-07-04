import time

#This is really powerful, to be able to iterate though a Hash map/dictionary effortlessly

vowels = {'a': 0, 'e': 0, 'i': 0 , 'o': 0, 'u': 0}
word = input("Please enter a word to search for vowels: ")
for letter in word:
    if letter in vowels:
        vowels[letter] += 1
        
print(vowels)
print()
start = time.time()
for kv in sorted(vowels):
    print(kv, 'was found' ,vowels[kv], 'time(s)' )
end = time.time()
print('Using the primitive reference takes', end - start , 'ms')

print('Using items') 
start = time.time()  
for k, v in sorted(vowels.items()):
    print(k, 'was found' ,v, 'time(s)' )
end = time.time()   
print('Using dictionary.items() takes', end - start , 'ms')
