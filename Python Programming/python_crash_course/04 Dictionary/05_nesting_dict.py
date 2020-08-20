###################
## Dictionary in List
#########################
haji_biriyani = {'biriyani':'Kacci Biriyani','polao':'Morog Polao','desert':'Faluda','rating': '8/10'}
kolkata_kacci = {'biriyani':'Kacci Biriyani','biriyani':'Hyderabadi Biriyani','desert':'Borhani','rating':'9/10'}
star_kabab = {'biriyani':'Deshi Biriyani','fast_food':'Burger','desert':'Pudding','rating':'8/10'}

hotel_foods = [haji_biriyani,kolkata_kacci,star_kabab]
# index[0]
print(hotel_foods[0])

print('After Looping:')
for food in hotel_foods:
    print(food)

print('\n')


#################
## List in Dictionary
###########################
user_info = []

for user in range(20):
    new_info = {'name':'Ananta','email':'anantajoy007@gmail.com'}
    user_info.append(new_info)

for user in user_info[:5]:
    print(user,'\n')


# change some info in the user_info dictionaries

for user in user_info[3:5]:
    if user['name'] == 'Ananta':
        user['name'] = 'Alien'
        user['email'] = 'alien.xyz@outlook.com'

# let's print out the changes
for alien in user_info[3:5]:
    print(alien)    

###############
## Dictionary in Dictionary
## List in a Dictionary