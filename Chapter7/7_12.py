from make_averager import make_average

avg = make_average()
print(avg.__code__.co_freevars)
print(avg.__closure__)

print(avg(10))
print(avg(11))
print(avg(12))
print(avg.__closure__[0].cell_contents)