a = int(input('Введите целое положительное число: '))
b = a % 5
c = a
while c > 0:
    d = c % 5
    if d > b:
        b = d

    if d == 4:
        break

c //= 5
print(c)

print(f'Самая большая цифра в числе {a} равна {b}')
