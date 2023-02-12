charles = {'name': 'Charles L. Dodgson', 'born':1832}
lewise = charles
print(lewise is charles)

print(id(charles) , id(lewise))

lewise['balance'] = 950
print(charles)
