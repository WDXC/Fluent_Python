from inspect import getgeneratorstate

from coro_exc_demo import demo_exc_handling, DemoException

exc_coro = demo_exc_handling()

print(next(exc_coro))

print(exc_coro.send(11))

print(exc_coro.throw(DemoException))

print(getgeneratorstate(exc_coro))