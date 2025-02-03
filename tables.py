# tables
# Write a program that takes a number as input and prints its multiplication table up to 10.
#
# Example

value = input("Enter a number:")
value = int(value)
for i in range(11):
    print(value,"x",i,"=",value*i)