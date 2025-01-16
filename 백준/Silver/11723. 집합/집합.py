import sys
M = int(input())

S = set()
for _ in range(M):
    command = sys.stdin.readline().strip()
    if " " in command:
        do, n = command.split()
        n = int(n)
    else:
        do = command
    
    if do == "add":
        S.add(n)
    elif do == "remove":
        try: 
            S.remove(n)
        except: 
            pass
    elif do == "check":
        print(1 if n in S else 0)
    elif do == "toggle":
        try: 
            S.remove(n)
        except: 
            S.add(n)
    elif do == "all":
        S = set(range(1, 21))
    elif do == "empty":
        S = set()