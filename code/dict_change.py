fruitDic = {
 'type': 'Apple',
 'color': ['Red','Green','Yellow'],
 'sour':False,
 'sweet':True,
 'price':'2.0'}

fruitDic['price'] = 3.0
print(fruitDic)

# update method
fruitDic.update({"price": 4.0})
print(fruitDic)
