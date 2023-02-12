from copy import deepcopy

a = [10, 20]
b = [a, 30]
a.append(b)
print(a)

c = deepcopy(a)
print(c)