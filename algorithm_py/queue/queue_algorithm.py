class queue_cmd:
    def __init__(self,n):
        self.q_list = [None for _ in range(n)]
        self.head = 0
        self.rear = 0

    def push(self,x):
        self.q_list[self.rear] = x
        self.rear += 1

    def pop(self):
        if self.size() > 0:
            self.head += 1
            return self.q_list[self.head-1]
        else:
            self.head = 0
            self.rear = 0
            return -1

    def size(self):
        return self.rear - self.head

    def empty(self):
        if self.size() > 0:
            return 0
        return 1

    def front(self):
        if self.size() > 0:
            return self.q_list[self.head]
        return -1

    def back(self):
        if self.size() > 0:
            return self.q_list[self.rear-1]
        return -1

def run_queue_cmd(command, queue_list):
    cmd = command[0]
    if cmd == 'push':
        x = int(command[1])
        queue_list.push(x)
    elif cmd == 'pop':
        print(queue_list.pop())
    elif cmd == 'size':
        print(queue_list.size())
    elif cmd == 'empty':
        print(queue_list.empty())
    elif cmd == 'front':
        print(queue_list.front())
    elif cmd == 'back':
        print(queue_list.back())

    return queue_list

n = int(input())
queue_list = queue_cmd(n)

for _ in range(n):
    command = input().split(' ')
    queue_list = run_queue_cmd(command, queue_list)