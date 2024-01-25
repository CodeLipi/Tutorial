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

- Python provides some inbuilt function :
    - `print()` : printing / output
    - `type()` : tell about data type
    - `id()` : address of object

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
- Inbuilt function : 
```py
append() : for data insert
remove() : for data remove
# but not applied on tuple 
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
- Inbuilt function :
```py
add() : for data insert
remove() : for data remove
# but not applied on frozenset
```

Dictionary
-------------------

- By default mutable.
- Key-value pair data
- Key : Not Duplicate, Value : Duplicate allowed
- Growable and reducable
- `empty_dict = dict()`
- `single_data_dict = {'key': 42}`
- Inbuilt function :
```py

```


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
-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
