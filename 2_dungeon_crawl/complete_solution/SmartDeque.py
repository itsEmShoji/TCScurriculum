from collections import deque

class SmartDeque:
    def __init__(self, mode_in):
        self.mode = mode_in
        self.data = deque()

    def push(self, elt):
        if(self.mode == "s"):
            self.data.appendleft(elt)
        else:
            self.data.append(elt)

    def pop(self):
        return self.data.popleft()

    def empty(self):
        return len(self.data) == 0

    def front(self):
        return self.data[0]
