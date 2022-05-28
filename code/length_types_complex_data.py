fruitList = ['Apple','Banana','Orange','Melon','Grape']
fruitTuple = ('Apple','Banana','Orange','Melon','Grape')
x = range(10)
fruitDict = {
 'type': 'Apple',
 'color': ['Red','Green','Yellow'],
 'sour':False,
 'sweet':True,
 'price':'2.0'}
fruitSet = {'Apple','Banana','Orange','Melon','Grape'}

# print the length of complex data types
print(len(fruitList))
print(len(fruitTuple))
print(len(x))
print(len(fruitDict))
print(len(fruitSet))

# types of complex data types
fruit = ('Apple','Banana','Orange','Melon','Grape')
t = type(fruit)

print(t)
