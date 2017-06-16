__author__ = 'Grzegorz'


class A:
    def __init__(self):
        self.a = 1
        self.b = 2

a = A()
b = A()

print(a.a)
print(b.b)

c = set([a,b])
print(c)

print("a in c:", a in c)


if __name__ == "__main__":
    print("Hellooo from main")

