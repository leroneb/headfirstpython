# dict of people pg 137
import pprint
people = {}

people['Ford'] = {'Name': 'Ford Perfect',
       'Gender': 'Male',
       'Occupation': 'Researcher',
       'Home Planet': 'Betelgeuse Seven' }

people['Arthur'] = {'Name': 'Arthur Dent',
       'Gender': 'Male',
       'Occupation': 'Sandwich-Maker',
       'Home Planet': 'Earth' }

people['Trillian'] = {'Name': 'Tricia McMillan',
       'Gender': 'Female',
       'Occupation': 'Mathematician',
       'Home Planet': 'Earth' }

people['Robot'] = {'Name': 'Marvin',
       'Gender': 'Unknown',
       'Occupation': 'Paranoid Android',
       'Home Planet': 'Unknown' }

pprint.pprint(people)

# What does Arthur do? We use double square brackets to access row and column of the data we need
print('Arthur is a:' , people['Arthur']['Occupation'])
