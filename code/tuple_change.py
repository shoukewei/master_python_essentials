fruitTuple = ('Apple','Banana','Orange','Melon','Grape')
fruitList = list(fruitTuple)
fruitList[1] = "Cherry"
fruitTuple = tuple(fruitList)

print(fruitTuple)
