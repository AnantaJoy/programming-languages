def user_account(f_name,m_name,l_name,contact_no,email,location):
    full_name = f_name+" "+m_name+" "+l_name
    full_name = full_name.title()
    user_info = {'name':full_name,'user_name':f_name+"_"+l_name,'email':email,'contact':contact_no,'location':location,} 
    return user_info


user_info = user_account(f_name='Ananta',m_name='Asim',l_name='Joy',contact_no='017xxxxxxxx',email='anantajoy007@gmail.com',location='Bangladesh')

print(user_info)