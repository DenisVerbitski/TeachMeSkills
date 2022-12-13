class EvenRange:

    def __init__(self, start: int, stop: int):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self
       
    def __next__(self):
        if self.start < self.stop:
            if self.start % 2 == 0:
                self.start += 2
            else:
                self.start += 1
            result = self.start
            return result
        else:
            print("Error")
            raise StopIteration

er1 = EvenRange(2, 20)

print(next(er1))
print(next(er1))
print(next(er1))
print(next(er1))
print(next(er1))
print(next(er1))
print(next(er1))
print(next(er1))
print(next(er1))
print(next(er1))

