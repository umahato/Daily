#   List Comprehensions are unique way of quickly creating a list with Python.
#   If you find yourself usig a a for loop along with .append() to create a list,
#   List Comprehensions are good alternative
#   Adding comment only

'''
mystring = 'hello'
mylist = []

for letter in mystring:
    mylist.append(letter)

print(mylist)


'''

# alternate way.
mystring = 'hello'
mylist = [letter for letter in mystring]
print(mylist)
