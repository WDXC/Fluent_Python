from vector2d import Vector2d

v1 = Vector2d(3, 4)
print(v1.x, v1.y)
x,y = v1
print(x, y)

print(v1)

v1_clone = eval(repr(v1))
print(v1_clone)

print(v1)

octets = bytes(v1)
print(octets)
print(abs(v1))

print(bool(v1), bool(Vector2d(0, 0)))