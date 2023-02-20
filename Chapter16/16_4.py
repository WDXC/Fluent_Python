from average import average

coro_avg = average()
next(coro_avg)

print(coro_avg.send(10))

print(coro_avg.send(30))

print(coro_avg.send(5))
