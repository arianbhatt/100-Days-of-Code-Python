# Day-2

## Control Flow with if else and Conditional Operators

A Common example of conditional operations is if else statements

```python
if condition:
	do this
else:
	do this
```
a short snippet of example

```python
print("Welcome to the rollercoaster!")
height=int(input("What is your Height?"))
if height >= 120:
	print("You can ride the Rollercoaster")
else:
	print("Sorry, you have to grow taller before you can ride.")
```
we can use multiple if else inside in else statements this is called nested if else statements.
```python
if condition:
	if another condition:
		do this
	else:
		do this
else:
	do this
```

In cases that there are more than 2 conditions we use elif
```python
if condition1:
	do A
elif condition2:
	do B
else:
	do this
```
## Logical Operators
and, or, not
For and operator both conditions have to be true
For or operator any one of the condition has to be true
```python
a=10
a>15 and a<13
```
we will get false

More stuff Day 4
