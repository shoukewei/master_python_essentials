# add another tuple with one element or more
fruitTuple1 = ('Apple','Banana','Orange','Melon','Grape')
fruitTuple2 = ("mango", "pineapple", "papaya") 
fruitTuple = fruitTuple1 + fruitTuple2
print(fruitTuple)


# extent method does not work for tuple
fruitTuple1 = ('Apple','Banana','Orange','Melon','Grape')
fruitTuple2 = ("mango", "pineapple", "papaya")

fruitTuple1.extend(fruitTuple)
print(fruitTuple1)
