vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Please enter a word to search for vowels: ")
for letter in word:
    if letter in vowels:
        print(letter)
        
aSet = set()        
# Now how to get the unique Return using set
for letter in word:
    if letter in vowels:
        #add to set
        aSet.add(letter)
for vowel in aSet: 
    print(vowel)