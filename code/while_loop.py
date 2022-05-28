# while loop

num = 5

while num > 0: #true
    num-=1 # num = num - 1
    print(num)

else:
    print('The number is no more greater than 0')


# guess the number

word = ' '
while word != 'big':
    word = input('Please input a word with the first letter of b: ')
    if word == 'big':
        print('Great! You got it.')
    else:
        print('Sorry. It is not correct. Please guess it again.')


# break
n = 1

while n < 7:
    n +=1
    print(n)

    if n == 4:
        break

print('....')
# continue
n = 1

while n < 7:
    n +=1

    if n == 4:
       continue
    print(n)
