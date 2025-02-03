#second lowest grade of the students
# print the name of the students with the second lowest grade
# if there are multiple students with the second lowest grade, print them in alphabetical order
# Example:

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
    students = []
    students.append([name, score])
    students.sort(key=lambda x: x[1])
    second_lowest = sorted(set([x[1] for x in students]))[1]
    result = sorted([x[0] for x in students if x[1] == second_lowest])
    print('\n'.join(result))


