n = 298

if n%2 == 0: # ture
    print('This is an even number.')
else: 
    print('This is an odd number.')

# if...elif...else

saleFruit = ['Apple','Orange','Melon','Grape']
stockFruit = ['Apple','Banana','Orange','Melon','Grape']

# check if banana is on sale or in storehouse
if 'Banana' in saleFruit:
  print('Banana is selling.')
elif 'Banana' in stockFruit:
  print('Banana is in the storehouse')
else:
  print('Banana is out of stock!')
