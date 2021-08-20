class stack_cmd:
    def __init__(self,n):
        self.s_list = [None for _ in range(n)]
        self.count = -1

    def push(self,x):
       self.count += 1
       self.s_list[self.count] = x

    def pop(self):
        if self.size() > 0:
            pop_x = self.s_list[self.count]
            self.count -= 1
            return pop_x
        else:
            return -1

    def size(self):
        return self.count + 1

    def empty(self):
        if self.size() > 0:
            return 0
        return 1

    def top(self):
        if self.size() > 0:
            return self.s_list[self.count]
        return -1

def run_stack_cmd(command, stack_list):
    cmd = command[0]
    if cmd == 'push':
        x = int(command[1])
        stack_list.push(x)
    elif cmd == 'pop':
        print(stack_list.pop())
    elif cmd == 'size':
        print(stack_list.size())
    elif cmd == 'empty':
        print(stack_list.empty())
    elif cmd == 'top':
        print(stack_list.top())

    return queue_list

n = int(input())
queue_list = stack_cmd(n)

for _ in range(n):
    command = input().split(' ')
    queue_list = run_stack_cmd(command, queue_list)