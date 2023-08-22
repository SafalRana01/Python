# This program prints Hello, world!

print('Hello world!')

# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------

#  Using of Arthematics Operator

a = int(input("Enter the first number:"))
b = int(input("Enter the Second number:"))

sum = a + b
diff = a - b
mul = a * b
div = a / b
rem = a % b

print("The sum of two number is",sum)
print("The difference of two number is",diff)
print("The product of two number is",mul)
print("The division of two number is",div)
print("The remainder of the number is",rem)

# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------

#  Using For Loop proper syntax
# Start - stop - step



days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

for i in (days):
    print(i)     #It will print all the weeks name

# Printing the number from 0 to 10
for i in  range(11):
    print(i)   #It will print the number from 0 - 10

# Printing number from 1 to 10
for i in range(1,11):
    print(i)   # It will print the number from 1 - 10

# Printing table of seven
for i in range(1,11):
    print("7 X",i,"=",7*i)


# ----Print from a to b range-----------
for i in range(10,16,1): # 10 starting point, 16 ending range, 1 increment range by 1 
    print(i)  # It will print from 10 to 15 only



# ------------BReak and CONTINUE in loop----------------------
for i in range(11):
    # if (i == 4):
    #     break   # it will print the number upto 3
    # print(i)  #Output  0, 1, 2, 3
    if (i == 4):
        continue  # it will skip the number 4 to print
    print(i)   #Output  0, 1, 2, 3, 5, 6, 7, 8, 9, 10

# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------

# Proper syntax to use while loop
# Initilization - condition - increment/decrement

# Printing number from 0 - 10 using while loop
i = 0
while i <= 10:
    print(i)
    i += 1


# Printing number from 1 to 10 using while loop

i = 1
while i <= 10:
    print(i)
    i += 1


#  Printing table of 4 using while loop

i = 1
while i <= 10:
    print("4 X ",i," = ",(4*i))
    i += 1


# ----------------------------------------------------------------------------------------

names = ["Safal", "Mohit", "Hemanta", "Biwash", "Rijan"]
marks = [87, 89, 98, 78, 77]
subject = 'Math'

i = 0
while i <= 4:
    print(names[i],"mark in",subject,"is",marks[i])
    i += 1
#  -------------------------------------------------------------


# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
