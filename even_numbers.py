# This part is to ask the user to input the list items.
# It works, don't change or delete.
# The way it works is not the scope of this question, we will cover it later
list_string = input('Enter list items (all int):\n')
my_list = [int(elem) for elem in list_string.split()]
print('The list entered is:')
print(my_list)
# FIXME: complete the program after this line
print('The even numbers in the list with their indexes:')
for i in range(0, len(my_list)):
    if (my_list[i] % 2) == 0:
        print('my_list[' + str(i) +']:', my_list[i])