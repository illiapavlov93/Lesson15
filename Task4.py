class IZip:
    def __init__(self, *args):
        self.args = args
        self.c = my_zip(self.args)

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.c) < 1:
            raise StopIteration
        else:
            d = self.c.pop(0)
            return d


def my_zip(args):
    out = []
    min_len = len(args[0])
    for i in args:
        if min_len > len(i):
            min_len = len(i)
    for i in range(min_len):
        item = []
        for collection in args:
            item.append(collection[i])
        out.append(tuple(item))
    return out


s = 'abcd'
t = [10, 20, 30]
f = (1, 2, 3)

obj = IZip(s, t, f)
while True:
    try:
        print(next(obj))
    except StopIteration:
        break
