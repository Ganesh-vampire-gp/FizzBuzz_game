# check if the string has matched brackets or not
# Write a function check_brackets(s) that returns True if s has matched brackets, and False otherwise.
# For example:
# check_brackets("((()))") => True
# check_brackets("(()") => False
# check_brackets("())") => False
# check_brackets(")(") => False


def check_brackets(s):
    count =0
    for char in s:
        if char == "(":
            count+=1
        elif char == ")":
            count-=1
        if count < 0:
            return False
    return count == 0

print(check_brackets("((()))"))