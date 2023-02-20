class DemoException(Exception):
    '''为这次演示定义的异常类型'''


def demo_exc_handling():
    print('-> coroutine started')
    while 1:
        try:
            x = yield
        except DemoException:
            print('*** DemoException handled.Continuing...')
        else:  # 如果没有异常name显示接受到的值
            print('-> coroutine received:{!r}'.format(x))
    raise RuntimeError('This line should never run')


if __name__ == '__main__':
    from inspect import getgeneratorstate

    ge = demo_exc_handling()
    print(getgeneratorstate(ge))
    next(ge)
    print(getgeneratorstate(ge))
    ge.send(10)
    ge.send(20)
    ge.throw(DemoException)
    print(getgeneratorstate(ge))
    print(ge.throw(DemoException))
    ge.send(100)
    # ge.throw(ZeroDivisionError)
    ge.close()
    print(getgeneratorstate(ge))