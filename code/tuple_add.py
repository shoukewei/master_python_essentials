# append an item
fruitTuple = ('Apple','Banana','Orange','Melon','Grape')

fruitList = list(fruitTuple)
fruitList.append('Cherry')
print(fruitList)

fruitTuple_new = tuple(fruitList)
print(fruitTuple_new)

# insert an item
fruitTuple = ('Apple','Banana','Orange','Melon','Grape')

fruitList = list(fruitTuple)
fruitList.insert(2,'Watermelon')
print(fruitList)

fruitTuple2= tuple(fruitList)
print(fruitTuple2)
