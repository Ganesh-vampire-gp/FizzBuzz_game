# s = 'Chennai'
# print(s)
# print(type(s))

# a="gugulothu ganesh"
# print(a)
# print(type(a))

# b=2
# c =2.5

# print(type(b))

# add two numbers

# x=13
# y=12

# print("sum of two numbers is = ",x+y)

#num=int(input("enter your number:"))

#remainder=num%2
# print(remainder)
#print(type(num))

# a=34
# b=80
# if(a>b):
#     print("a is greater than b")
# else:
#     print("b is greater than a")

# num = int(input("Enter the number:"))
# num1=int(input("enter the number:"))

# num2 = num+num1


# print(num2/2)
# name="aaahhhahahe"
# p=name[1:6:2]
# print(p,len(name))
# print(name.endswith("ah"))
# print(name.count("a"))
# print(name.capitalize())
# print(name.find("e"))
# print(name.replace("a","f"))

# name=input("enter your name:")

# print(name,"Good afternoon sir!!..")

# letter = '''Dear Ganesh,
# You are selected!
# 30/01/2025'''
# print(letter)

# text="gani  is legend"

# if "  " in text:
#     print("yes")
# else:
#     print("NO")

# n=32
# a=[]

# for i in range(n):
#     l1=[]
#     p=0
#     for j in range(i):
#         l1.append(j)
#     for k in l1:
#      p+=1
#     a.append(p)
# k=0
# for l in a:
#    k+=l
# print(k)

# n=256
# k=0
# a=[]
# b=0
# while(n!=0):
#     k=k+(n%10)
#     a.append(n%10)
#     n=n
# a.sort()
# for i in a:
#     b=b+i
# if(b!=k):
#     print("Python is fun")
# else:
#     print("python is boring")

# second largest number in a list if it has repitetive numbers

# values=input("enter the numbers:")
# list=values.split(" ")
# list1=[]
# for i in list:
#     list1.append(int(i))
#     list1.sort()
# for k in list1:
#     for j in list1:
#         if(i<j):
#             min=i
# print(min)
# #print("second largest number is:",list1[1-len(list1)])

# def find_second_smallest(numbers):
#     unique_numbers = list(set(numbers))
    
#     if len(unique_numbers) < 2:
#         return None

#     unique_numbers.sort()
#     return unique_numbers[1]

# def main():
    
#     user_input = input("Enter a list of numbers separated by spaces: ")
#     number_list = list(map(int, user_input.split()))
    
#     second_smallest = find_second_smallest(number_list)
    
#     if second_smallest is None:
#         print("There is no second smallest number.")
#     else:
#         print("The second smallest number is:", second_smallest)

# if __name__ == "__main__":
#     main()

# remove even duplicate for the list

# def remove_even_duplicates(numbers):
#     result = []
#     seen = set()
#     for num in numbers:
#         if num % 2 == 0:
#             if num not in seen:
#                 result.append(num)
#                 seen.add(num)
#         else:
#             result.append(num)
#     return result

# # Example usage
# numbers = [3,1,4,1,5,9,2,6,5,3,5,2,2]
# print("Original list:", numbers)
# print("List after removing even duplicates:", remove_even_duplicates(numbers))


# x = ['super',397,'king',43]
# y = x[2:]
# u = x
# w = y
# w = w[0:]
# w[1] = 357
# x[3:4] = [723]

# first = "pterodactyl"
# second = ""
# for i in range(len(first)-1,-1,-2):
#   second = first[i]+second
# print(second)

# def mystery(l):
#   l[1:3] = l[4:6]
#   return()

# list1 = [34,69,12,78,23,91,42]
# mystery(list1)
# print(list1)

#second lowest grade of the students

# 
#dictionary contain student name and marks find average of the marks

