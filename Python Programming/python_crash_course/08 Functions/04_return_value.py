# user first, middle,last name

def user_name(f_name,m_name,l_name):
    full_name = f_name.title()+' '+l_name.title()
    return 'Hello'+' '+full_name

first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')

# here we're not defining middle name(optional vale)
# but the postion of argument is very important
print(user_name(f_name=first_name,l_name=last_name))