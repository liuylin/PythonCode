'''
a=10
print(id(a))
print(type(a)

a = 5.6 / 2
b = 5.6 // 2
c = 5 % 2
print(a,b,c)


#x = input()
print(x)

first=123
second=3.14
third=3+4j
print(type(first))
print(type(second))
print(type(third))
'''

'''
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,4 * np.pi,0.01)
y = np.sin(x)
plt.plot(x,y)
plt.show()


a=input("please input something!\n")
if a == '+':
    print('++++++++')
elif a == '-':
    print('-------')
else:
    print(a)


a = input('please input your age:')
w = input('please input your weight:')
if a >= '18' and w >= '60':
    print('yes\n')
elif a <= '18' or w <='50':
    print('fight\n')
else:
    print('no\n
a = input("please input something:")
try:
    a = int(a)
    if isinstance(a,str) == False:
        print('num')
except:
    print('str')
    '''
'''
arr = [1,8,2,5,4,3,7,6,5,8,9,7,20,3,4,55]
for i in range(len(arr)):
    for j in range(i+1):
        if arr[i] < arr[j]:
            #实现两个变量的互换
            arr[i],arr[j] = arr[j],arr[i]
print(arr)

'''
'''
num=[]

for i in range(2,50):
    for j in range(2,i):
        if (i % j == 0):
            break
        num.append(i)
print(num)
'''

'''
num=[]

for i in range(2,100):
   for j in range(2,i):
      if i%j != 0:
        num.append(i)
print(num)
'''

'''
for i in range(10):
    if i == 5:
        print(i*10)
        continue
    if i == 7:
        break
    if i == 2:
        pass
    print(i)
'''

'''
nums = []
for i in range(1,101):
    if i % 3 == 0 or i %5 == 0:
        nums.append(i)
print(nums)
print(sum(nums))
'''

'''
while True:
    try:
        x = int(input("first:"))
        o = input('operator:')
        y = int(input('second:'))
    except:
        break

    ope = {
            '+':x+y,
            '-':x-y,
            '*':x*y,
            '/':x/y
        }
    result = ope.get(o,'please input +|-|*|/')
    print(result)
 '''

'''
import os

i = 0
while True:
    if os.path.isfile('lock.log'):
        print('locked')
        break
    username = input('login:')
    password = input("password:")

    if username == 'lyl' and password == '123':
        welcome = "welcome!"
        print(welcome)
    else:
        i += 1
        if i == 3:
            open('lock.log','w').write(username)
            print('locked by %s'%username)
            break
        continue
        '''
'''
import random

def guessNum():
    x = random.randint(1, 100)
    while True:
        y = int(input("please guess:"))
        if y == 0:
            break
        if x > y:
            print("猜小啦……")
        elif x < y:
            print("猜大啦……")
        else:
            print("you are right")
            break

guessNum()
'''

'''
def Abs(num):
    if num < 0:
        return abs(num)
    else:
        return num

ret = Abs(8)
print(ret)
'''

'''
from functools import  reduce

def myadd(x,y):
    return x+y

sum = reduce(myadd,[1,2,3])
print(sum)
'''

'''
import time

def deco(func):
    def wrapper():
        startT = time.time()
        func()
        endT = time.time()
        msecs = (endT - startT)*1000
        print("it's %s ms" % msecs)
    return wrapper

@deco
def myfunc():
    print('myfunc start...')
    time.sleep(1.7)
    print('myfunc end...')


print('myfunc is ',myfunc.__name__)
#myfunc = deco(myfunc)
print('#'*20)
print('myfunc is ',myfunc.__name__)
myfunc()
'''

def hello_conf(prefix):
    def hello(name):
        print(prefix,name)
    return hello

a = hello_conf('Good morning!')
a('lyl')
a('zyh')

b = hello_conf('where are you going?')
b('honey')
b('dear')




