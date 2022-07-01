# 큐 2
"""
정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 여섯 가지이다.

push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
"""
import sys

class Queue2:
    def __init__(self):
        self.queue = []
        self.cnt = 0

    def push(self, num):
        self.queue.append(num)
        self.cnt += 1
        print(self.queue, self.cnt)
        
    def pop(self):
        if self.cnt ==0 :
            print(-1)
            return
        self.cnt -=1
        print(self.queue.pop(-1))

    def size(self):
        print(self.cnt)

    def empty(self):
        if self.cnt ==0:
            print(1)
            return
        print(0)

    def front(self):
        if self.cnt == 0 :
            print(-1)
            return
        print(self.queue[0])

    def back(self):
        if self.cnt ==0 :
            print(-1)
            return
        print(self.queue[-1])

queue = Queue2()
cnt = int(sys.stdin.readline())

for i in range(cnt):
    str = sys.stdin.readline().strip().split()
    if len(str) == 2:
        queue.push(int(str[1]))
        continue
    getattr(queue, str[0])()
