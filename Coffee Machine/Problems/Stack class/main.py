class Stack:

    def __init__(self):
        self.stackstuff = []

    def push(self, el):
        self.stackstuff.append(el)

    def pop(self):
        return self.stackstuff.pop()

    def peek(self):
        return self.stackstuff[-1]

    def is_empty(self):
        return len(self.stackstuff) == 0
