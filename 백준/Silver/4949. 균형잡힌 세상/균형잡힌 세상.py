from collections import deque

start = ['[', '(']
end = [']', ')']

while True:
    S = input()
    if S == '.':
        break
    balanced = True
    queue = deque()
    for s in S:
        if s in start:
            queue.append(s)
        elif s in end:
            try:
                now = queue[-1]
                if (now == '[' and s == ']') or (now == '(' and s == ')'):
                    queue.pop()
                else: 
                    raise
            except:
                balanced = False
                break
                
    if (not queue) and balanced:
            print('yes')
    else:
        print('no')
        balanced = True