# count from 1 to 10

for value in range(1,11):
    print(value)

# create a list using list

odd_numbers_list = list(range(1,10,2))

print(odd_numbers_list)

# list of square numbers in certain range
# using a empty list

squares = []

for i in range(1,11):
    squares.append(i**2)

print(squares)

# sum of numbers in a list

numbers = [75,21,2,32,58,42]
# sum = 0
# for i in range(0,len(numbers)):
#     sum += numbers[i]

# print(sum)
#print(min(numbers))
#print(max(numbers))
#print(sum(numbers))