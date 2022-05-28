# join sets 
fruitSet1 = {'Apple','Banana','Melon'}
fruitSet2 = {'Orange','Melon','Grape'}

fruitSet1.update(fruitSet2)
print(fruitSet1)

# merge a list into the current set
fruitSet = {'Apple','Banana','Melon'}

fruitList = ['Orange','Melon','Grape']

fruitSet.update(fruitList)
print(fruitSet)
