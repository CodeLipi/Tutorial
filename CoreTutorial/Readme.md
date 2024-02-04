[Go to HomePage](/README.md)

![python](/PythonExample.png "Core Python")

Application of Python :
------------------------------

- Desktop Application
- Web Application
- Database Application
- Networking Application
- Data Science
- Data Analysis
- A.I.
- Machine Learning
- Iot Application
- Automation
- and many more....


Features of Python :
-------------------------------

- Simple and Easy
- Free and Open source
- High level programming
- Platform independent : Write once and Run anywhere (WORA)
- Portability
- Dynamically typed
- Procedure oriented (functional) and Object oriented
- Interpreted
- Extensible (We can use any language code into python)
- We can improve performance using Extensible feature
- Embedded (Python can be use any other language or embedded)
- Extensive library support


Limitation of Python :
-------------------------------

- Performance wise (Cause : Interpreter)
- Not Supported for Mobile Application

> Myth : Python is not suitable for large scale enterprise application


Flavors of Python :
---------------------------

- *CPython* : It can be used with c language (Standard)
- *Jython* or *JPython* : It can be used with java language
- *Iron Python* : C# & .Net 
- *Pypy* : Upgrade performance of python (inside PVM use JIT)
- *RubyPython* : Ruby language
- *AnacondaPython* : Used for data processing and to handle huge data
- *Stackless* : for multithreading (Python for concurrency)



Identifiers :
--------------------
- Variable, class or method (function) name : What we define

**Rules :**

- a-z,A-Z,0-9,_ (both upper and lower case)
- Should not starts with digit
- Case sensitive
- Keyword is not allowed in identifiers
- No length limit for identifiers : Not recommended for lengthy length for identifiers
- If identifiers starts with _ : private identifiers (_var)
- If identifiers starts with __ : strongly private identifiers (__var)
    - `__var__` : language specific identifiers


Reserved words : `total 35`
----------------------
```py
True, False, None
and, or, not, is, in
if, else, elif
while, for, break, continue, return, yield
try, except, finally, raise, assert
import, from, as
class, def, pass
global, nonlocal, lambda, del, with
async, await
```

**Note:**
- It contains only lower alphabet symbol, except 3 : `True, False, None`

```py
import keyword
print(keyword.kwlist) # Print the all reserved keyword
```

Data Types : `total 14`
----------------------
```
- int, float, complex
- bool
- str 
- bytes, bytearray
- range
- list, tuple, set, frozenset, dict
- None
```

- Everything in python is object
    - Here, size of data type is undecided because object


int :
-------------
1. *Decimal(0-9)* --> a=10, b=2
1. *Binary(0,1)* --> a=0b1111, b=0b1001  (use b or B)
1. *Octal(0-7)* --> a=0o777, b=0o443  (use o or O)
1. *Hexa decimal(0-15):(0-9&A-F)* --> a=0x234af, b=0xbeef  (use a-f or A-F)

- Utility function for base conversions :

    - `bin(x)` : x value in decimal, octal, hexa decimal convert into binary
    - `oct(x)` : x value in decimal, binary, hexa decimal convert into octal
    - `hex(x)` : x value in decimal, octal, binary convert into hexa decimal


float :
--------------
- Floating point doesn't support binary, octal and hexa decimal floating point.
- It supports exponential values.

```py
f = 10  # 10.0
f = 10.2    # 10.2

# f = 0b10.2  # doesn't support binary
# f = 0o10.2  # doesn't support octal
# f = 0x10.2  # doesn't support hexa decimal


# exponential form
f = 1.2e100
f = 1.2e100000
```


complex number : 
--------------------------

    a = real part, b = imaginary part
    then complex no = a+bj

- In imaginary part `j` is important. We can't change with any other letter.
- In real part int, float, binary, octal, haxadecimal all the value are allowed.
- In imaginary part only int and float are allowed.
- If you want that imaginary part is zero then it is important to put `0j` value

**inbuilt attribute :**
```py
a = 10+5j
a.real   # real is attribute(var)
a.imag   # imag is attribute(var)
```


bool :
-----------

