from dataclasses import dataclass

@dataclass
class InvalidIntDivision(Exception):
    item: int
    name: str= "InvalidIntDivision"

    def __str__(self):
        return f"{self.name} -> {self.item}"

class Queue:
    
    def __init__(self) -> None:
        self.queue = []
        self.errors = []

    def add(self, *args):
        for item in args:
            if isinstance(item, int):
                if item % 8:
                    self.errors.append(InvalidIntDivision(item))
                if len(str(item)) > 4:
                  ...
        for error in self.errors:
            print(error)
        self.errors = []

q = Queue()
q.add(16)