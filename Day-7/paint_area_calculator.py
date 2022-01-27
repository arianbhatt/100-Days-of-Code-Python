import math
def no_of_cans(h,w,per):
    # here per is area that a can, can cover
    area=h*w
    cans=math.ceil(area/per)
    print(f"{cans} are required to cover the wall")
height=int(input("Enter the height of the wall "))
width=int(input("Enter the width of the wall "))
coverage=5
no_of_cans(height,width,coverage)
