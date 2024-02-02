[Go to HomePage](/README.md)

![Ooops](/PythonExample.png "Oops Concpt")

Class, Object : 
----------------------

- **Class**: blueprint/plan/model/design for object --> existing on paper.
- **Object**: physical existing of a class.

	> Ex : TV Model design : class, Each TV : object

```py
class name_of_class:
	''' doc string '''

	# properties (var)
	# methods (action/ behaviour/ function)
```
*Every object has properties and behaviour.*



Types of variables : (in oops not in functional)
----------------------------------------------
1. Instance variables (Object level variables)
2. Static variables (Class level variables)
3. Local variables (Methods level variables)


Types of Methods :
---------------------
1. Instance Methods (Object related method)
2. Class Methods (Class related method)
3. Static Methods (General utility method)


Reference variables :
---------------------
- This can be used to refer objects
- By using Reference variables, we can invoke functionlaity of object.
	> Ex : TV (obj) <--- Remote(reference variable)
- This invoke the functionality of TV like increase/decrease volume or change channel etc.
- For a single object has one or many references.
	> - For any class, we can create any number of object (one-to-many)
	> - For any object, we can take any number of rreference variables (one-to-many)


**How to create object in python ?**
`reference_var = classname()`



self variable :
---------------
1. self is a reference variable, which is always pointing to current object
within the python class, to access current object, we can use self.
2. The first argument of the constructor is always self.
3. The first argument of the instance methods is always self.
4. We are not required to provide value for self variable, PVM itself will provide value.
5. We can use self always within the class only.
	- Inside constructor, we can use self to declare object related vaiables (instance variables)
	- Inside instance method, we can use self to access the values of instance variables
6. self is not a keyword. We can use any name like delf/kelf/relf...etc




Constructor :
----------------
1. Constructor is a special method.
2. The name of constructor is always `__init__()`
3. We are not required to call constructor explicitly. It will be executed atomatically when we are creating an object.
4. Per object, constructor will be executed only once.
5. The main purpose of constructor is to declare and initialize instance variables.
	`__init__` means initialization
6. Constructor should take atleast one argument (atleast self)
7. Within the python class constructor is optional. If we are not providing constructor default constructor will be provided by PVM
8. We can call constructor explicitly then it will be executed just like a normal method and new object won't be created.
9. Constructor/Method overloding are not possible in python.
	- It always providing the preference to the last constructor




Difference between Method vs Constructor:
------------------------------------------
**Method:**
1. Method name can be anything.
2. Method won't executed automatically, we have to call explicitly.
3. Per object, we can call method any no of times.
4. Inside method, we can write logic based on requirement.

**Constructor:**
1. Constructor name should be `__init__().`
2. Constructor wil be executed automatically whenever we are creating an object.
3. Per object constructor will be executed only once.
4. Inside constructor we have to write code to declare and initialize instance variables.




Instance variable:
---------------------------
1. If the value of a vaiable is varied from object to object, such type of variables are called instance variable / Object level variables.
2. For every object a separate copy will be created.
3. In general we can define instance variables inside constructor by using self.



Static variable:
----------------------
- If the value of a variable is not varied from object to object then it is not recommended to declared that variable as instance variable, so it is called static variable/ class level variable.
- In the case of instance variable, for every object has separate copy.
- But in the case of static variable, a single copy will be created and shared to every object of that class.
	> Most of times, static variables should be declared within the class directly.




Local Variable :
-----------------------
To meet temporary requirement of the programmer, we can declare variable directly inside a method.
Method level variable.



Instance Method :
-------------------
- If we are accessing instance variables (atleast one instance variable)
(whether we are using static or/and local variable or not.)
- The first argument to the instance method should be self.

**where to declare instance variable ?**
1. Inside constructor by using self
2. Inside instance method by using self
3. Outside of the class by using object reference.

**How to access instance variable ?**
- Within the class by using self (self.var_name)
- Outside of the class by using object reference (obj_reference.var_name)

**How to delete instance variable ?**
- Within the class :
	`del self.var_name`*
