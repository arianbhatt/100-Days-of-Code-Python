# github@arianbhatt

student_heights=input("Enter a list of Student Heights ").split()
# example input 170 180 190 175 165
l=len(student_heights) # total number of students
s=0 # to hold the total sum of heights
for i in student_heights:
    s=s+int(i)
avg=s/l
rounded=round(avg)
print(f"The Average Height of students is {rounded}")


