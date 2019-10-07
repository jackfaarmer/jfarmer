# FIXME 3-a: Complete draw_right_triangle function.
def draw_right_triangle(symbol, height):

    for i in range(0, height + 1):
        print(str(symbol) * i)


if __name__ == "__main__":
    # FIXME 1: Print what the program is going to do.
    print('This program will draw a right triangle')

    # FIXME 2: Prompt the user to enter a char and height.
    triangle_char = input('Enter a character:\n')
    triangle_height = int(input('Enter triangle height:\n',))

    # FIXME 3-b: Then, call the function draw_right_triangle
    print(end="")
    draw_right_triangle(triangle_char, triangle_height)
