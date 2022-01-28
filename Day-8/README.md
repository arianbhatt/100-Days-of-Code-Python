# Day-8

## Dictionaries and Nesting
Every Dictionary has Two Parts 
The 'Key' and the Associated 'Value'
Represented as {key:value}
```python
dict={"Bug":"The Defination of Bug","Function":"The Defination of Function","Loop":"The Defination of Loop"}
```
Here Bug is the key for the "The Defination of Bug" value.
```python
print(dict["Bug"])
```
Provide the key in the actual datatype.
Adding new item to dictionary
```python
dict["Python"]="Some Info about Python"
```
we can empty the dicitonary if we want
```python
dict={}
```
to edit a key's value
```python
dict["Bug"]="Better Defination of Bug"
```
we can loop through the dictionary
```python
for var in dict:
	print(var)
```
this only gives the key
```python
for var in dict:
	print(dict[var])
```
now we got the values really easy.

## Nesting
Putting one inside another List,List Dictionary,List, Dictionary,Dictionary
```python
[{
    Key:[List],
    Key2:{Dict},
},
{
    Key:Value,
    Key2:Value
}]

