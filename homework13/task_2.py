class MySquareIterator:

    def __init__(self, collection) -> None:
        self.collection = collection
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            item = self.collection[self.index]
        except IndexError: 
            raise StopIteration
        self.index += 1
        return item ** 2


lst = [1, 2, 3, 4, 5]
itr = MySquareIterator(lst)

for element in itr:
    print(element)

