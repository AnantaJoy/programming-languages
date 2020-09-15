temp_list = ['Aaron','Pinkman','Walter','Marie']

permanent_list= ['Skyler','Hank']

while temp_list:
    temp_user = temp_list.pop()
    permanent_list.append(temp_user)
   
print('----------Breaking Bad Cast----------')
print(permanent_list)