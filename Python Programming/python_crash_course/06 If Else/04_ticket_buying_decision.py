# Rajshahi to Dhaka Journey Plan

pocket_money = int(input('How much money, do you have?'))

if pocket_money>=3000:
    print('Buy a airlines ticket')
elif pocket_money<3000 and pocket_money>=1000:
    print('Buy train cabin ticket or AC bus ticket')
elif pocket_money>=700  and pocket_money<1000:
    print('Buy train Snighdha ticket or Normal AC')
elif pocket_money>= 400 and pocket_money<700:
    print('Buy Normal bus ticket or train normal class')
elif pocket_money<400 and pocket_money>100:
    print('Local Bus or make onther system')
else:
    print('Borrow money from your friends or call daddy')
