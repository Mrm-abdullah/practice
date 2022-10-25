#from math import *

#Triangle
"""
base = float(input('enter your base ='))
height = float(input('enter your height ='))
triangle_area = 0.5 * base * height

print(triangle_area)
"""
#circle 
"""
radious = float(input('Enter your Radius ='))

circle_area = 3.1416 * radious * radious
print(circle_area3) """

#format
"""
a = 5
b = 7
print(f"{a} + {b} = {a+b} ") """

#triangle

""" base = int(input('Enter your base: '))
height = int(input('Enter your Height: '))

triangle_area = 0.5 * base * height
print(triangle_area) """

#Ractangle

""" width = int(input('Enter your Width: '))
height = int(input('Enter your Height: '))

ractangle_area = width * height
print(ractangle_area) """

# Trapezium 

""" a = int(input('Enter your 1st bahu: '))
b = int(input('Enter your 2nd bahu: '))
height = int(input('Enter your height: '))

trapezium = 0.5 * (a+b) * height
print(trapezium) """

#Ellipse

""" a = int(input('Enter your 1st bahu: '))
b = int(input('Enter your 2nd bahu: '))

elipse = 3.1416*a*b
print(elipse) """

#some Function
""" print(max(10,20))
print(min(30,50))
print(abs(-4))
print(abs(4))
print(round(3.2))
print(round(3.7))
print(floor(4.7))
print(pow(2,3))
print(sqrt(25))
print(ceil(4.7)) """


# ternary operator

""" num1 = 32
num2 =65

max = num1 if num1>num2 else num2
print(max)

min = num1 if num1<num2 else num2
print(min) """

#Logical operator
""" 
num1 = 35
num2 = 245
num3 = 348

if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num1 and num2 > num3:
    print(num2)
else:
    print(num3) """


#vpwel a, e, i, o ,u

""" ch = input('Enter your Letter: ')

if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' :
    print("Vowel")
else:
    print('consonant') """

#Letter grade

""" marks = int(input('Enter your markrs: '))

if 100 >= marks >= 80:
    print('A+')
elif 79 >=marks >= 70:
    print('A-')
elif 69 >= marks >= 60:
    print('A')
elif 59 >= marks >= 50:
    print('B')
elif 49 >= marks >= 40:
    print('C')
elif 39 >= marks >= 33:
    print('D')
else:
    print('Fail') """

#group

""" user = input('Enter your text: ')
output = ''
sdj = user.split(' ')
for i in sdj:
    if len(i)==0:
        pass
    else:
        output += i + '**'
output = output[0:-2]
print(output)
 """
# list
"""
list  = [ 3265, 2, 2, 2, 56545, 54564,]
print(list)
print(list[2])
print(list[2:])
print(list[2:5])
print(list[-1])
print(list[:3])
print('hello' in list)
print('hellhho' not in list)
print(list + [13,455])
print(len(list))
list.append('100')
list.insert(2, 500)
list.sort()
list.reverse()
list.pop()
#list.clear()
list2 = list.copy()
print(list2)
print(list.index(2))
print(list.count(2))"""



#for loop

""" list = [10, 20, 30, 40, 50]

for x in list:
    print(x) """

# seris
# 1+2+3+....+n

""" n= 5
sum = 0
for x in range(1, n+1, 1):
    sum = sum + x
print(sum) """

# Random number
#from random import randint

""" 
for x in range(50):
    guessNumber = int(input('Enter your no- 1 to 5 : '))
    randomNumber = randint(1, 5)

    if guessNumber == randomNumber:
        print('You are Won')
    else:
        print('You are lose')
        print('Random number is: ',randomNumber) """




""" user_input = 'how are    you 10 20 30'
text = user_input.split()
output = ''
for x in text:
    output += x + '**'
output = output[0:-2]
print(output)
 """


#list input from user
 
""" user_input = 'how are    you 10 20 30'
text = user_input.split()
output = ''
for x in text:
    output += x + '**'
output = output[0:-2]
print(output) """

""" user = 'How are you 1203'

letter = 0
word =0 
number = 0
for x in user:
    x = x.lower()
    if 'a' <= x <= 'z':
        letter += 1
    elif '0' <= x <= '9':
        number += 1
    elif x == ' ':
        word += 1
print(letter)
print(number)
print(word+1) """


#Matrix

""" matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

#matrix[0][2] = 10
#print(matrix[0][2])

for row in matrix:
    for col in row:
        print(col) """

# dictionary

""" student = {
    101 : 'ami',
    '102' : 'tumi',
    '103' : 'tara'
}

print(student[101])
#print(student[105])
print(student.get(105))
print(student.get(105, 'Not a valid key')) """


#truple

""" student = (
    'ami',
    ('tumi', 'amra', 'amader'),
    'tara'

)

print(student)
print(student[2])
print(student[1]) """

# set

""" num = { 1, 2, 3, 4, 5, 5}
num2 = set([4, 5, 6, 5])

num2.add(8)
num2.remove(8)
print(num)
print(num2)
print(6 in num2)
print(6 not in num2)

print(num | num2)
print(num & num2) """

#stak (FIFO)

""" books = []

books.append('bngla')
books.append('ongkko')
books.append('enlish')

print(books)

books.pop()
print(books[-1])
books.pop()
print(books[-1])
books.pop()
if not books:
    print('No books') """


#queue (LIFO)

""" from collections import deque

bank = deque(['ami', 'tumi', 'tara'])

bank.popleft()
print(bank) """

# function

""" def add(x,y,z):
    sum = x + y + z
    print(sum)

add(10, 20, 30)

def message():
    print('No Pera')
message() """

""" def oooo(str1):
    bbbb = ''
    index = len(str1)
    while index>0:
        bbbb += str1[index-1]
        index = index -1
    return bbbb

print(oooo('fghdfjdjnsydyj123')) """
""" 
def str_reverse(str1):
    re = ''
    index = -1
    for x in range(len(num)):
        re += num[index]
        index = index - 1
    return re
print(str_reverse('asdfgh')) """


print(222)