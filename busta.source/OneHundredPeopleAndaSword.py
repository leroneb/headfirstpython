'''
Created on Jun 27, 2017

@author: ubuntu
'''
# There are 100 people standing in a circle in an order 1 to 100. No. 1 has a sword. 
# He kills the next person (i.e. No. 2) and gives the sword to the next (i.e. No. 3). 
# All people do the same until only 1 survives. Which number survives at the last?
# There are 100 people starting from 1 to 100.

people = []
#people = [5]

for num in range(1,101,1):
    people.append(num)
    
while (len(people) > 1):
    i = 0
    for person in people:
        if len(people) > (i+1):
            people.remove(people[i+1])
            i = i+1
        else:
            i = 0
            people.remove(people[0])
            
for person in people:
     print('The last remaining swordman is swordman #' + str(person))
    
