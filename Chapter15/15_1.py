with open('mirror.py') as fp:
    src = fp.read(60)

print(len(src))

print(fp)

print(fp.closed, fp.encoding)

print(fp.read(60))

