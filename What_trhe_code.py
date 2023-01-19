class Foo:
    def __init__(self, x):
        self.x = x

a = Foo(1)
print(a)
b = Foo(1)
print(b)

d = {a:1}
print(d)
d[b] = 2

print(d[Foo(1)])