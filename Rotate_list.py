# Description: Given a list, rotate the list to the right by k places, where k is non-negative.
# Example:
# Input: [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
# Input: [1,2,3,4,5], k = 3
# Output: [3,4,5,1,2]

def rotate_list(l,k):
    if k<=0:
        return l
    k=k% len(l)
    return l[-k:] + l[:-k]
print(rotate_list([1,2,3,4,5],2))
