#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
classmates = ('Michael', [1, 2], 'Tracy')
classmates[1].append(1)
print classmates
'''

'''
sum = 0
for i in range(101):
    sum += i;
print sum
'''

'''
dic = {'aa':'aa', 'bb':22}
print dic['aa']
'''
'''
list1 = [1, 2, 3, 1]
list2 = [2, 3, 4, 3]
print list1, list2
set1 = set(list1)
set2 = set(list2)
print set1, set2
print set1 & set2
print set1 | set2
a = 1
b = a
a = 2
print b
'''
'''
def my_abs(x):
    if x >= 0:
        return x
    #return

print my_abs(-1)
'''
'''
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError("bad operand type")
    if x < 0:
        return -x;
    return x

print my_abs(int(raw_input()))
'''

'''整数、字符串等都是不可变得，改变它是会重新复制一份，而list等可以改变
def add_end(L = None):
    if L is None:
        L = []
    L.append('end')
    print id(L)
    return L
A = add_end()
print id(A)
A.append('end')
print id(A)

a = 1
b = a
b = 2
print id(a), id(b)
'''
'''
def calc(*numbers):
    sum = 0
    for a in numbers:
        sum += a
    return sum

print calc(1,2,3)
A = [1,2,3]
print calc(A[0],A[1], A[2])
print calc(*A)
'''
'''
import math
def move(x, y, step, angle = 0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny
print move(0, 0, 10, 0)
'''

'''
def person(name, age, **kw):
    print 'name:', name
    print 'age:', age
    print 'city:', kw['city']
    print 'addr:', kw['addr']
    print 'weight:', kw['weight']
person('ycc', 25, city = 'BeiJing', addr = 'NinBo', weight = 110)
print '\n'
kw = {'city':'BeiJing', 'addr':'NinBo', 'weight':110}
person('ycc', 25, **kw)
'''
'''
d = {'a':1, 'b':2, 'c':3}
for key in d:
    print key
for value in d.itervalues():
    print value
for keyValue in d.iteritems():
    print keyValue
'''

'''
from collections import Iterable
print isinstance('abc', Iterable)
print isinstance([1,2,3], Iterable)
print isinstance(123, Iterable)
'''

'''
print [x * x for x in range(1, 11)]
print [x * x for x in range(1, 11) if x % 2 == 0]

print [m + n for m in 'ABC' for n in 'XYZ']
'''
'''
d = {'a':1, 'b':2, 'c':3}
for k, v in d.iteritems():
    print k ,':', v
'''
'''
x = 1
y = 'abc'
print isinstance(x, int), isinstance(y, str )
'''

'''
d = ['ABc', 111, 'jCNF']
print [s.lower() for s in d if isinstance(s, str)]
'''
'''
g = (x * x for x in range(10))
for x in g:
    print x
def fab(num):
    n, a, b = 0, 0, 1
    while n < num:
        yield b
        n = n + 1
        a, b = b, a + b
f = fab(6)
for x in f:
    print x
'''
'''
def odd():
    print 'step 1'
    yield 1
    print 'step 2'
    yield 3
    print 'step 3'
    yield 5

o = odd()
print o.next()
print o.next()
print o.next()
print o.next()
'''
'''
def add(x, y, f):
    print f(x) + f(y)
add(10, -2, abs)
'''
'''
def char2num(c):
    return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[c]
def fn(x, y):
    return x*10 + y
num = reduce(fn, map(char2num, '12345'))
print isinstance(num, int)
'''
'''
def nor(s):
    def upper(name):
        return name.title()
    return map(upper, s)
print nor(['njnj', 'jfvj'])

def prod(s):
    def chen(x, y):
        return x * y
    return reduce(chen, s)
print prod([1, 2, 3, 4])
'''
'''
def is_odd(a):
    return a % 2 == 1
print filter(is_odd, [1,2,3,4,5,6])
def not_empty(s):
    return s and s.strip()
print filter(not_empty, ['','a ','fv',''])
'''
'''
print sorted([2,6,4,3,8,0])

def cmp_reversed(x, y):
    if x > y:
        return -1
    elif x < y:
        return 1
    return 0
print sorted([2,6,4,3,8,0], cmp_reversed)

def cmp_ignore_case(c1, c2):
    c1 = c1.upper()
    c2 = c2.upper()
    if c1 > c2:
        return 1
    elif c1 < c2:
        return -1
    return 0
print sorted(['bob', 'about', 'Zoo', 'Credit'],cmp_ignore_case)
'''
'''
def lazy_sum(*arg):
    def sum():
        ax = 0
        for i in arg:
            ax += i
        return ax
    return sum
f = lazy_sum(*[1,2,3,4])
print f()

def count():            #这样结果全部是9，因为最终i的值为3
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs
f1, f2, f3 = count()
print f1(), f2(), f3()

def count():
    fs = []
    for i in range(1, 4):
        def g(j):
            def f():
                return j * j
            return f
        fs.append(g(i))
    return fs
f1, f2, f3 = count()
print f1(), f2(), f3()
'''
'''
print map(lambda x: x*x, [1, 2, 3, 4, 5, 6, 7, 8, 9])
'''
'''
def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper
@log
def now():
    print '2017-03-13'
now()
'''
'''
def log(func, text):
    def wrapper(*args, **kw):
        print '%s %s():' % (text, func.__name__)
        return func(*args, **kw)
    return wrapper
def now():
    print '2017-03-13'

now = log(now, 'call')
now()
print now.__name__   #wrapper
'''
'''
import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper

@log
def now():
    print '2017-03-13'

now()
print now.__name__
'''
'''
def log(func):
    def wrapper(*args, **kw):
        print 'call begin:'
        res = func(*args, **kw)
        print 'call end'
        return res
    return wrapper
@log
def now():
    print '2017-03-13'
now()
'''
'''
def log(*text):
    def decorator(func):
        def wrapper(*args, **kw):
            if len(text) == 1:
                print '%s %s():' % (text[0], func.__name__)
            else:
                print 'no text %s()' % func.__name__
            return func(*args, **kw)
        return wrapper
    return decorator

@log('fhvb')
def now():
    print '2017-03-13'

now()
'''
'''
print int('12345', base = 8)

import functools
int2 = functools.partial(int, base = 2)
print int2('10')
print int2('10', base = 10)
'''
'''
import Module1
print Module1.__doc__
print Module1.__author__
print Module1.__sex
Module1._private1()
'''
'''
from PIL import Image
im = Image.open('source.bmp')
print im.format, im.size, im.mode
'''
'''
import sys
print sys.path
'''
'''
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score

s = Student('ycc', 88)
print 'name is:%s, score is:%s' % (s.get_name(), s.get_score())
'''

'''
class Animal(object):
    def __init__(self, name, ageIn):
        self.__name = name
        self.age = ageIn
    def run(self):
        print 'Animal is running'

class Dog(Animal):
    def run(self):
        print 'Dog is running'

def action(ani):
    ani.run()

ani = Animal('ani1', 11)
dog = Dog('dog1', 11)

import types
print type(123) == types.IntType
print type('123') == types.StringType
print type(int) == types.TypeType#类型本身是一种叫type的类型，因为python都是引用，所以可以理解为存放指针的数据类型吧
print type(str) == types.TypeType

action(ani)
action(dog)

print isinstance(dog, Animal), isinstance(dog, Dog)

print hasattr(dog, '__name')    #私有属性不可直接访问
print hasattr(dog, 'age')     #这些访问形式只有在对对象不了解的情况下，一般不这么访问
f = getattr(dog, 'run')
f()
'''
'''
class Student(object):
    pass

def set_age(self, age):
    self.age = age

from types import MethodType
Student.set_age = MethodType(set_age, None, Student) #动态绑定方法


s = Student()
s.name = 'ycc'         #动态绑定属性
s.set_age(25)
print 'name:', s.name, 'age:', s.age
'''

'''
class Student(object):
    __slots__ = ('name', 'age')       #只能绑定

def set_age(self, age):
    self.age = age

from types import MethodType
Student.set_age = MethodType(set_age, None, Student) #动态绑定方法


s = Student()
s.name = 'ycc'         #动态绑定属性
s.set_age(25)
s.score = 99      #由于限制，score属性不能绑定
print 'name:', s.name, 'age:', s.age
'''
'''
class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s._score = 60
#s.score = 999
print s._score
'''
'''
import numpy as np
from numpy.matlib import randn
from numpy.matlib import array
class Network(object):
    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x)
            for x, y in zip(sizes[:-1], sizes[1:])]

net = Network([2, 3, 4])
#print net.biases, np.zeros(net.biases[0].shape)
#print net.weights
print np.zeros(net.weights[0].shape)
'''
'''
w = array([[-1.8042905 ,  0.36018469],
       [-0.69390716, -0.60624698],
       [-1.13982134,  0.54092366]])
a = array([[1], [2]])
print np.dot(w, a)
'''
