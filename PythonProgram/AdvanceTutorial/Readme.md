Logging in Python
--------------------------

- Log : History or Record of user or program activity like startup time, ending time, process duration, raise error, breaking point, users request and so on...
- Main advantage of log file we can perform debugging for any error
- Inbuit module name : `logging`
- Logging level : 6 (depends on severity)
    - `CRITICAL` (severity value = 50) : High severity
    - `ERROR` (severity value = 40) : 
    - `WARNING` (severity value = 30) : Alert to the programmer
    - `INFO` (severity value = 20)
    - `DEBUG` (severity value = 10)
    - `NOTSET` (severity value = 0)

How to implement logging?
------------------------------

- First we have to create a log file
- Logging level messages
- basicConfig() of logging module
    - `logging.basicConfig(filename='log.txt', level=logging.WARNING)`
    - `logging.debug(message)`
    - `logging.info(message)`
    - `logging.waring(message)`
    - `logging.critical(message)`
    - `logging.error(message)`
    
Debugging
-----------------

- `Defect/Bug` : Mismatch between excepted result and actual result.
- Debugging is the process of the check and fixing the problem.
- This happen only in development or testing envoirment.
- assert statements is used to debugging.
- assert vs print : after fixing the bug print requires delete but assert is not.

Type of assert statement
------------------------------

1. Simple Version
```py
assert conditional_expression   # true
    # code has no error
assert conditional_expression   # false
    # code has some error
```
2. Very Simple Version (Augemented Version)
```py
assert conditional_expression,message   # true
    # code has no error
assert conditional_expression,message   # false
    # code has some error
```


File Handling
---------------------

- In file handling concept we have to store min/less information, but if you want large data store go for database concept.
- For very huge data go for big data concept


Types of files
---------------------

1. Text File
    - .txt, .py etc..
2. Binary File
    - image, video etc..

Opening a file
---------------

`open()`
- f = open(file_name, mode)</br>
`f = open('abc.txt','r')`

The allowed modes in Python are :
1. `r` : open existing file for read operation. It is default mode.
2. `w` : open existing file for write operation. Override the existing file if created and if file is not created then its create that file.
3. `a` : open existing file for write operation. Do not override the existing file if created and if file is not created then its creted and write the file form ending.
4. `r+` : open existing file for read and write operation. Do not override the existing file if created and if file is not created then its creted and write the file form beggining.
5. `w+` : open existing file for write and read operation. Override the existing file if created and if file is not created then its creted and write the file form beggining. (write then read)
6. `a+` : open existing file for write and read operation. Do not override the existing file if created and if file is not created then its creted and write the file form ending. (append then read)
7. `x` : open new file for write operation.If file exits then it exit from file and raise FileExitError. (exclusive creation mode)

These all mode is applicable for text file, if we want modes for binary file then every mode is suffixed with b like : `rb, wb, r+b, w+b, a+b, ab, xb`

Closing file
-------------------

- It is highly recommeded to close the file after any read and write operation.
- `f.close()`

Various properties of the file object :
------------------------------------------

- `f.name` : file name
- `f.mode` : mode of the file
- `f.closed` : file is closed ?
- `f.readable()` : file is readable ?
- `f.writable()` : file is writeable ?


Writing data to the text file
-----------------------------------

`write()`
- f.write("str")
- f.write("list of lines")


Reading character data from the file
-----------------------------------------

- `read()` : read total data form file
- `read(n)` : read n character form file
- `readline()` : read single line form file at a time.
- `readlines()` : read all lines into a list

`with` statement
---------------------

- It close the file automatically if the programmer forget to close the file

```py
f = open('abc.txt','w')

with open('abc.txt','w') as f:
    # ...
    # ...
    # ...
    # perform some operation and close the file automatically out of the with block
```

Some inbuilt function for file
----------------------------

- `tell()` : tells the current position of cursor or file pointer.
- `seek()` : move the cursor to a particular location
    - `f.seek(offset,fromwhere)`
        - offset : no of position
        - fromwhere : form which location
    - fromwhere argument value :(in py 2 : 0,1,2 but in py 3 only 0 the default one.)
        - `0` : from beginning of the file (default value)
        - `1` : from current position
        - `2` : from end of the file


`os` & `sys` Module
----------------

- os module for file related opeation and sys module for system operation


Binary file handling
----------------------------

- managing image and video files
- handling csv file with `csv` module


Zipping and Unzipping file
---------------------------------

- Zipping file improves the performance and memory utilization
- Reduce transport time
- Inbuilt module : `zipfile` module


Working with directories
----------------------------

- Inbuilt module : `os` module
    - `os.getcwd()` : currend working directory
    - `os.mkdir('sub_dir')` : create sub directory in cwd
    - `os.makedirs('sub1/sub2/sub3/..')` : create multiple sub directory in cwd
    - `os.rmdir('sub_dir/')` : remove sub directory in cwd
    - `os.removedirs('sub1/sub2/sub3/..')` : remove multiple sub directory in cwd
    - `os.rename('oldname','newname')` : rename the file and folder in cwd
    - `os.listdir('dir')` : list the dir in cwd and return in list type
    - `os.walk(path,topdown=True,onerror=None,followlinks=False)` : list the dir and sub dir in cwd
    - `os.system('cmd string')` : run the cmd command string
    - `os.stat('file')` : stats of file


Pickling and unpickling of objects:
--------------------------------------

Pickling is the process of writing total state of object in a file and reverse process of reading total state of object in a file is called Unpicking. ( in other language, this process called serialization concept )

Implimentation of Pickling and Unpickling
----------------------------------------

- Inbuilt module : `pickle` module
    - `pickle.dump(obj, file)` : for pickling
    - `pickle.load(file)` : for unpickling


