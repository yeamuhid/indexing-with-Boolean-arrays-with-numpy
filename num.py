Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> a=np.array([[6,7,8],[1,2,3],[9,3,2]])
>>> a
array([[6, 7, 8],
       [1, 2, 3],
       [9, 3, 2]])
>>> for row in a:
...     print (row)
... 
...     
[6 7 8]
[1 2 3]
[9 3 2]
>>> for cell in a.flat
SyntaxError: expected ':'
>>> for cell in a.flat:
...     print cell
...     
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>>  print (cell)
...  
SyntaxError: unexpected indent
>>> 
>>> 
>>> for cell in a.flat:
...     print(cell)
... 
...     
6
7
8
1
2
3
9
3
2

