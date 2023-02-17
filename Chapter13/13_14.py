from Chapter_11.vector2d_v3 import Vector2d
from Vector_v8 import Vector


va = Vector([1.0, 2.0, 3.0])
vb = Vector(range(1, 4))
print(va == vb)

vc = Vector([1, 2])

v2d = Vector2d(1, 2)
print(vc == v2d)

t3 = (1, 2, 3)

print(va == t3)