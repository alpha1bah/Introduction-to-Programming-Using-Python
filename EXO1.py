# Eoxo 1.1
# Display three different message

print("Welcome to Python.")
print("Computer Science is fun.")
print("Python is fun.")

# *************************
# Exo 1.2
# Write a program that displays 'Welcome to Python' five times
print("Welcome to python. "*5)

#   ***********************************
# Exo 1.3
# Display a patern. Write a program that displays fun
print("FFFFFFF    U     U    NN          N")
print("FF         U     U    NNN         N")
print("FFFFFFF    U     U    NN  N       N")
print("FF          U   U     NN    N     N")
print("FF           UUU      NN        NNN")


# Exo 1.4
# Print a table
print("a             a^2            a^3")
print("1              1              1")
print("2              4              8")
print("3              9              9")
print("4              16             64")

# Exo 1.5
# (Compute expressions) Write a program that displays the result of   (9.5 * 4.5 - 2.5 * 3) / (45.5 - 3.5)
print("(9.5 * 4.5 - 2.5 * 3) / (45.5 - 3.5) = ",(9.5 * 4.5 - 2.5 * 3) / (45.5 - 3.5))

# Exo 1.6
#  (Summation of a series) Write a program that displays the result of 1+2+3+4+5+6+7+8+9
print("1+2+3+4+5+6+7+8+9=",1+2+3+4+5+6+7+8+9)

# 1.7
# Write a program that displays the result of 4 * ( 1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + ... )
print("4 * ( 1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + ... )= ",4 * ( 1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 ))
print("4 * ( 1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + 1/13 - 1/15) =", 4 * ( 1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + 1/13 - 1/15))


# Exo 1.8
# (Area and perimeter of a circle) Write a program that displays the area and perimeter of a circle that has a radius of 5.5 using the following formulas:
#
# perimeter = 2 * radius * p
#  area = radius * radius * p
radius = 5.5
pi = 3.14
area = radius * radius * pi
perimeter = 2 * radius * pi
print("The area is:", area)
print("Perimeter= ", perimeter)



# Exo 1.9
# (Area and perimeter of a rectangle)
# Write a program that displays the area and perimeter of a rectangle with the width of 4.5 and
# height of 7.9 using the following formula: area = width * height
width = 4.5
height = 7.9
area = width * height
print("The area is: ", area)

# 1.10  (Average speed) Assume a runner runs 14 kilometers in 45 minutes and 30 seconds.
# Write a program that displays the average speed in miles per hour. (Note that 1 mile is 1.6 kilometers.)
#t= 45 * 60 + 30
#print("time in second",t)
#t1=t/3600
#print("time in hours", t1)

t2=45/60+30/3600
print("time in hours", t2)
x = 14 * 1/1.6
print("Distance in miles is: ", x)
v=x/t2
print("The average speed is: ", v, "m/s")


# *1.11 (Population projection) The US Census Bureau projects population based on the following assumptions:
# One birth every 7 seconds One death every 13 seconds One new immigrant every 45 seconds Write a program
# to display the population for each of the next five years. Assume the current population is 312032486 and
# one year has 365 days. Hint: in Python, you can use integer division operator // to perform division.
# The result is an integer. For example, 5 // 4 is 1 (not 1.25) and 10 // 4 is 2 (not 2.5).
p = 312032486
t = 365 * 24 * 60 * 60
birth = t // 7
death = t // 13
immigration = t // 45

print("initial population: ", p)

p1 = p + birth - death + immigration
print("Population in first year: ",p1)

p2 = p1 + birth - death + immigration
print("Population in second year: ",p2)

p3 = p2 + birth - death + immigration
print("Population in third year: ",p3)

p4 = p3 + birth - death + immigration
print("Population in fourth year: ",p4)

p5 = p4 + birth - death + immigration
print("Population in fifth year: ",p5)