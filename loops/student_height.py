
# Instructions 
# you are going to write a program that calculate the average student height from a list of heights 
# eg. student_height = [180, 12, 45, 56, 6645, 5454, 454, ]

# the average hight can be calculated by adding all the height together and dividing by the total number of heights 
# eg. 
# 180 + 12 +  45 + 56 + 6645 + 5454 + 454

# There are a total of 7 heights in the student heights 

# 1146 ÷ 7 =  163.7142857142857
# Average height rounded in the nearest whole number = 167


student_height = input('input a list of student heights ').split()
for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])
print(student_height)



