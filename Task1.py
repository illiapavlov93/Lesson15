class Range:
    def __init__(self, stop, start=0, step=1):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.stop:
            raise StopIteration
        else:
            self.start += self.step
            if self.start > self.stop + 1:
                raise StopIteration
            return self.start - 1


for c in Range(10, start=2, step=3):
    print(c)



