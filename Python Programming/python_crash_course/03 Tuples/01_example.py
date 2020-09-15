# tuples are immutable
# you can't change it

user_age = (21,22,20,21,22,23)

print((user_age))

#user_age[0] = 22
print(user_age[0])

#print(user_age.append(2))

for age in user_age:
    print(age)

# overwriting a variable is valid
user_age = (40,433,41,42,45,4,32,44)

print(user_age)

print(type(user_age))