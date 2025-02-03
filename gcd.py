#gcd.py
#A program that computes the greatest common divisor of two numbers.
#The greatest common divisor of two positive integers is the largest integer that divides each of them without remainder.
#For example, gcd(2, 12) is 2.
#The function gcd(m, n) is defined recursively as follows:
#If n is 0, then the answer is m.
#Otherwise, the answer is the same as the answer of gcd(n, m % n).
#Write a function gcd(m, n) that returns the greatest common divisor of m and n.
#For example:
#gcd(2, 12) => 2
#gcd(3, 7) => 1
#gcd(18, 27) => 9
#Hint: You can use the modulo operator % to compute the remainder of a division.
#For example, 14 % 3 is 2.
#You can also use the modulo operator to compute the remainder of a division of two numbers.
#For example, 14 % 3 is 2.


def gcd(m,n):
    fm=[]
    for i in range(1,m+1):
        if (m%i)==0:
            fm.append(i)

    fn=[]
    for i in range(1,n+1):
        if (n%i)==0:
            fn.append(i)

    cf=[]
    for f in fm:
        if f in fn:
            cf.append(f)
    return(cf[-1])