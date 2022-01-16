year, month, day, hour, minute, second = input().split()
print(year, month, day, hour, minute, second, sep=' ')
print(year, month, day, sep='-', end='T')
print(hour, minute, second, sep=':')
