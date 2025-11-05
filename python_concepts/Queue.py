class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        return self.items.append(item)

    def dequeue(self):
        if len(self.items) < 1:
            return None
        return self.items.pop(0) 

    def display(self):
        print(self.items)

    def size(self):
        return len(self.items)

queue = Queue()
print(queue.isEmpty())

for i in range(0, 5):
    queue.enqueue(i)

queue.display()
queue.dequeue()
print("FIFO: ")
queue.display()

#Queue made with list
queue_list = []
queue_list.append(1)
queue_list.append(2)
queue_list.append(3)
print("Full queue: ", queue_list)
print(queue_list.pop(0))
print(queue_list.pop(0))
print(queue_list.pop(0))
print("Empty queue: ", queue_list)