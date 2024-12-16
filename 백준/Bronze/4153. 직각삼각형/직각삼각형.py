while True:
    lens = sorted(list(map(int, input().split())), reverse = True)
    if lens[0] == 0: break
    if lens[0]**2 == lens[1]**2 + lens[2]**2:
        print("right")
    else:
        print("wrong")
    