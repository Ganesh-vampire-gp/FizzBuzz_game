# n=int(input())
# t=tuple(map(int,input().split()))
# result=hash(t)
# print(result)

# def custom_hash(t):
#     # Custom hash function to ensure consistent output
#     return sum(t) * 31 + len(t)

# # Read the integer n
# n = int(input())

# # Read the space-separated integers and create a tuple
# t = tuple(map(int, input().split()))

# # Compute the custom hash of the tuple
# result = custom_hash(t)

# # Print the result
# print(result)

n = int(input())

# Read the space-separated integers and create a tuple
t = tuple(map(int, input().split()))

# Compute the hash of the tuple
result = hash(t)

# Print the result
print(result)