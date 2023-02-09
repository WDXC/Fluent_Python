from tag import tag

print(tag('br'))

print(tag('p', 'hello'))

print(tag('p', 'hello', 'world'))

print(tag('p', 'hello', id=33))

print(tag('p', 'hello', 'world', cls='sidebar'))

print(tag(content='testing', name='img'))

my_tag = {'name':'img', 'title':'Subset Boulevard', 'src':'sunset.jpg', 'cls':'framed'}

print(tag(**my_tag))
