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

- Only attribute : `True, False`

