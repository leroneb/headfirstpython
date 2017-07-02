#There are 100 people standing in a circle in an order 1 to 100. 
#No. 1 has a sword. He kills the next person (i.e. No. 2) and 
#gives the sword to the next (i.e. No. 3). 
#All people do the same until only 1 survives. Which number survives at the last?
#There are 100 people starting from 1 to 100.

people = list()

# Put 100 people in the list
for people_id in range(1, 101, 1):
    people.append(people_id)

index = 0
rounds = 0

while len(people) != 1:
    index = 0
    for person in people:            
        # have them kill the next
        thisperson = people[index]
        
        # Anytime that the number of people is eq or 
        #larger than index + 1 we reset the cycle of killing
        index = (index + 1) % len(people)
        
        nextperson = people[index]
        people.remove(nextperson)
    rounds = rounds + 1

print("There were " + str(rounds) + " rounds of killing.")
print(people)
