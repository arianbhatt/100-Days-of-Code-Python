# Day-1 

## Understanding Data Types 

Unlike most languages Python assigns the data types with respect to the value provided to the variable.
The Datatypes can be broadly classified as integer, floating, string.
to initialise a varible just type

```python
var_name=1
var_name2=1.0
var_name3="Hello World"
```
Check the Datatype with the Help of type function
```python
print(type(var))
```
We can change Datatypes (if feasible)
for example:

```python
var_name="123"
var_name2=int(var_name)
print(type(var_name2))
```
the output would be 
```sh
<class 'int'>
```
## Mathematical Operations

They work the same way as they work in real life.
A special thing to keep in mind. for Python3 and up

```python
print(12/3)
print(12//3)
```
both these commands give different output
/ will give use floating result
// will give the nearest floor-integer 

## Special Notes

Look into

```python
print(3**2)
```
this statement is just 3 to the power 2

next thing is fstrings
```python
age=int(input("How old are you? "))
years_left=90-age
days_remaining=years_left*365
weeks_remaining=years_left*52
print(f"You have {days_remaining} days, {weeks_remaining} weeks, {years_left} years")
```
in this in the print statement an f string is used which treats things inside {} as variables as gives expected output.

```sh
How old are you? 18
You have 26280 days, 3744 weeks, 72 years
```
