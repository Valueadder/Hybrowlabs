class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# The queue front stores the front node of Linked list and rear stores the last node of linked list


class Queue:
    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        return self.front == None

# add element to the queue

    def EnQueue(self, item):
        temp = Node(item)
        if (self.rear == None):
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

#  remove element to the queue

    def DeQueue(self):
        if self.isEmpty():
            return
        temp = self.front
        self.front = temp.next
        if (self.front == None):
            self.rear = None


# Diver code implementation
q = Queue()
q.EnQueue(10)
q.EnQueue(20)
q.DeQueue()
q.DeQueue()
q.EnQueue(30)
q.EnQueue(40)
q.EnQueue(50)
print(f"Queue Front: {q.front.value}")
print(f"Queue Back: {q.rear.value}")