- Outside of the class :
	`del obj_reference.var_name`




Class vs Static Method :
------------------------------

*Are you using any instance variable :*
- if *Yes* : Instance Method
- if *No* : whether Class Method or Static Method

*Are you using any static variable / class level variable :*
- if *Yes* : Class Method
- if *No* : Static Method


1. The first argument to the instance method is self, which is pointing to the current object.
2. The first argument to the class method is cls, which is pointing to corresponding class object.

>	- instance method --> no decorator
>	- class method --> @classmethod
>	- static method --> @staticmethod


*Where to declare static variable ?*
1. In general we can declare static variables within the class directly, but outside of any method.
2. Inside constructor and instance methods, by using class name.
3. Inside class method by using either classname or cls variable.
4. Inside static method by using classname.
5. From outside of the class by using class name.


- We can declare static variable within the class directly.
- Either by class name or by cls variable.


*How to access static vaiable ?*
- We can access static variable by using self, classname, cls and object reference.
- But recommended to use by class name.
```py
print(self.a)      	# this works fine
print(Test.a) 		# this is recommended
```
>- in case of print(self.a), PVM always check first for instance variable if it is not present then go to the static variable.


**- How to modify(update) the value of static variable ?**- 
- We should update the value of static variable either by classname or by cls variable.
- We can't use self or object reference to update static variable value.


>- Declare static var : classname, cls variable
>- Access static var : classname, cls, self, object reference
>- Update static var : classname, cls variable


Getter and Setter Methods
-------------------------------

- Getter and Setter method is only works for instance method (90% of the time)
- Getter method --> to get the value (accessor method)
- Setter method --> to set or modify the value (mutator method)

```py
# for security reason getter and setter method implements

s = Student()
s.setName('Jenny')
print(s.getName())


def setName(self, name):
	self.name = name
def getName(self):
	return self.name
```

Inner Class / Nested Class
--------------------------

- Class inside an another class is inner class
- Without existing one typeof object, if there is no chance of existing another type of object then we should go for inner classes.
- Ex : Car(individual)		Engine(individual)  but both are linked.
- Ex : University(individual)		Department(individual)  but both are linked.
- Ex : Human(individual)		Brain(individual)  but both are linked.
```py
class Car:
	class Engine:
		pass

```
- Without existing outer class object, there is no chance of existing inner class object. Inner class object is always associated with outer class.


Inheritance
---------------

**How we can use member of a class inside another class ?**
- By using Composition (Has-A Relationship)
	`class Car <--------- class Engine`
	- class Car Has-A Engine Reference
	- Code reusability

- By using Inheritance (Is-A Relationship)
	- Everything is available to child class what the parent class has.
	- If anything present in child class then priority goes to child and if not then priority goes to parent class.

- `super()` method : it's priorities the paraent class
	- super() is not used for accessing instance variable, only class level variable.

Types of Inheritance
--------------------------

1. Single Inheritance
2. Multi level Inheritance
3. Hierarchical Inheritance
4. Multiple Inheritance
5. Cyclic Inheritance (Not supported in python)
6. Hybrid Inheritance

Single Inheritance
-------------------

- Member of a class is inherited by an another class

```
			Parent class
			   ^
			   |
			   |
			   |
			Child class
```

Multilevel Inheritance
--------------------------

- Member of a class is inherited by multiple level another class

```
			Parent class
			   ^
			   |
			   |
			   |
			Child class
			   ^
			   |
			   |
			Myself class			
```

Hierarchical Inheritance
-----------------------------

- Member of a class is inherited by multiple at single level another class

```
			Parent class
	-----------------------------
	   ^                    ^
	   |                    |
	   |                    |
	Child 1 class      Child 2 class			
```

Multiple Inheritance
------------------------
- Member of multiple parent classes is inherited by a single child class.

```
    Parent 1 class         Parent 2 class
	   ^                       ^
	   |                       |
	   |                       |
	   --------------------------
	          Child class
```

Hybrid Inheritance
--------------------

- Combination of above inheritance

