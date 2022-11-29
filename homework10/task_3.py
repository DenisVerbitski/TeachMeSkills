class Counter:
    def __init__(self, start = 0, stop = None) -> None:
        self.start = start
        self.stop = stop

    def increment(self):
        while True:
            self.start += 1
            if self.start == self.stop:
                return print("Maximal value is reached")
          
    def get(self):
        print(f'meaning counter: {self.start}')

count = Counter(1,20)
count.increment()
count.get()