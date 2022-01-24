# github@arianbhatt
# using for loop to find the lowest score from the given list

student_scores=input("Input a list of student scores ").split()

# example input 20 30 12 40 50 45
# the split() divides the string input into a list of strings
high=0
for i in student_scores:
    if(int(i)>high):
        high=int(i)
print(f"The highest score in the class is: {high}")

# we can also change the list of strings to numbers
# for i in range(0,len(student_scores):
#   student_scores[i]=int(student_scores[i]
# print(max(student_scores))

