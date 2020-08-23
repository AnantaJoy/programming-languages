## slicing
prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23]

print(prime_numbers[1:5])
print(prime_numbers[2:7])
print(prime_numbers[:2])
print(prime_numbers[4:])
print(prime_numbers[4:-3])
print(prime_numbers[-3:])
print(prime_numbers[:-2])



## looping
country = ['bangladesH','inDIA','nePAL']

for i in country[0:]:
    print(i.title())

## copying

foods =['Burger','Pizza','Pasta','Cake','Biriyani']

fav_foods = foods[:]

print(foods)
print(fav_foods)

fav_foods = foods[2:4]
print(fav_foods)

foods.append('Thai Soup')
fav_foods.append('Morog Polao')
print(foods)
print(fav_foods)

fav_foods = foods
################
# Don't assign list in this way
# Cz they indicate the same list
# So when you change in one list
# Changes apply to both lists
