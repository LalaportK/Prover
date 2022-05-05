from .PropositionalLogicBase import PropositionalLogicBase


class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item: PropositionalLogicBase):
        self.stack.append(item)
    
    def pop(self) -> PropositionalLogicBase:
        res = self.stack[-1]
        del self.stack[-1]
        return res