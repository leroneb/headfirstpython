#Using a dictionary, we now have an unordered key/value set of information
#

person3 = {'Name': 'Ford Perfect',
       'Gender': 'Male',
       'Occupation': 'Researcher',
       'Home Planet': 'Betelgeuse Seven' }
       

print(person3.get('Occupation'))
print(person3['Occupation'])

# Add an age
person3['Age'] = 33

print(person3)