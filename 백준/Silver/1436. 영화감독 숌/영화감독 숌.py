from collections import deque

N = int(input())


candis = [str(i) for i in range(10)]

queue = deque()
queue.append("666")
total = set()
while queue:
    now = queue.popleft()
    if len(now) == 7:
        break
    for candi in candis:
        queue.append(candi+str(now))
        total.add(int(candi+str(now)))
        queue.append(str(now)+candi)
        total.add(int(str(now)+candi))
        
print(sorted(list(total))[N-1])