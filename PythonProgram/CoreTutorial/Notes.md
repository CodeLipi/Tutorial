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
