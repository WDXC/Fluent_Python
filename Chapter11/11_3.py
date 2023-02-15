class Foo:
    def __getitem__(self, item):
        return range(0, 30, 10)[item]

f = Foo()
print(f[1])

for i in f: print(i)

print(20 in f)

print(15 in f)