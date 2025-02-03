#applying list operations
# Description: Perform the following commands:
# insert i e: Insert integer e at position i.
# print: Print the list.
# remove e: Delete the first occurrence of integer e.
# append e: Insert integer e at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Input:
# The first line contains an integer, n, denoting the number of commands.
# Each line i of the n subsequent lines contains one of the commands described above.
# Output:
# For each command of type print, print the list on a new line.
# Sample Input:

list = []
n = int(input())

for _ in range(n):
    command = input().split()
    cmd = command[0]
    
    if cmd == "insert":
        index = int(command[1])
        element = int(command[2])
        list.insert(index, element)
    elif cmd == "print":
        print(list)
    elif cmd == "remove":
        element = int(command[1])
        list.remove(element)
    elif cmd == "append":
        element = int(command[1])
        list.append(element)
    elif cmd == "sort":
        list.sort()
    elif cmd == "pop":
        list.pop()
    elif cmd == "reverse":
        list.reverse()