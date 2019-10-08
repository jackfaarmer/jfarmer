def create_list():
    n = []
    i = 0
    while i >= 0:
        if len(n) == 0:
            inp = int(input('Input numbers or -1 to stop:\n'))
            n.append(inp)
            i = 0
        else:
            inp = int(input('Input another numbers or -1 to stop:\n'))
            if inp >= 0 or inp <= -2:
                n.append(inp)
            elif inp == -1:
                i = -1
    print('The list entered is:', n)
    return n


def count_odd(list):
    c = 0
    for i in list:
        if i % 2 != 0:
            c += 1
    print('Number of odd numbers:', c)
    return c


def count_even(list):
    c = 0
    for i in list:
        if i % 2 == 0:
            c += 1
    print('Number of even numbers: 3')
    return c


print('This program will count the number of odd and even numbers in a list')
list1 = create_list()
count_odd(list1)
count_even(list1)
