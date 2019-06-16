class Stack():

    # Initialize an empty stack
    def __init__(self):
        self.items = []

    # Push a new item onto the stack
    def push(self, item):
        self.items.append(item)

    # Remove and return the last item
    # If the stack is empty, return None
    def pop(self):
        
        if not self.items:
            return None

        return self.items.pop()

    # Return the last item without removing it
    # If the stack is empty, return None
    def peek(self):
        
        if not self.items:
            return None
        return self.items[-1]
