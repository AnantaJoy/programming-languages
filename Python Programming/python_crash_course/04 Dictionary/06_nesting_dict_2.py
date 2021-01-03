districts_in_bd  = {
    'dhaka':['Dhaka','Gazipur','Narshingdi'],
    'rajshahi':['Rajshahi','Natore','Bogura',],
    'rangpur':['Rangpur','Dinajpur','Panchagargh'],
    'sylhet':['Sylhet','Moulavibazar','Hobiganj'],
    'barishal':['Barishal','Jhalakhathi','Bhola'],
}

for key, values in districts_in_bd.items():
    print('Districts in',key.title(),'division:')
    for value in values:
        print(value)


accounts_info = {
    'user_1': {
        'f_name':'donald',
        'l_name':'trump',
        'location':'america',
        'title':'Presidet'
    },
    'user_2': {
        'f_name':'vladimir',
        'l_name':'putin',
        'location':'russia',
        'title':'Presidet'
    }
}

for key, values in accounts_info.items():
    print('Username:', values['f_name']+'.'+values['l_name'])
    name = values['f_name'] + " " + values['l_name']
    print("\t Title: Mr.",values['title'])
    print("\t Full Name:",values['f_name'].title(),values['l_name'].title())
    print("\t From:",values['location'].title())
