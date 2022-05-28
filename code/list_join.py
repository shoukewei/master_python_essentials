# Join two or more lists

fruitList = ['Apple','Banana','Orange','Melon','Grape']
tropFruits = ["mango", "pineapple", "papaya"]

fruitList_new = fruitList + tropFruits

print(fruitList_new)

# extend the list

fruitList.extend(tropFruits)
print(fruitList)


# append a tuple to a list
fruitList2 = ['Apple','Banana','Orange','Melon','Grape']
fruitTuple = ("mango", "pineapple", "papaya")

fruitList2.extend(fruitTuple)
print(fruitList2)
