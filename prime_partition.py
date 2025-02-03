# check a integer is prime partition or not
# A prime partition of a positive integer n is a set of one or more prime numbers that add up to n.
# For example, there are four prime partitions of 11:
# 11
# 2 + 2 + 7
# 2 + 3 + 3 + 3
# 3 + 5 + 3
# Write a function prime_partition(n) that returns True if n has a prime partition, and False otherwise.
# For example:
# prime_partition(11) => True
# prime_partition(7) => False
# prime_partition(8) => True
# prime_partition(9) => False


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def prime_partition(n):
    for i in range(2, int(n**0.5)+1):
        if is_prime(i) and is_prime(n-i):
            return True
    return False

print(prime_partition(3234))