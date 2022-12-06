from dataclasses import dataclass

@dataclass
class DataObject:
    data: any

data_1 = DataObject(10)
data_2 = DataObject(12)

class Deque:
    deque = [1,2]

    @classmethod
    def append_left(cls, value: any):
        if len(cls.deque) < 5:
            if isinstance(value, DataObject):
                cls.deque.insert(0, value.data)
                return cls.deque
        else:
            print('Очередь переполнена')
        return cls.deque
    @classmethod
    def append_right(cls, value: any):
        if len(cls.deque) < 5:
            if isinstance(value, DataObject):
                cls.deque.append(value.data)
                return cls.deque
        else:
            print('Очередь переполнена')
        return cls.deque
    
    @classmethod
    def pop_left(cls):
        return cls.deque.pop(0), cls.deque

    @classmethod
    def pop_right(cls):
        return cls.deque.pop(-1), cls.deque

element = Deque()

element.append_left(data_1)
element.append_right(data_2)
print(element.append_left(data_1))
print(element.pop_left())
print(element.pop_right())

