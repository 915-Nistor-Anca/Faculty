class Data():
    def __init__(self, v, c):
        self.vertex = v
        self.cost = c

class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0

    # for inserting an element in the queue
    def insert(self, data):
        self.queue.append(data)

    # for popping an element based on Priority
    def delete(self):
        min = 0
        for i in range(len(self.queue)):
            if self.queue[i].cost < self.queue[min].cost:
                min = i
        item = self.queue[min]
        del self.queue[min]
        return item.vertex