```
		 Grand Parent class
	-----------------------------
	   ^                    ^
	   |                    |
	   |                    |
	Father class      Uncle class
	   ^                    ^
	   |                    |
	   |                    |
	-----------------------------
            Child class				
```

Method Resolution Order
------------------------------

- Follow C3 algorithm and linearization order
- if you want to print the execution order then `object.mro()`
- If multiple parent is available then python will consider from left to right of declaration. `class Child(P1,P2,P3)`


```
					A
			 B	           C	
		D	        E            F
		     G             H
			        I	

	# searching from bottom to top	
```

Polymorphism
------------------

- One name but many forms
- Overloading and Overriding used in the concept of polymorphism


Overloading
----------------

- Operator Overloading
	- `+` : used for addition, concatenation
	- `*` : used for multiplication, repeatition
	- `__add__()` : magic method for `+` operator
	- `__sub__()` : magic method for `-` operator
	- `__mul__()` : magic method for `*` operator
	- `__div__()` : magic method for `/` operator
	- `__floordiv__()` : magic method for `//` operator
	- `__mod__()` : magic method for `%` operator
	- `__pow__()` : magic method for `**` operator
	- `__iadd__()` : magic method for `+=` operator
	- `__isub__()` : magic method for `-=` operator
	- `__imul__()` : magic method for `*=` operator
	- `__lt__()` : magic method for `<` operator
	- `__gt__()` : magic method for `>` operator
	- `__le__()` : magic method for `<=` operator
	- `__ge__()` : magic method for `>=` operator
	- `__eq__()` : magic method for `==` operator
	- `__ne__()` : magic method for `!=` operator
- Method Overloading by default this is not possible in python but with different arguments with same name is possible, only last/recent one is acceptable.
	- possible with 2 ways
		- with default args
		- with variable no of args
- Constructor Overloading is not possible just like method overloading but we make possible with like method overloading

Overriding
--------------

- Method Overriding
- Constructor Overriding

Duck Typing Philosophy of Python:
----------------------------------

Python is dynamically typed language so we can not decide what type of obj passed as a argument.
`If it walks like a duck and talks like a duck then it is duck`
```
def f1(obj):
	obj.talk()
```

- `hasattr(obj,'attr_name')`

Abstraction
----------------

Incomplete information about anything is abstraction.
- Abstract Method (partial declaration of a method)
	- `@abstractmethod` decorator used in method and this decorator available in `abc` module
- Abstract class
	- partial implementation of a class
	- child class of `ABC` class
	- can't instantiate abstract class without an implementation for abstract method, we have to remove the @abstractmethod 
	- child class provides the implementation of parent abstract class.
- Interface
	- if abstract class contains only one abstract method then this is called interface.


Interface vs Abstract vs Concrete class
--------------------------------------------

- Interface
	- if we don't know anything about implementation, just we have requirement specification then we should go for interface.
	```py
	class CollageAutomation(ABC):
		@abstractmethod
		def m1(self): pass
		@abstractmethod
		def m2(self): pass
		@abstractmethod
		def m3(self): pass
		@abstractmethod
		def m4(self): pass
	```
- Abstract
	- talks about partially implementation of abstract class
	```py
	class ImplCls(CollageAutomation):
		def m1(self): print('m1 implementation')
		def m2(self): print('m2 implementation')
		def m3(self): print('m3 implementation')
	```
- Concrete Class
	- talks about completely implementation and ready to provide service
	```py
	class ConcreteCls(ImplCls):
		def m4(self): print('m4 implementation')
	```

Public, Private and Protected
--------------------------------

- `x = 10` : public
- `__x = 10` : private (not accessed outside of the class)
- `_x = 10` : protected (just a conventation)
- `MAX_VALUE = 10` : constant (just a conventation)
- `objref._classname.__variable` : using this we can not access private variable outside of the class


`__str__()` method overriding
--------------------------------

```py
class Test:
	def __init__(self,name,id):
		self.name = name
		self.id = id
	def __str__(self):
		return 'name : {},id : {}'.format(self.name,self.id)
```