from mirror import LookingGlass

manager = LookingGlass()
print(manager)

monster = manager.__enter__()
print(monster == 'JABBERWOCKY')


print(monster)

print(manager)

manager.__exit__(None, None, None)

print(monster)