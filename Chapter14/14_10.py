from decimal import Decimal
from fractions import Fraction

from ArithmeticProgression import ArithmeticProgression

ap = ArithmeticProgression(0, 1, 3)
print(list(ap))

ap = ArithmeticProgression(1, .5, 3)
print(list(ap))

ap = ArithmeticProgression(0, 1/3, 1)
print(list(ap))

ap = ArithmeticProgression(0, Fraction(1, 3), 1)
print(list(ap))

ap = ArithmeticProgression(0, Decimal('.1'), .3)
print(list(ap))
