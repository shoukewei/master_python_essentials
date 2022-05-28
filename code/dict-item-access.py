fruitDic = {
 'type': 'Apple',
 'color': ['Red','Green','Yellow'],
 'sour':False,
 'sweet':True,
 'price':'2.0'}

# use key to get its value
print(fruitDic['price'])

# use get() method to get a value
x = fruitDic.get('price')

print(x)

# get just the keys
keys = fruitDic.keys()

print(keys)

# get the values

values = fruitDic.values()
print(values)
