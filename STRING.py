"""
#PRINT STATEMENT

print('hello world')

#CONCATINATING A STRING

greetings = ('Hello')
name=('muthu')

message = '{} , {} .Welcome!'.format(greetings,name)

print(message)


#COUNT METHOD

message = ('Hello Bro Revieve')
print(message.count('e'))

#FIND METHOD

message = ('Hello Bro Revieve')
print(message.find('Bro'))


#INDEX

message = ('hello bro revieve')
print(message[7])


#LENGTH OF VARIABLE

message = ('hello bro revieve')
print(len(message))

#LOWERCASE

message = ('Hello Bro Revieve')
print(message.lower())


#REPLACE METHOD

message = ('hello bro revieve')
print(message[0:7])

#REPLACE METHOD

message = ('Hello Bro Revieve')

new_message = message.replace('Revieve','im under the water')

print(new_message)


#UPPERCASE

message = ('Hello Bro Revieve')
print(message.upper())

#VARIABLE WITH PRINT STATEMENT

message = ('hello bro revieve')
print(message)

#LIST WITH INDEX

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#index     0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#negative
#index   -10,-9,-8,-7,-6,-5,-4,-3,-2,-1

# list[start:end:step]

print( my_list[5])


#SLICING WITH RANGE

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#index     0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#negative
#index   -10,-9,-8,-7,-6,-5,-4,-3,-2,-1

# list[start:end:step]

print( my_list[2:7])


#SLICING WITH STEP OPERATOR

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#index     0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#negative
#index   -10,-9,-8,-7,-6,-5,-4,-3,-2,-1

# list[start:end:step]

print( my_list[0::2])


#STRING  FORMATTING WITH RANGE

for i in range(1,11):
    value='The value is {}'.format(i)
    print(value)

#STRING FORMATTING USING CLASS

class person():

    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = person('Jack','33')

sentence = 'My name is {0.name} and I am {0.age} years old.'.format(p1)
print(sentence)


#STRING FORMATTING WITH DICTIONARY

person = {'name':'jack','age':20}


greetings ='My name is {name} and I am {age} years old.'.format(**person)
print(greetings)

#STRING FORMATTING WITH INDEX

person = {'name':'sajeev','age':20}

sentence ='my name is {0} and I am {1} years old.'.format(person['name'],person['age'])
print(sentence)

"""
