def sum_array(*numbers):
    sum = 0
    for num in numbers:
        sum +=num
    return sum

x = sum_array(1,3,2,4,5,6,)
print(x)
y = sum_array(1,2,3)
print(y)