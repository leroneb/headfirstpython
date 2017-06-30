vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Please enter a word to search for vowels: ")
for letter in word:
    if letter in vowels:
        print(letter)
        

found = []
# Now how to get the unique Return using lists
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for vowel in found: 
    print(vowel)