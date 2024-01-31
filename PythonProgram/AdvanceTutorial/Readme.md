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

- It's destroy the useless object automatically
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