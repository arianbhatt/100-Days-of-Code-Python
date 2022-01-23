# Day-3

## Randomisation

Adds Unpredictably to our Python Project.
Programming/Computers in general to create randomness use pseudorandom number generator (PRUG)
Python uses 'Mersenne Twister'

In Python we can use the Random module to do randomisation.

## examples of random

```python
a=random.randint(1,10)
# random funtion generates a floating number between 0 and less than 1
b=random.random()
```
seed number is used to generate a random number according to the seed if you use the same seed again. we will get the same random values
```python
num=int(input("Create a Seed number: "))
random.seed(num)
```
## Lists 

List is Data Structure, a way of storing data in python. To Store data which has some connection with each other and Provides Order to data.
Lists can have any datatype.

```python
l=[item1,item2,item3]
```
this is a list 
Note: Lists are indexed.

To add to data to end of a list.
```python
l.append(item4)
l.extend([item5,item6,item7])
```
now item4 is appended to the end of the list l.
and after that item5 item6 and item7 is also appended.

note: whoispaying.py we use split() it splits the string by the seperator and makes it a list.
We can have lists inside lists nested lists.

Learn to visit Stackoverflow.

Python Loops on Day-4
