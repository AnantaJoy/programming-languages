user_info = {
    'f_name':'Ananta',
    'l_name':'Asim',
    'user_email':'anantajoy007@gmail.com',
    'user_contact': '017xxxxxxxxxx',
    'user_name':'ananta.xoy'
}

for key, value in user_info.items():
    print('Key:',key)
    print('Value:',value,'\n')

print('Key:')
for key in user_info.keys():
    print(key)

print("\nValue:")
for value in user_info.values():
    
    
    
    # it's doesn't make any sense wheather you put space or not 
    print(value)

# sorted

print('\nAfter sorting:')

for key in sorted(user_info.keys()):
    print(key)

# set