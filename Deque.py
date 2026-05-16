class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def add_front(self, item):
        self.items.append(item)

    def remove_front(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Deque is empty")

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_rear(self):
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError("Deque is empty")

    def size(self):
        return len(self.items)