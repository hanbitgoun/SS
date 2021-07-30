class Circular_queue():
    def __init__(self, n):
        self.cq = [None for _ in range(n)]
        self.n = n
        self.head = 0
        self.rear = 0
    
    def push(self, x):
        if self.is_full():
            return -1
        self.rear = (self.rear+1) % self.n
        self.cq[self.rear] = x

    def pop(self):
        if self.is_empty():
            return -1
        self.head = (self.head+1) % self.n
        return self.cq[self.head]

    def empty(self):
        if self.is_empty():
            return 1
        return 0

    def size(self):
        return self.rear - self.head

    def front(self):
        if self.is_empty():
            return -1
        return self.cq[self.head+1]

    def back(self):
        if self.is_empty():
            return -1
        return self.cq[self.rear]

    def is_empty(self):
        return self.head == self.rear

    def is_full(self):
        return (self.rear+1) % self.n == self.head

    

def run_circular_queue(command, cq):
    cmd = command[0]
    
    if cmd=='push':
        _, x = command
        cq.push(int(x))
    elif cmd=='pop':
        print(cq.pop())
    elif cmd=='size':
        print(cq.size())
    elif cmd=='empty':
        print(cq.empty())
    elif cmd=='front':
        print(cq.front())
    elif cmd=='back':
        print(cq.back())

    return cq

n = int(input())
cq_list = Circular_queue(n)

for _ in range(n):
    cmd = input().split()
    cq_list = run_circular_queue(cmd, cq_list)