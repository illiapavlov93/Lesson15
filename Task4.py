class IZip:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.c = zip(self.a, self.b)

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.c) < 1:
            raise StopIteration
        else:
            d = self.c.pop(0)
            return d


def zip(a, b):
    out = []
    min_len = len(a)
    if min_len > len(b):
        min_len = len(b)
    for i in range(min_len):
        item1 = a[i]
        item2 = b[i]
        out.append((item1, item2))
    return out

s = 'abcd'
t = [10, 20, 30]

obj = IZip(s, t)
while True:
    try:
        print(next(obj))
    except StopIteration:
        break
