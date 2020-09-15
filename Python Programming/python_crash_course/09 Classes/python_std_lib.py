# import python default module
from collections import OrderedDict
from random import randint

fav_lang = OrderedDict()

fav_lang['jen'] = 'ruby'
fav_lang['joy'] = 'python'
fav_lang['elly'] = 'c++'
fav_lang['jelly'] = 'java'

# loop through a dictionary
for name,value in fav_lang.items():
    print(name.title()+"'s favorite language is "+value.title()+".")

# generate a random number between (1-6)
random_num = randint(1,6)
print(random_num)