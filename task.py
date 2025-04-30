def square(a):
    return 4 * a


side = int(input('Enter the side of a square '))
print(f'The perimeter of that square is {square(side)}')


def rectangle(l, b):
    return 2 * (l + b)


length = int(input('Enter the length of a rectangle '))
breadth = int(input('Enter the breadth of a rectangle '))
print(f'The perimeter of that rectangle is {rectangle(length, breadth)}')


def even(a):
    if a % 2 == 0:
        print(True)
    else:
        print(False)

num = int(input('Enter number '))
check = even(num)
print(check)
