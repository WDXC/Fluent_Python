class MySeq:
    def __getitem__(self, item):
        return item


s = MySeq()
print(s[1])

print(s[1:4])

print(s[1:3:2])
print(s[1:3:2, 9])
print(s[1:4:2, 7:9])