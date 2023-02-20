from mirror_gen import looking_glass

with looking_glass() as what:
    print('Alice, Kitty and Snowdrop')
    print(what)

print(what)