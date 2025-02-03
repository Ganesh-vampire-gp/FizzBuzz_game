#FizzBuzz Game
#Prints Fizz if the number is divisible by 3
#Prints Buzz if the number is divisible by 5
#Prints FizzBuzz if the number is divisible by both 3 and 5
#Prints the number if the number is not divisible by 3 or 5

n =input("Enter your number:")
n = int(n)
for  i in range(1,n+1):
    if(i%3==0 and i%5==0):
        print("FizzBuzz")
    else:
        if(i%3==0):
            print("Fizz")
        else:
            if(i%5==0):
                print("Buzz")
            else:
                print(str(i))