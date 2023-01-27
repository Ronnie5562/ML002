def sum(x, y):
    return x + y

def test_sum():
    assert sum(1, 3) == 4

x = [1, 2, 3, 4, 5, 6, 7]

y = [n*n for n in x]

print(y)


a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
c = int(input('Enter the Third number: '))

min = a if a < b and a < c else b if b < c else c
max = a if a > b and a > c else b if b > c else c

print(f'min: {min}')
print(f'max: {max}') 