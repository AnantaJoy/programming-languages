def user_profile(fname,lname,**user_info):
    profile = {}
    profile['first_name'] = fname.title()
    profile['last_name'] = lname.title()
    for key, value in user_info.items():
        profile[key] = value.title()
    return profile

user = user_profile('donald','putin',location='america',field='politics')
print(user)