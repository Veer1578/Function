def add(P, Q):
    return P + Q


def subtract(P, Q):
    return P - Q


def multiply(P, Q):
    return P * Q


def divide(P, Q):
    return P / Q


print("Select the operation")
print("a.Add")
print("b.Subtract")
print("c.Multiply")
print("d.Divide")
operation = input('Enter choice (a/b/c/d): ')

num1 = int(input('Enter a number: '))
num2 = int(input('Enter another number: '))

if operation == 'a':
    print(f'{num1} + {num2} = {add(num1, num2)}')
elif operation == 'b':
    print(f'{num1} - {num2} = {subtract(num1, num2)}')
elif operation == 'c':
    print(f'{num1} * {num2} = {multiply(num1, num2)}')
elif operation == 'd':
    print(f'{num1} / {num2} = {divide(num1, num2)}')
else:
    print('Select valid operation')
