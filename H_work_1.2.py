time = input('Введите время в секундах: ')
time = int(time)
hr = time // 3600
min = time // 60 - hr * 60
sec = time % 60
print(f'{hr:02}:{min:02}:{sec:02}')

