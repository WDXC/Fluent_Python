from inspect import getgeneratorstate

from coro_exc_demo import demo_exc_handling

exc_coro = demo_exc_handling()
print(next(exc_coro))

print(exc_coro.send(11))

print(exc_coro.throw(ZeroDivisionError))

print(getgeneratorstate(exc_coro))
