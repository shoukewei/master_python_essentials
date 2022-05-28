# Python program to illustrate
# enumerate function in loops
fruit_list = ['apple', 'banana', 'cherry','orange']
  
# printing the tuples in object directly
for fruit in enumerate(fruit_list):
    print(fruit)

# changing index and printing separately
for n,fruit in enumerate(fruit_list,20):
    print(n,fruit)

#
for n,fruit in enumerate(fruit_list,20):
    print(n)
    print(fruit)


