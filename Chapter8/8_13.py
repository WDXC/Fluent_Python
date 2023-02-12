from HauntedBus import HauntedBus

bus1 = HauntedBus(['Alice', 'Bill'])
print(bus1.passengers)

bus1.pick('Charlie')
bus1.drop('Alice')
print(bus1.passengers)

bus2 = HauntedBus()
print(bus2.passengers)

bus2.pick('Carrie')
print(bus2.passengers)

bus3 = HauntedBus()
print(bus3.passengers)

bus3.pick('Dave')
print(bus2.passengers)
print(bus2.passengers is bus3.passengers)

print(bus1.passengers)
