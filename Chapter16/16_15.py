from coroaverager2 import averager

coro_avg = averager()
next(coro_avg)
coro_avg.send(10)
coro_avg.send(30)
coro_avg.send(6.5)

try:
    coro_avg.send(None)
except StopIteration as exc:
    result = exc.value

print(result)
