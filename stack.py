from node import Node


class Stack:

    def __init__(self) -> None:
        self.bottom = None
        return None

    def push(self, d) -> None:
        self.new_node = Node(d)
        self.new_node.set_next(self.bottom)
        self.bottom = self.new_node
        return None

    def pop(self) -> float:
        if self.is_empty():
            return "No Input Given"
        else:
            temp = self.bottom
            self.bottom = self.bottom.get_next()
            n = temp.get_data()
            del temp
            return n

    def is_empty(self) -> bool:
        if self.bottom is None:
            return True
        else:
            return False
