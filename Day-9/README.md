# Day-9

## Functions with outputs

```python
def calculate():
    result=3*5
    return result
ans=calculate()
```
here calculate() will return a value here result and when calling calculate() we have to use a variable to catch the returned value.

## Docstrings
way to create documentation for our own function.
First Idented Line after def write between """Docstring What does it do """
## Recursion
Answer of our First Calculation becomes input for ouw next calculation.
```python
def add(n1,n2):
    return n1+n2
answer1=add(2,3)
answer2=add(answer1,3)
```
note: this is not what recursion is exactly this is to just give an idea.

