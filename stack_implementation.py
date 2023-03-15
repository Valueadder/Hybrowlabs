# Implementing stack data structure in Python.
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    # Initializing a stack
    def __init__(self):
        self.head = Node("head")
        self.size = 0

    # Checking if the stack is empty
    def isEmpty(self):
        return self.size == 0

    def peek(self):
        if self.isEmpty():
            raise Exception("Peekingfrom an empty stack")
        return self.head.next.value

    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value


if __name__ == "__main__":
    stack = Stack()
    # push opeation
    for i in range(1, 11):
        stack.push(i)
    print(f"Stack:{stack}")
    # pop opeation
    for j in range(1, 6):
        remove = stack.pop()
        print(f"Pop: {remove}")
    print(f"Stack:{stack}")
