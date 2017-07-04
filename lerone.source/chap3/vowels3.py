## Using a SET over a list

# vowels = {'a', 'e', 'e', 'i', 'o', 'u', 'u'} or vowels = set('aeeiouu')
vowels = set('aeeiouu')
print(sorted(vowels))
word = input("Please enter a word to search for vowels: ")
print(vowels.intersection(set(word)))
        