Garbage Collection
---------------------

- It's destroy the useless object automatically (Main job)
- Done by pvm
- Which object will be destroyed ?
	- which object has not any reference variable.

How to enable and disable GC in out program?
------------------------------------------

- By default gc is enable.
- Inbuilt module : `gc` module
	-  `gc.isenabled()` : is enable or not ?
	-  `gc.disable()` : to disable gc
	-  `gc.enable()` : to enable gc

Destructors
------------------

- It is the part of garbage collector
- Main job of destructor is to perform cleanup activities of useless object
- Before destroying useless object by gc, it is going to perform cleanup activities of the useless object.
- Destructor named with `__del__()`


How to find number of references of an object ?
--------------------------------------------------

- `sys.getrefcount(obj_ref)`

Regular Expression
----------------------

- Used for pattern search
- It uses group of string to represent search pattern
- Main application
    - Search Pattern
    - Validation
    - Translator : Compiler, Interpreter, Assemblers
    - Finite Automata (Digital Circuits)
    - Communication Protocals : TCP/IP
- Inbuilt module : `re` module
    - `re.compile()` : to compile pattern
    - `re.finditer()`: to match pattern
    - `re.start()` : start index of match
    - `re.end()` : end+1 index of match
    - `re.group()` : returns match string

Character Class for pattern
------------------------------

- `[abc]` : either a or b or c
- `[^abc]` : except a and b and c
- `[a-z]` : any lower case
- `[A-Z]` : any upper case
- `[a-zA-z]` : any alphabet char case
- `[0-9]` : any digit
- `[a-zA-Z0-9]` : any alphanumeric
- `[^a-zA-z0-9]` : except alphanumeric


Predefined Character Class
-----------------------------

- `\s` : search for space character
- `\S` : except space character
- `\d` : search for any digit [0-9]
- `\D` : except digit
- `\w` : search for alphanumeric character [0-9a-zA-Z]
- `\W` : search for special character
- ` . ` : search for every character

Quantifiers
-----------------

- The number of occurence
- `a` : exactly one 'a'
- `a+` : atleast one 'a'
- `a*` : any number of 'a' including 0 times 'a' also
- `a?` : atmost one 'a' (either one 'a' or 0 times 'a')
- `a{n}` : exactly n times 'a'
- `a{m,n}` : minimum m times 'a' and maximum n times 'a'
- `a{2}a*` : exactly two times 'a' after any number of a's
- `^a` : starts with 'a' or not ?
- `a$` : ends with 'a' or not ?

Important function of `re` module
--------------------------------

- `re.match()` : to check the pattern is at the beginning or not, if present then return match pattern otherwise return None.
- `re.fullmatch()` : to check the pattern is matched with complete string or not if present then return match otherwise None.
- `re.search()` : to search the given pattern in target string, it match of the first occurrence and if not find then return None
- `re.findall()` : find all the match and return the list of occurrence and if not find the return None
- `re.sub(pattern, replacement, targetstring)` : substitution or replacement and return replace string
- `re.subn()` : Works same as sub, how many replacement happen, and return is tuple (not string), tuple --> (result_string, no of replacement) --> t[0], t[1]
- `re.split()` : split the string according to pattern (same as string split()) return list
- `re.IGNORECASE` : ignore the upper and lower case, search in both cases like easy, Easy, EASY all are same.


```
^ : starts with
Ex --> ^learn, ^is ... etc

$ : ends with
Ex --> re$, ly$

. : anything
* : any number of times
```

Web Scrapping by using Regular Expression
---------------------------------------

- Inbuilt module : `urllib` module
    - `urllib.request()` : to request the server


Multi-threading
--------------------

`Multitasking` : Executing several task simultaneously
    - Process besed multitasking
    - Thread besed multitasking
With the help of multitasking we can reduce execution time and improve performance of the program.

Process Based Multitasking
-------------------------------

Executing several task simultaneously where each task is a seperate independent process. </br>
Ex : Typing and playing music at a same time both are independent from each other </br>
It happens at os level.


Thread Besed Multitasking
---------------------------

In a single program, Executing several task simultaneously where each task is a seperate independent process. </br>
Ex : In a vs code editor Typing and code highlighting executing at the same time </br>
It happens at program level.

Thread
---------

1. Flow of Execution
    - Single threaded program
        - one by one (single flow of execution)
    - Multi threaded program
        - many threads runs at a time (multi flow of execution)
2. Inbuilt module : `threading` module has `Thread()` class
    - `current_thread()`
    - `current_thread().getName()`   # getName() is deprecated
    - `current_thread().name`
    - `current_thread().setName('kush')`  # setName() is deprecated
    - `current_thread().name = 'kush`
    - `current_thread().ident` : id number
    - `current_thread().active_count()` : active no of thread


Ways of creating thread in python
------------------------------

3 ways :
1. Creating a thread without using any class
2. Creating a thread by extending Thread class
3. Creating a thread without extending Thread class


Daemon Thread:
--------------------

- Backround execution thread like main thread ex:gc
- MainThread is always non daemon, but for all remaining threads daemon nature will be inherited form parent, and these child thread is changable to daemon thread.
- If last non daemon threads terminates then by default daemon threads will be terminated.
- Active thread nature is not changable.
- `t.isDaemon()` : to check daemon or not (deprecated)
- `t.daemom` : to check daemon or not
- `t.setDaemon()` : to set (deprecated)
- `t.daemon=True/False` : to set


Synchronization
-------------------

- At a time only one thread.(Don't fight if multiple threads are available.)
- `Lock` : lock the a single thread and to waits other to be released the locked one.
- `RLock` : provide recursive lock and same works as lock
- `Semaphor` : allows multiple threads to lock at one for execution.

