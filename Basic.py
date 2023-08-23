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


#    Using Array Index


a = "aufwiedersehen"

print(a[1])      # output = u
print(a[0:8])    # output = aufwiede --- the value in index 8 no will not print it will print upto index 7
print(a[1:8:2])  # output = uwee  

#  Start : stop : steps

print(a[-1])     # output = n ---- It will print the last value i.e n 
print(a[::-1])   # output = nehesredeiwfua
''' It will print all the number from last as we have kept empty in start and stop which works as a default
and -1 in steps part which will print the values from last''' 


# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------


# LIST WORKS AS ARRAY IN PYTHON SO LIST START FROM HERE

marks = [50, 20, 30, 49, 78, 57, 92, 47, 88, 91]
names = ["Safal", "AAA", "BBB", "CCC", "DDD", "EEE", "FFF", "GGG", "HHH", "III"]

print(marks)
print(names)
print(marks[-1])

i = 0
while i <= 9:
    print("The marks of",names[i],"in math is",marks[i])
    i += 1

# ------TO ADD NUMBERS IN ARRAY
marks.append(77)     #IT WILL ADD 77 AT LAST
print(marks)

# ------TO CHANge the value inside array
marks[4] = 88  #If i change the value of index[4] i.e 78 to 88 this is the syntax
print(marks)

# ------To clear all values
marks.clear()
print(marks)

# -------TO Insert inside in middle
# ----IF i want to put 35 after 20 and before 30 this is the syntax
marks.insert(2, 35)  
print(marks)

# --------To REmove any number from array
# ------If i want to remove 92 from array then
marks.remove(92)
print(marks)

# -----Next process to remove the number using pop
#   bUt for this you have to write index number instead of values
marks.pop(3)   #it will remove 49 value
print(marks)

# -----To arrange in ascending order
marks.sort()
print(marks)

#-----------------------LIST END HERE--------------------------------


'''                   LIST                       |     TUPLE                       |    SETS
(a)= value can be changed and can be assigned    | both is not possible            | both is not possible
     or add easily
(b)= can display any index number                | can display any index number    | cannot display this also
(c)= denoted by BIG BRACKETS "[]"                | SMALL BRACKETS "()"             | CURLY BRACKETS {}
'''

# --------------------------------------------------------------------------------
numbers = [22, 43, 65, 76, 43, 77, 90, 65, 32, 54, 66, 75, 65]

numbers.append(99)  #To add any number in list
numbers.clear()  # To clear all the list's data/ numbers
numbers.remove(75) # To remove any number for example 75 from the list 
numbers.pop(5)   # It remove 77 from the list but we have to write index number
numbers.insert(5,98) # It put the value 98 in index 5 i.e after 43
numbers.sort()    # It will helps to arrange the number in ascending order
numbers[6] = 00    # It will change the value of index 6 i.e 90 to 0
print(numbers)
# -----------------------------------------------------------------

# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------



# Tuple use small bracket() while list(Array) use big brackets[]


tp = (12, 34, 56, 78, 86, 84, 3)
print(tp)     # output = will display all number
print(tp[0])    # output = 12 
print(tp[0:4])   #output = 12, 34, 56, 78

# IN TUPLE WE CANNOT ASSIGNED OR CHANGE THE NUMBER INSIDE THE BRACKETS FOR EXAMPLE
tp[3] = 99  #Output = error 

# Here tuple is used while if the value is constant and will not be change and listed is used to change 
# the value later also



'''                   LIST                       |     TUPLE                       |    SETS
(a)= value can be changed and can be assigned    | both is not possible            | both is not possible
     or add easily
(b)= can display any index number                | can display any index number    | cannot display this also
(c)= denoted by BIG BRACKETS "[]"                | SMALL BRACKETS "()"             | CURLY BRACKETS {}
'''

# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
