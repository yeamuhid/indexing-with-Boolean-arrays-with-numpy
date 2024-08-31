Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import numpy as np
n= [6,7,8,]
n[0:2]
[6, 7]
n[-1]
8
a=np.array([6,7,8,])
a[0:2]
array([6, 7])
a[-1]
np.int64(8)
a=np.array([[6,7,8,],[1,2,3],[9,3,2]])
a=np.array([[6,7,8,],[1,2,3],[9,3,2]])a
SyntaxError: invalid syntax
a=np.array([[6,7,8,],[1,2,3],[9,3,2]])
a
array([[6, 7, 8],
       [1, 2, 3],
       [9, 3, 2]])
a=np.array([[6,7,8,],[1,2,3],[9,3,2]])
a[1,2]
np.int64(3)
a[0:2,2]
array([8, 3])
a[-1]
array([9, 3, 2])
a[:,1,:3]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a[:,1,:3]
IndexError: too many indices for array: array is 2-dimensional, but 3 were indexed
a[:,1:3]
array([[7, 8],
       [2, 3],
       [3, 2]])
[3, 2]])
SyntaxError: unmatched ']'






SyntaxError: unmatched ']'
SyntaxError: invalid syntax




a=np.array([[6,7,8,],[1,2,3],[9,3,2]])



import numpy as np
a=np.array([[6,7,8,],[1,2,3],[9,3,2]])
a
SyntaxError: multiple statements found while compiling a single statement
a=np.array([[6,7,8,],[1,2,3],[9,3,2]])
a
SyntaxError: multiple statements found while compiling a single statement


a
array([[6, 7, 8],
       [1, 2, 3],
       [9, 3, 2]])
[9, 3, 2]])for row in a
SyntaxError: unmatched ']'
SyntaxError: unmatched ']'
SyntaxError: invalid syntax

for row in a
SyntaxError: expected ':'







































>>> 

>>> 

... 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> import numpy as np
>>> a=np.array ([6,7,8],[1,2,3],[9,3,2,]])
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
>>> a=np.array ([[6,7,8],[1,2,3],[9,3,2,]])
>>> a=np.array ([[6,7,8],[1,2,3],[9,3,2,]])
>>> a
array([[6, 7, 8],
       [1, 2, 3],
       [9, 3, 2]])
>>> for row in a:
... 
... 
... 
... 
... 
... 
... 
... 
... 
... print (row)
SyntaxError: expected an indented block after 'for' statement on line 1
