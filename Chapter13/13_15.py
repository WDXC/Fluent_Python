from Chapter_13.Vector_v8 import Vector

v1 = Vector([1,2,3])
v1_alias = v1
print(id(v1))

v1 += Vector([4, 5, 6])
print(v1)

print(id(v1))

print(v1_alias)

v1 *= 11
print(v1)

print(id(v1))