import weakref

from Cheese import Cheese

stock = weakref.WeakValueDictionary()
catalog = [Cheese('Red Leicester'), Cheese('Tilist'),
           Cheese('Brie'), Cheese('Parmesan')]

for cheese in catalog:
    stock[cheese.kind] = cheese

print(sorted(stock.keys()))

del catalog
print(sorted(stock.keys()))

del cheese
print(sorted(stock.keys()))