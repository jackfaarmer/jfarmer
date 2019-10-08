def boo_function(low, high):
    list1 = []
    for i in range(low, high + 1):
        if (i % 3 == 0) or (i % 7 == 0):
            if i % 15 == 0:
                list1.append('Boo')
                continue
            list1.append(i)
        else:
            continue

    print(list1)


if __name__ == "__main__":
    lower = int(input('Please input the lower limit:\n'))
    upper = int(input('Please input the upper limit:\n'))

    print('The list of numbers between', lower, 'and', upper, 'that are divisible by 3 or 7 is:')

    boo_function(lower, upper)