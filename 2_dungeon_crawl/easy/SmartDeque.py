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
        # TODO: call popleft() and return the item we popped

    def empty(self):
        # TODO: return whether the SmartDeque is empty

    def front(self):
        # TODO Return the first item in the SmartDequeu
