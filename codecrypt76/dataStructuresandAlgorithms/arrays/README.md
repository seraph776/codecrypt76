# Arrays

Array is a container which can hold a fix number of items and these items should be of the same type. 

## Important terms

- **Element** − Each item stored in an array is called an element.
- **Index** − Each location of an element in an array has a numerical index, which is used to identify the element.


## Basic Operations

The basic operations supported by an array are as stated below −

- **Traverse** − print all the array elements one by one.
- **Insertion** − Adds an element at the given index.
**- Deletion − Deletes an element at the given index.**
- **Search** − Searches an element using the given index or by the value.
- **Update** − Updates an element at the given index.

## Creating an Array

```python
from array import *

arrayName = array(typecode, [Initializers])
```


| Typecode | Value                                       |
|----------|---------------------------------------------|
| `b`      | Represents signed integer of size 1 byte    |
| `B`      | Represents unsigned integer of size 1 byte  |
| `c`      | Represents character of size 1 byte         |
| `i`      | Represents signed integer of size 2 bytes   |
| `I`      | Represents unsigned integer of size 2 bytes |
| `f`      | Represents floating point of size 4 bytes   |
| `d`      | Represents floating point of size 8 bytes   |


### Example

```python
from array import *

array1 = array('i', [10,20,30,40,50])

for x in array1:
   print(x)
```

## Accessing Array Element

```python
from array import *

array1 = array('i', [10,20,30,40,50])

print (array1[0])

print (array1[2])
```

## Insertion Operation

```python
from array import *

array1 = array('i', [10,20,30,40,50])

array1.insert(1,60)

for x in array1:
   print(x)
```

## Deletion Operation

```python
from array import *

array1 = array('i', [10,20,30,40,50])

array1.remove(40)

for x in array1:
   print(x)
```

## Search Operation

```python
from array import *

array1 = array('i', [10,20,30,40,50])

print (array1.index(40))
```

## Update Operation

```python
from array import *

array1 = array('i', [10,20,30,40,50])

array1[2] = 80

for x in array1:
   print(x)
```