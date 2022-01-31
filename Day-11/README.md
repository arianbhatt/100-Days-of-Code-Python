# Day-11

## Scope
The values of variable and declaration of variables is limited by their scope.
usually divided as local and global.
example: local scope - scope inside functions

### To Modify a global variable
define global variable inside the funtion.
```python
a=1
def fun():
    global a
    a+=1
    print(f"New Value of a: {a}")
```

## Global constants
Variable names in capital, variables we do not want to change.
example: value of pi or something.

## The Number guess game
Check the code ^_^

