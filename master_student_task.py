master = input("student: ")
a2 = master.replace('(', ' ').replace(')', ' ').split()
print(a2)


def number(num):
    if num == 'zero':
        return 0
    elif num == 'one':
        return 1
    elif num == 'two':
        return 2
    elif num == 'three':
        return 3
    elif num == 'four':
        return 4
    elif num == 'five':
        return 5
    elif num == 'six':
        return 6
    elif num == 'seven':
        return 7
    elif num == 'eight':
        return 8
    elif num == 'nine':
        return 9


def calculation(num, a, b):
    if num == 'times':
        return int(a*b)
    elif num == 'plus':
        return int(a+b)
    elif num == 'minus':
        return int(a-b)
    elif num == 'divided_by':
        return int(a//b)


cal = calculation(a2[1], number(a2[0]), number(a2[2]))

print(cal)
