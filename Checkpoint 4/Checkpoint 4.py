#Exercise 1

#List

a_list = ['python', 'programming', 'course']

#Tuple

a_tuple = (1, 2, 3,)

#Float

a_float = 3.14

#Integer

a_integer = 18

#Decimal

from decimal import Decimal
a_decimal = Decimal("10.99")

#Dictionary

a_dictionary = {
    'age' : 25,
    'name' : 'Jordan',
    'job' : 'Teacher'
}

print(a_list)
print(a_tuple)
print(a_float)
print(a_integer)
print (a_decimal)
print(a_dictionary)
    
#Exercise 2

import math

round_up = math.ceil(a_float)

print(round_up)


#Exercise 3

square_root = math.sqrt(a_float)
print(square_root)

#Exercise 4

first_element = a_dictionary ['age']
print(first_element)

#Exercise 5

second_element = a_tuple [1]

print(second_element)

#Exercise 6

a_list.append('coding')

print(a_list)

#Exercise 7

a_list[0] = 'create'

print(a_list)

#Exercise 8

a_list.sort()

print(a_list)

#Exercise 9

a_tuple += (4,)

print(a_tuple)

