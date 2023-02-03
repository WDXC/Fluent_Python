t = (1, 2, [30, 40])
t[2] += [50, 60]
# t[2] += [50,60] throw exception
# TypeEror: 'tuple' object does not support item assignment
print(t)