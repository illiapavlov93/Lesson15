class Reverse:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.data) < 1:
            raise StopIteration
        else:
            a = self.data.pop(-1)
            return a


list1 = ['a', 1, 2, 3, 'c', 17]
it = Reverse(list1)
# for i in range(len(list1)):
#     print(next(it))

while True:
    try:
        print(next(it))
    except StopIteration:
        break
