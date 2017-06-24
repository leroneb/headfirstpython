#MEET PYTHON CHAP 1
#####################################
print("hello" )
if 43 > 42:
    print("Don't panic!")
    print()


#List of movies, or array of movies
movies = ["The Holy Grail",
          "The life of Brian",
          "The Meaning of Life"]

#easier to print than Java
print(movies)

#lists are like arrays with the bottom/first item being item #0
print(movies[0])
print(len(movies))

#append movie
movies.append("Horse Raider")
print(movies)

movies.pop() #Pop last item off the list
print(movies)

movies.extend(["Tomb Raider", "Warrior Cry"])
print(movies)

#find and remove item
movies.remove("Tomb Raider")
movies.insert(0, "Tomb Fighter")
print(movies)

#Inserting date of the films
movies.insert(1, 2017)
movies.insert(3, 1975)
movies.insert(5, 1979)
movies.insert(7, 1983)
movies.insert(9, 1999)
print(movies)

#Iterating over a list
print()
for eachMovie in movies:
    print(eachMovie)

movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
          ["Graham Chapman",
           ["Michael Palin", "John Cleese", "Eric Idle"]]]

# Find Michael Palin in the third list
print()
print(movies[4][1][0])
print(movies)

#The for loop prints each item of the outer list once - it sees the inner list as just another list item
for eachMovie in movies:
    print(eachMovie)

# For each item check if it is a list and process it before moving onto the next list item
print()
for eachMovie in movies:
    # list processing code is called a suite
    if isinstance(eachMovie, list):
        for isItem in eachMovie:
            print(isItem)
    else:
        print(eachMovie)
print()

# Better but the 3rd list for supporting actors not being processed.
# So now we create our own named suite of code - a recursive function
def print_nesters(the_list):
    for list_item in the_list:
        if isinstance(list_item, list):
            print_nesters(list_item)
        else:
            print(list_item)


print_nesters(movies)
