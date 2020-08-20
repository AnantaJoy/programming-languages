food_rating = {}

# add key-values to the list
food_rating['Kacci Biriyani'] = '8.5/10'
food_rating['Beauty Lacci'] = '9/10'
food_rating['Borhani'] = '8/10'

print('Before:')
print(food_rating)


# delete a key-value from the list

print('After:')
del food_rating['Borhani']
print(food_rating)