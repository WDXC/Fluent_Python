registery = []
def register(func):
    print('running register(%s)' % func)
    registery.append(func)
    return func

@register
def f1():
    print('running f1()')

@register
def f2():
    print('running f2()')

@register
def f3():
    print('runing f3()')

def main():
    print('running main()')
    print('registry -> ', registery)
    f1()
    f2()
    f3()

if __name__ == "__main__":
    main()