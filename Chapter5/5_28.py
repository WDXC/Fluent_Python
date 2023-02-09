from tag import tag
print(tag)

from functools import partial
picture = partial(tag, 'img', cls='pic-frame')
print(picture(src='wumpus.jpeg'))

print(picture)

print(picture.func)

print(picture.args)

print(picture.keywords)