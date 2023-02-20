from coroaverager1 import average

coro_avg = average()
print(coro_avg.send(40))

print(coro_avg.send(50))

print(coro_avg.send('spam'))

print(coro_avg.send(60))
