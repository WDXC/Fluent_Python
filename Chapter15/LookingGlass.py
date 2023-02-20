from mirror import LookingGlass

with LookingGlass() as what:
    print('Alice, Kitty and SnowDrop')
    print(what)

print(what)

print('Back to normal')