- Only 2: `True, False`
- True + True = 2
- True + False = 1

> Cause: True=1, False=0



str :
------------

- one or more than one char is string in python.
- Support multiline string.    
```py
string = '''this is 
multiline string'''
```
- Support single (') and double (") quote in string.
```py
# 'string' --> string
# "string" --> string
# """multiline string""" --> multiline string literal
```

Inbuilt function in string:
------------------------------

- `strip()` : remove spaces form both side
- `lstrip()` : remove spaces form begining of the string
- `rstrip()` : remove spaces form end of the string
- `find(substring)` : finding the string from beginning and return the index of first match and when not find return -1
- `rfind(substring)` : finding the string from reverse(ending) direction and retrun the index of string and when not find return -1
- `find(substring, begin, end)` : we can customize the serch in string.
- `rfind(substring, begin, end)` : we can customize the serch in string.
- `index(substring)` : it works like find and when it not find raise a IndexError.
- `index(substring, begin, end)` : it works like find and when it not find raise a IndexError, while stopping the execution.
- `rindex(substring)` : it works like rfind and when it not find raise a IndexError.
- `rindex(substring, begin, end)` : it works like rfind and when it not find raise a IndexError, while stopping the execution.
- `count(substring)` : counts, how many times the substring is present in main string.
- `count(substring, begin, end)` : counts, how many times the substring is present in given range of the main string.
- `replace(oldstring, newstring)` : replace the old string with new string, it creats a new string object at memory level, previous string is not changed.
- `split(seperator)` : default is space; splits the string according to seperator.
- `rsplit(seperator)` : reverse direction.
- `join()` : joins the string
- `upper()` : to change in uppercase
- `lower()` : to change in lowercase
- `title()` : to change in title case like first letter is capital in each word
- `capitalize()` : to capitalize the first word's first leter in single sentence.
- `swapcase()` : to change uppcase into lower case and lowercase into upper case.
- `startswith(substring)` : to check the substring is starts with substring or not ? returns True or False. 
- `endswith(substring)` : to check the substring is ends with substring or not ? returns True or False. 
- `isalnum()` : to check alphanumeric or not ? a-z, A-Z, 0-9 returns True or False.
- `isalpha()` : to check only alphabet or not ? a-z, A-Z returns True or False.
- `isdigit()` : to check only digit or not ? 0-9 returns True or False.
- `islower()` : to check lowercase or not ? returns True or False.
- `isupper()` : to check uppercase or not ? returns True or False.
- `istitle()` : to check title case or not ? returns True or False.
- `isspace()` : to check contains only space or not ? returns True or False.



Slice Operator :
------------------

- Breaking string into char or sub string.
- +ve --> left to right (start with 0 and goes)
- -ve --> right to left (start with -1 and goes)
- : slice operator
- \* repeat operator
```py
s = 'Uttar Pradesh'
# s[begin : end]
# begin --> inclusive
# end --> exclusive
s[1:4] --> tta

# s[1:] --> index 1 from ending
# s[:7] --> begining from index 7

# s[begin : end : step]

```


Type Casting or Type Coersion :
--------------------------------

```py
int()
float()
complex()
bool()
str()
bin()
oct()
hex()
```

- `int()` : any other type value into `int` type
``` py
int(10) : 10
int('10') : 10
int(2.3 ) : 2
int('2.3') : ValueError
int('str') : ValueError
int(2+3j) : TypeError
int('2+3j') : ValueError
int(0b11) : 3
int('0b11') : ValueError
int(0o11) : 9
int('0o11') : ValueError
int(0x11) : 17
int('0x11') : ValueError

```
- `float()` : any other type into `float` type.
```py
float(10) : 10.0
float('10') : 10.0
float(2.3 ) : 2.3
float('2.3') : 2.3
float('str') : ValueError
float(2+3j) : TypeError
float('2+3j') : ValueError
float(0b11) : 3.0
float('0b11') : ValueError
float(0o11) : 9.0
float('0o11') : ValueError
float(0x11) : 17.0
float('0x11') : ValueError
```
- `complex()` : any other type intp `complex`type.
```py
complex(10) : 10+0j
complex('10') : 10+0j
complex(2.3 ) : 2.3+0j
complex('2.3') : 2.3+0j
complex('str') : ValueError
complex(2+3j) : 2.3+0j
complex('2+3j') : 2.3+0j
complex(0b11) : 3+0j
complex('0b11') : ValueError
complex(0o11) : 9+0j
complex('0o11') : ValueError
complex(0x11) : 17+0j
complex('0x11') : ValueError
```
- `bool()` : any other type into `complex` type.
```py
bool(10) : True 
bool('10') : True 
bool(2.3 ) : True 
bool('2.3') : True 
bool('str') : True 
bool(2+3j) : True 
bool('2+3j') : True 
bool(0b11) : True 
bool('0b11') : True 
bool(0o11) : True 
bool('0o11') : True 
bool(0x11) : True 
bool('0x11') : True
bool(0) : False 
bool(0b0) : False 
bool(0o0) : False 
bool(0x0) : False
bool('0') : True 
bool('0b0') : True 
bool('0o0') : True 
bool('0x0') : True 
bool('') : False 
bool(' ') : True 
```
- `str()` : any other type into `str` type.
```py
str(10) : '10'
str('10') : '10'
str(2.3) : '2.3'
str(2+3j) : '(2+3j)'
str('2+3j') : '2+3j'
str(0b11) : '3'
str('0b11') : '0b11'
str(0o11) : '9'
str(0x11) : '17'
str('0x11') : '0x11'
str('0o11') : '0o11'
```
- `bin()` : any other type into `bin` type, except string and any type inside string, floating value.
```py
bin(10) : 0b1010
bin(0o11) : 0b1001
bin(0x11) : 0b10001
bin(0b11) : 0b11
```
- `oct()` : any other type into `oct` type except string and any type inside string, floating value.
```py
oct(10) : 0o12
oct(0o11) : 0o11
oct(0x11) : 0o21
oct(0b11) : 0o3
```
- `hex()` : any other type into `hex` type except string and any type inside string, floating value.
```py
hex(10) : 0xa
hex(0b11) : 0x3
hex(0o11) : 0x9
hex(0x11) : 0x11
```


Immutable vs Fundamental data type :
-----------------------------------

- If we create var with same name which is before created is not replace but a new variable obj is created.
```py
x=10
print(id(x))  # same obj

y=10
print(id(y))  # same obj

x=111
print(id(x))  # different obj

# pointing to same obj but not replaced, created a new one.
```
- All fundamental data types :`int, float, bool, complex, string` --> immutable
- Only in the following datatype with ranges reusing the same obj is applicable : (only in idle not in python file)
```py
# int --> -5 to 256
# bool --> always
# str --> always
# float, complex --> not applicable.
```
- Python preallocates an array of integer objects from -5 to 256 for memory optimization in idle

bytes and bytesarray
----------------------

- range : must be from 0 to 256
- bytes : immmutable, bytesarray : mutable.


List & Tuple
--------------------

- Growable & Reduceable
- Insertion order is preserved
- Dublicate allowed
- Hetrogeneous data allowed
- List : Mutable, Tuple : Immutable
- List : [], Tuple : ()
- Index : -ve and +ve
- Slice and Repeat Operator (: and *)
- `empty_list = []`
- `empty_tuple = ()`
- `single_data_list = [42]`
- `single_data_tuple = (42,)`
- in tuple paranthesis is optional when creation
- in tuple only reading is allowed not writing or updating
- convert input (string) data into list
```py
- dynamic method : eval(input())
- list method : list(input())
- split method : split(input())
```


Inbuilt function
-------------------

- `append(item)` : for data insert     # but not allowed in tuple
- `remove(item)` : for data remove, won't return anything      # but not allowed in tuple
- `pop()` : remove the last item in list return the removed item    # not allowed in tuple
- `pop(index)` : remove the specified item in list return the removed item    # not allowed in tuple
- `count(item)` : how many time item is present in list       # allowed in tuple
- `index(item)` : search of item present in first occurence       # allowed in tuple
- `insert(index, item)` : insert the item at specified index        # not allowed in tuple
- `extend(any sequence)` : add another list into existing list to extend the list, return None.     # allowed in tuple
- `reverse()` : reverse the order of items in list.       # allowed in tuple
- `sort()` : sort into natural sorting order like 0,1,2,3...;a,b,c,d...;A,B,C,D...   # allowed in tuple
- `sort(reverse=True)` : sort in reverse order like 9,8,7...;z,y,x...        # allowed in tuple
- `copy()` : to clone (copy) the whole list     # allowed in tuple
        `x = [1,2,3,4,5]     y = x[:]   # clone the data`
- `clear()` : remove all the item inside list but not delete the list.
- `min(sequence)` : return the minimum value.      # allowed in list, tuple, string
- `max(sequence)` : return the maximum value.      # allowed in list, tuple, string




Comprehesion
------------------------

- Comprehension works on list, set and dict.  (Do google for this) but not on tuple because its changed to generators
```py
l = []
for x in range(1,11)
    l.append(x*x)
print(l)

# list comprehension
l = [ x*x for x in range(1,11)]
print(l)

# list = [expression for x in sequence]
# list = [expression for x in sequence if condition]
```

Packing and Unpacking
-------------------------------

- packing and unpacking is applied on list, tuple, string and set  (Do google for this)
```py
# packing
a,b,c,d,e = 1,2,3,4,5
t = a,b,c,d,e
print(type(t), t)    # <class 'tuple'> (1, 2, 3, 4, 5)

# unpacking
t = 10,20,30,40,50
a,b,c,d,e = t
print(a)  # <class 'int'> 10
print(b)  # <class 'int'> 20
print(c)  # <class 'int'> 30
print(d)  # <class 'int'> 40
print(e)  # <class 'int'> 50
```


range()
----------------

- Sequence of number
- Immutable
- range(n) : 0 to n-1
- range(x,y) : x to y-1
- range(x,y,z) : x to y-1 at z step


Set & Frozeset
---------------

- Growable and reducable
- Insertion order is not preserved
- Duplicate not allowed
- Hetrogeneoud data allowed
- Both : {}
- Indexing and Slicing is not allowed
- `empty_set = set()`
- `empty_frozenset = frozenset()`
- `single_data_set = {42}`
- `single_data_frozenset = frozenset({42})`


Inbuilt function
--------------------
- `add()` : for data insert    # not allowed in frozenset
- `remove()` : for data remove  # not allowed in frozenset
- `update(any sequence)` : add another set into existing set to update (like extend) the set, return None.     # allowed in frozenset
- `copy()` : clone the set
- `pop()` : remove some random element and return that element
- `remove(elment)` : remove specified element and return None
- `discard(element)` : remove specified element and return None and when element not find raise KeyError
- `clear()` : remove whole element only but not delete the set return empty set.
- `union()` : all the element inside both.
- `intersection()` : only common element
- `difference()` : s1.difference(s2) --> s1 - s2
- `symmetic_difference()` : s1.symmetric_difference --> s1^s2 (element in s1 but not in s2)



Dictionary
-------------------

- By default mutable.
- Key-value pair data
- Key : Not Duplicate, Value : Duplicate allowed
- Growable and reducable
- `empty_dict = dict(), {}`
- `single_data_dict = {'key': 42}`

Inbuilt function :
-------------------------

- get()
- get(key, default value)
- clear()
- pop()
- popitem()
- keys()
- values()
- items()
- update()
- setdefault(key, value)   


None & Pass
-------------

- When a function doesn't return anything then handling this situation `None` is return.
- When a function doesn't do anything then handling this situation `pass` is used.
```py
def fn():
    # doesn't return anything

print(fn())   # None

def fn():
    # doesn't do anything
    pass

print(fn())  # Nothing print (a blank line)
```

Constant 
---------------

`MAX_VALUE = 10` --> This value doesn't changable or treated as constant.


Operator
------------

1. Arithmetic Operator
2. Relational Operator or Comparison Operator
3. Logical Operator
4. Bitwise Operator
5. Assignment Operator
6. Special Operator


Arithmetic Operator
---------------------------

- Addition : + (Used for string concatenation)
- Subraction : -
- Multiplication : *  (Used for string repeation)
- Division : /  --> 10/2 = 5.0, 10//3 = 3.3333
- Modulo : %  --> Reminder
- Floor Division : // 10//2 = 5, 10//3 = 3
- Exponent (power) : **
```
/ --> float
// --> int or float
    if both argument are int --> int
    else --> float

For string case
+ : both argument should be in string
* : any one argument shuld be in int

In case of zero divison
x / 0 : ZeroDivisionError
x % 0 : ZeroDivisionError
x // 0 : ZeroDivisionError
```

Relational or Comparison Operator
--------------------------------

- less than : <
- greater than : >
- less than or equal to : <=
- greater than or equal to : >=
- assignment : =
- In string comparison based on alphabetical order.
- a to z : 97 to 122
- A to Z : 65 to 90


Chaining of Relational Operator
------------------------

- Atleast one operator returns false then whole condition is false.
- If all oprator returns true then whole condition is true.
```
10<20<30<40<50 : True
10<20<30<40<50>60 : False
```


Equality Operator
--------------------

- equal : ==
- not equal : !=
- chaining is possible here.
- It only compare content inside variable.

`content same : True, content different : False`


Logical Operator
------------------------

- and : if every argument returns True then True.
- or : if atleast one argument is True then True.
- not : opposite of operator
- 0 means False
- non-zero means True
- empty string means False
```
x and y
-----------
if x evaluate to false then result is x otherwise result is y
if x evaluate to true then result is y

10 and 20 --> result 20
0 and 20 --> result 0

x or y
----------
if x evaluate to false then result is y.
if x evaluate to true then result is x.

10 or 20 --> result 10
0 or 20 --> result 20
0 or 0 --> result 0 (second)

```

Bitwise Operator
--------------------

- Apply only on int and boolean data
- bitwise and (&) : if both bits are 1 then only 1 otherwise 0
- bitwise or (|) : if atleast one bit is 1 then 1 otherwise 0
- exclusive or / x-or (^) : if both bits are different then 1 otherwise 0
- bitwise not (~) : 1 --> 0 and 0 --> 1
- bitwise left shift (<<) : on right filled with zero
- bitwise right shift (>>) : on left filled with sign bit (0-->+ve,1-->-ve)
```
4&5 : valid
True | False : valid
10.5 % 2.3 : not valid
```

Ternary Operator
------------------

`var = first_value if condition else second_value`<br>
`var = first_value if condition_1 else second_value if condition_2 else third_value`


Special Operator
--------------------

1. Identity Operator
1. Membership Operator : in, not in

Identity Operator
---------------------

- is, is not : for identity(id:memory_address) check.
- In case of same object.


Input
--------------

- input() : takes input and return string always.
- eval() : takes input as string and evaluate on the go.


Command Line Arguments:
---------------------------

- Values which are pass or entered (or another file) on command line/cmd.
- argv : variable which is available in `sys` module.
- argv hold data as list or array.
- while using slice operator: no error
- and when using index : indexerror(in case of max index which is not entered)

```py
import sys  # we entered on cmd 10 20 30
print(sys.argv[7:100])   # []
print(sys.argv[100])     # IndexError : out of range
```


Output
------------------

1. Form-1
    - print() 
    - print('str 1' + 'str 2') 
    - print('str ' * 3) 
    - print(a,b,c) 
    - print(a,b,c,sep=',') 
    - print(a,b,c,sep=':',end=' ') 
2. Form-2
    - print(formated string): 
    - %i = int type 
    - %d = int type 
    - %f = float type 
    - %s = str type 
    - print('formated string :' %(variable list)) 


f-string and .formated method
---------------------------------

- print(f'value is {var | direc value}')
- print('value is {var | direct value| replaced}'.format(var | var | replace var = previous var))


Flow Control
-----------------

1. Selection Statements
- if
- if-else
- if-elif-else
- if-elif

2. Iterative Statements
- for loop : When we no the no of iteration
- while loop : When we don't know the no of iteration.
- Infinite loop : while True
- Nested loop : loop inside loop

3. Transfer Statements
- break : to break the loop iteration and come out of it
- continue : to skip the current loop and continue to next iteraton
- pass : to do nothing after it


del and None:
--------------------

- del : deletes the object and don't delete immutable object's item like string's character
- None : No value.


Functions
---------------------

- Code reusablility of biggest advantage
- `def` keyword for defining function
- It is also called method(class), procedures, sub routine.
- 2 types : Inbuilt/Predefined and user defined functions
- A function can return function and also function takes another function as an arguments
- In nested function, inner function can called by with the help of assigning into a var and called by this variable alias.
- Python provides some inbuilt function :
    - `print()` : printing / output
    - `type()` : tell about data type
    - `id()` : address of object
    - `len()` : length of object
    - `eval()` : to eval input on the go..
    - `sorted()` : for sorting the data
- Types of argumets :
    - Formal arguments : General way
    - Positional arguments
    - Keyword arguments
    - Default arguments
    - Variable length arguments

- argument order is important : positional, keyword, default, variable list 


```py
# definition of function
def function(argument or argrment list):
    body

funtion(parameter or parameter list)  # function call
```

Positional Arguments
----------------------------

```py
def sub(a,b):
    print(a-b)

sub(100,50)  # here order is important because of function expression
sub(50,100)  # here if we change the order, result is change
```

Keyword Arguments
---------------------

``` py
def wish(name,msg):
    print('Hello', name,msg)
    
wish(name='kush',msg='good morning') # these are keyword argument we can change the order here
wish(msg='good morning', name='kush') # these are keyword argument we can change the order here like this
wish('kush', msg='good morning') # here positional and keyword argument are used
wish(msg='good morning', 'kush') # here positional and keyword argument are used, here order is not important too
```

Default Arguments
---------------------------

```py
def wish(name='guest'):
    print('hello', name, "Good Morning")

wish("Kush")
wish()  # this is also possible

# we can use positional, keyword and default argument together.
```

Variable length arguments (*n, **n)
------------------------------

```py
def sum(a,b):
    print(a+b)

def sum(a,b,c):
    print(a,b,c)

def sum(a,b,c,d):
    print(a,b,c,d)

sum(10,20)
sum(10,20,30)
sum(10,20,30,40)

# solve the above problem by this method 

def f1(*n):   # *n works as tuple (*args)
    print('Var-arg function...')

f1()
f1(1)
f1(1,2)
f1(1,2,3)
f1(1,2,3,4)
#f1(1,2,3,4,5....)

# we can pass positional, keyword, default, var-arg
```

Keyword var-length argument
--------------------------------

```py
def display (**n):   # **n works as dict (**kwargs)
    print("record info")
    for key, value in n.items():
        print(key,"\t",value)

display(name = 'kush', marks = 100, age = 23, day = 'sumday')
display(name = 'jenny', marks = 140, age = 53, day = 'mmonday', job = 'cs')
display(name = 'kolfher', marks = 123, day = 'mmonday', job = 'service')

# we can pass positional, keyword, default, var-args
```



Types of Variables in Functional Programming
--------------------------------------------------

1. Gloabal variables
    - Declared outside of function and available to access for all the modules.
    - inside a fn `global` keyword is used for to making global variable.
    - `globals()` returns the dictonary of all global variable 
2. Local variables
    - Declared inside of function and available to access inside the function only
    - It's priority is high.
    - local variable is declare after the global variable
- Priority : local > global


Recursive function
-----------------------

- function is call by itself
- it takes much space for the long calculation and also take too much time.
- reduce the length of the code and improves the readability
- we can solve very complex problems easily like `tower of hanoi` and `factorial program`.

Anonymous funcion
---------------------

- Without name or nameless function
- instant use (only one time usage)
- syntax : `lambda var or input : expression`
```py
add = lambda a,b : a+b
print(add(10,4))
```
- Some function take function as an argument like these where we use lambda function.
    - `filter(function, sequence)` : here, sequence applied on function and returns sequence (filter obj) </br>
        - filter function filter value when the function return True, So filter works on True and False (boolean value) </br>
    - `map(function, sequence)` : here, sequence applied on function and returns sequence (map obj)
        - map function takes value and the function return calculated value
    - `reduce(function, sequence)` : reduce the sequence into in a single value (this is the part of `functools` module)


Function Aliasing
------------------------

- If delete origin then original is not accessed but alias is accessable.

```py
def wish(name):
    print('Good Morning', name)

wish('jenny')  #  function call
greet= wish('kush')  # function aliasing


print(id(wish))
print(id(greet))
```


Nested Function
---------------------

- Function inside function is called nested functions
- We can't call nested function with the help the outer most function.


Function Decorators
-------------------------

- Simple Lady(Input function) --> BeautiParlour (Function Decorator) --> Output function (Heroine) : with some extra capability 
- Decorators help to make out code shorter and more pythonic(readable)
- If we want a new feature in existing function, we apply decorator for this


Decorator Chaining
---------------------------

```py
@decorator1
@decorator2
@decorator3
.
.
.
.
#  function declaration
```

List vs Tuple with large amount of data
------------------------------------------

```py
list = [x*x for x in range(10000000000000000000000000000000)]  # this gives MemoryError
tuple = (x*x for x in range(10000000000000000000000000000000))  # this doesn't raise any error
# this is also called Generators Concept

# because list store every data in memory but tuple produce on the go in each line and does'nt store the data
```

Generators 
--------------

- Very easy to use
- This improves the performance of the program
- Memory utilization improved
- Used in web scraping and crawling
- Best suitable for reading data from large number of files
- We can write generator just like normal function but when return value we use `yield` keyword for return.

```py
def my_gen():
    yield 'A'
    yield 'B'
    yield 'C'
    yield 'D'
    # there order is important

g = my_gen()
print(type(g))

print(next(g))   # A
print(next(g))   # B
print(next(g))   # C
print(next(g))   # D
```


Modules, Packages and Library
-----------------------------

- contains a group of variable and functions in a different file is called module
- contains a group of modules in a folder is called packages
- contains a group of packages in a folder is called library

Modules
----------------------

- Code reusability
- Maintainability
- Improve readability
- In whole program module is imported once and when we updated something in module, the new version is not imported in program by default, with the help of reload() method we can import updated version of module.


Special Variable `__name__` :
----------------------------

```py
def f1():
    if __name__ == '__main__':
        print("Directly execution")
        print("__name__ : ", __name__)
    else:
        print("Indirectly execution")
        print("__name__ : ", __name__)
```

Packages
------------------

- A single unit of multiple modules
- It is a simple folder fo multiple python file with consist of a special file `__init__.py` and in every sub folder also consist `__init__.py`
- Python 3.3 onwords this special file is optional.
- A package can contain subpackages also.
- We can resolve naming conflicts with package concept.
- We can identify our components uniquely
- Modularity, readability and maintability improved.

```
Folder structure of a package...
pkg1
  |
  |- __init__.py
  |- py01.py
  |- sub_pkg1
            |
            |- __init__.py
            |- py01.py
            |- py02.py
            |- py03.py
            |- sub_pkg1
                    |
                    |- __init__.py
            |- sub_pkg2
                    |
                    |- __int__.py
                    |- py01.py
  |- sub_pkg2
            |
            |- __init__.py
            |- py01.py
  |- sub_pkg3
            |
            |- __init__.py
```

- Importing ways
    - `import pkg` 
    - `import pkg.sub_pkg1`
    - `import pkg.sub_pkg2`
    - `import pkg.sub_pkg3`
    - `import pkg.sub_pkg1.sub_pkg2`
    - `import pkg.sub_pkg1.sub_pkg1`


Exception Handling:
-----------------------------

- It is recommended to handle error.
- It is important to smoothly termination of the program
- Every exception is class/object in py
- Handling code is present in `except` block
- 2 types of error occurs
    - Syntax error
    - Runtime error / logical error

Syntax Error
--------------------

- Typing error / coding mistake
- occurs while interpreting and compling
- Generate : `SyntaxError, NameError`

Runtime Error / Logical Error
----------------------------------

- Occurs at runtime
- Generate : `ZeroDivisionError, TypeError, ValueError, FileNotFoundError, EOFError`


How to handle:
---------------

```
try:
    read data from file
except(error):
    continue if something goes wrong
```

Exception Hierarrchy
----------------------------

```
BaseException
            |
            |- Exception
                        |
                        |- AttributeError
                        |- ArithmeticError
                                        |
                                        |- ZeroDivisionError
                                        |- FloatingPointError
                                        |- OverflowError
                        |- EOFError
                        |- NameError
                        |- LookupError
                                    |
                                    |- IndexError
                                    |- KeyError
                        |- OSError
                                |
                                |- FileNotFoundError
                                |- InterruptedError
                                |- PermissionError
                                |- TimeOutError
                        |- TypeError
                        |- ValueError
            |- SystemExit
            |- GeneratorExit
            |- KeyBoardInterrupt

```

Customized Exception Handling
------------------------------

- Case-1 : If no exception </br>
        Only try block and out of block code execute
- Case-2 : If error occurs and except block matched </br>
        Every line of code execute including except block
- Case-3 : If error occurs but except block is not match </br>
        Program terminated abnormally

```py
print("Hello")
print(10/0)   # Risky code
print("Bro")

# try:
#     risky code
# except (error):
#     Handling code


# Handling code

print("Hello")

try :
    print(10/0)   # Risky code
except ZeroDivisionError: # we can take here root exception (BaseException)
    print(10/2)

print("Bro")

```


How to print error msg?
---------------------------

```py
try:
    print(10/0)
except ZeroDivisionError as msg:
    print("error occured : ", msg) 
```

Single except block with multiple error:
-------------------------------------------

```py
except exception:
    # handling code

except exception as msg:
    # handling code

except (exception1, exception2,...):
    # handling code

except (exception1, exception2,...) as msg:      # here msg print the error description..
    # handling code

# default exception
except :    # here is not imp to provide error
    # handling code
```

`finally` block
----------------------

- `finally` block is always execute, if exception occurs or not after `try` block

- In case of pvm shutdown (`os.exit(0)`) `finally` block is not executed. 

```py
try:
    # risky code
    # open db connection
    # reading the data
except:
    # handling code
finally:
    # cleanup code
    # close db connection

```

Control flow of exception
---------------------------

```py
try:
    print("statement 1")
    print("statement 2")
    print("statement 3")
except:
    print("statement 4")
finally:
    print("statement 5")
print("statement 6")

```
- If no exception raise :</br>
    1->2->3->5->6 (normal termination)
- If an exception raise at statement-2 and exception matched :</br>
    1->4->5->6 (normal termination)
- If an exception raise at statement-2 and exception matched and another exception raise at statement 4 also :</br>
    1->5 (abnormal termination)
- If an exception raise at statement-2 but exception not matched :</br>
    1->5 (abnormal termination)
- If an exception raise at statement-5 :</br>
    1->2->3 (abnormal termination)
- If an exception raise at statement-6 :</br>
    1->2->3->5 (abnormal termination)

```py
# Nested exception

try:
    print('statement 1')
    print('statement 2')
    print('statement 3')
    try:
        print('statement 4')
        print('statement 5')
        print('statement 6')
    except:
        print('statement 7')
    finally:
        print('statement 8')
    print('statement 9')
except:
    print('statement 10')
finally:
    print('statement 11')
print('statement 12')

# check every case by yourself
```

`else` block
----------------------

- This works when try block have no error raise
- else vs finally : finally always execute but else execute when no error raise in try block
- We can't write try block only, there is finally or except block should exist.
- We can't write except block only, there is try block should exist.
- We can't write else block only, there is try with except block should exist.
- We can't write finally block only, there is try block should exist.
- try, except, else, finally this order is important.
- `try --> except`
- `try --> except 1 --> except 2`
- `try --> except --> else`
- `try --> finally`
- `try --> except --> finally`
- `try --> except --> else --> finally`
- `1 try --> n except --> 1 else --> 1 finally`


```py
try:
    # risky code
except:
    # will be executed if exception in try
else:
    # will be executed if no exeception in try
finally:
    # always executed if error raise or not
```

Customized Exception
-----------------------


