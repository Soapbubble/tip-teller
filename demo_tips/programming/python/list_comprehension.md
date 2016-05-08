[tip]
# List comprehension - definition
A list literal enclosed in square brackets ([...]) can be a simple list of expressions or a list comprehension expression of the following form:

```
[expr for target1 in iterable1 [if condition1]
      for target2 in iterable2 [if condition2] ...
      for targetN in iterableN [if conditionN] ]
```
List comprehensions construct result lists: they collect all values of expression expr, for each iteration of all nested for loops, for which each optional condition is true. 

# List comprehension - examples

```Python
>>> [ord(x) for x in 'spam']
[115, 112, 97, 109]
>>> list(map(ord, 'spam'))       # Use list() in 3.X
[115, 112, 97, 109]
```

```Python
>>> [x ** 2 for x in range(5)]
[0, 1, 4, 9, 16]
>>> list(map((lambda x: x ** 2), range(5)))
[0, 1, 4, 9, 16]
```

```Python
>>> [x for x in range(5) if x % 2 == 0]
[0, 2, 4]
>>> list(filter((lambda x: x % 2 == 0), range(5)))
[0, 2, 4]
```
