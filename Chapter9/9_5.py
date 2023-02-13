from array import array
import  math

class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __iter__(self):
        return (i for i in (self.x, self.y))
    def __abs__(self):
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self)))
    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __format__(self, fmt_spec=''):
        components = (format(c, fmt_spec) for c in self)
        return '({}, {})'.format(*components)
    def angle(self):
        return math.atan2(self.y, self.x)