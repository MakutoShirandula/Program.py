name = "Hello"
print(name)

name = "world"
print(name)

my_goal = "Learn python"

#Lengths

print(len(my_goal))

#INDEXING

# L e a r n   p y t h o n 
# 0 1 2 3 4 5 6 7 8 9 10 11

print(my_goal[0]) # l
print(my_goal[4]) # n

#OPERATORS

x = 4 

y = 5

print(x + y)

print(x or y)

print(x and y)

print(x > 2 and y > 2)

#Assignment operators

my_var = 5

print(my_var)

my_var += 2

print(my_var)

#Lists

favorite_games = ["scrabble", "monopoly", "Jenga"]

print(len(favorite_games))

# Indexing a List
# [scrabble, monopoly, jenga]
#     0       1          2

print(favorite_games[0])
print(favorite_games[-1])

#Slicing in Lists

print(favorite_games[1:])
print(favorite_games[:2])
print(favorite_games[::2])

favorite_games.append("clue")
print(favorite_games)

# Tuples
my_tuple = ("Hello","Hello", "Hello", "World")
print(my_tuple)

my_tuple.count("Hello")
my_tuple.count("World")

#Dictionaries

chemical_symbols = {
    "Hydrogen": "H",
    "Boron": "B",
    "Sodium": "Na",
    "Potassium": "K",
    "Iron": "Fe"
}

print(chemical_symbols["Hydrogen"])
print(chemical_symbols["Sodium"])
print(chemical_symbols["Potassium"])
print(chemical_symbols["Iron"])

print(len(chemical_symbols))

# To add another value

chemical_symbols["Zinc"] = "Zn"
chemical_symbols

# To delete a value

del chemical_symbols["Boron"]
print(chemical_symbols)

# Conditionals
score = 90
if score < 80:
    print("Congratulations! You won")

name == "Gina"    
if name == "Nora":
     print("Is Nora!")
else:
     print("Hey! your name is Not Nora")

# use of Elif

x = 6

if x > 3:
     print("Hello World")
elif x > 0:
     print("python is awesome")
else:
     print("Have an awesome day")

y = 2

if y > 3:
     print("Hello World")
elif y > 0:
     print("python is awesome")
else:
     print("Have an awesome day")

#Loops
# a) For loops

for (i) in range (4):
     print(i)
# range(4) -> 0,1,2,3

x = 5

for (i) in range(4):
     print(x)
     x += 1

for (i) in range(4):
     print(x)
     x *= 2

favorite_colors = ["Blue", "Purple", "Green"]
for colors in favorite_colors:
     print(colors)

# from the chemical_symbol variable created above
for element, symbol in chemical_symbols.items():
     print(element, symbol)

# While loop
x = 4

while x < 15:
     print(x)
     x += 2

stop = False

while not stop:
     print("Hello world!")
     answer = input("would you like to stop? Enter Y for Yes, N for No:")
     if answer == "Y":
          stop = True

# Functions
def count_vowels(word):
    number_vowels = 0
    for char in word:
        if char in 'aeiou':
            number_vowels += 1
    print(number_vowels)

count_vowels("programming")
count_vowels("coding")
count_vowels("python")


