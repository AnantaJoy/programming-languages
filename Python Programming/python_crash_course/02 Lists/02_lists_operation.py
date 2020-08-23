# add a element

motorcycles_brand = ['Suzuki','Honda','Yahamaha','Ducati']

print(motorcycles_brand)

motorcycles_brand.append('Kawasaki')  # append added element to the last of list
motorcycles_brand.append(['BMW','Bajaj'])
print(motorcycles_brand[-1])

# insert a element into a list
motorcycles_brand.insert(0,'Royal Enfield')
print(motorcycles_brand)

# removing a element
del motorcycles_brand[-1]
print(motorcycles_brand)

motorcycles_brand.pop()
print(motorcycles_brand)

motorcycles_brand.pop(1)
print(motorcycles_brand)

motorcycles_brand.remove('Royal Enfield')
print(motorcycles_brand)

motorcycles_brand.clear()
print(motorcycles_brand)