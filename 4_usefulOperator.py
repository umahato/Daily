'''

index_count = 0
word = 'abcde'
for letter in word:
    print(word[index_count])
    index_count += 1



word = 'abcde'
for item in enumerate(word):
    print(item)



mylist1  = [1,2,3,4,5]
mylist2 = ['a','b','c','d','e']

for item in zip(mylist1,mylist2):
    print(item)

from random import shuffle
mylist = [1,5,2,22,55,59,47]
shuffle(mylist)
print(mylist)




from random import randint
print(randint(0,100))


result = input('What is your name : ')
print(f'Welcome : {result}')

'''

result = input('Favorite Number :')
print(int(result))
print(type(result))
