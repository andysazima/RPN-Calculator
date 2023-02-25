class Node:

    def __init__(self, d) -> float:
        self.data = d
        return None

    def set_next(self, n) -> float:
        self.next = n
        return None

    def get_data(self) -> float:
        return self.data

    def get_next(self) -> float:
        return self.next
