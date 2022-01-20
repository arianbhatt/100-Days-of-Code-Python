# Day-0

## Getting Started 
Firstly we will get Python installed on our system.
read how to get it on your system from python.org
or you can watch a video tutorial.

### Hello World
First thing any programmer learns when learning a language is usually how to print out something and continuing the legacy.
we use the print() function in python.

```python
print("Hello World")
```
A Quick Info anything inside "quotes" is a string.

### How to take input in Python

```python
input("Message for the user ")
```
in python we use the input() function to take input from the user by default the input function takes input as string only.
```
s=input("Enter Something ")
```
We made a variable for the string named s.
To take numbers from user typecast the input string.
```python
a=int(input("Enter a number "))
b=float(input("Enter a Number "))
```
we just took input as an integer and a floating variable.

### Playing with strings
We can do a lot of stuff with strings.
- Concatination: we use '+' operator to concatinate two strings.
```python
print("Hello"+" "+"World")
```
The Output would be:
```sh
Hello World
```
- Strings are actually Indexed starting with 0.
```python
a="Hello World"
print(a[2])
```
The Output would be:
```sh
l
```
More about Datatypes and Operations in Day-1
