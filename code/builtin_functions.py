# abs()
a = -5
print(abs(a))

# max() and min()
b = [-3, -5, 0, 2, 10]
print('Maximun: ', max(b))
print('Minimun: ', min(b))

# round()
x = 5.456
y = 5.543
z = -5.454
e = - 5.542
print(round(x))
print(round(y))
print(round(z))
print(round(e))

print('------')

# zip()
fruits = ['apple', 'banana', 'cherry','organge']
prices = [2.59, 0.66, 3.29, 4.45]

fruit_prices = zip(fruits,prices)

for price in fruit_prices:
    print(price)

# create a dictionary using zip()

fruit_dict = {fruits: price for fruits,
              price in zip(fruits,prices)}
print(fruit_dict)



