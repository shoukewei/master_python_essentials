fruitDic = {
 'type': 'Apple',
 'color': ['Red','Green','Yellow'],
 'sour':False,
 'sweet':True,
 'price':'2.0'}
fruitDic['origin'] = 'USA'
print(fruitDic)

# update method to add new items 
fruitDic.update({"In stock": 'Yes'})
print(fruitDic)
