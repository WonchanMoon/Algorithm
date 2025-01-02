from collections import Counter

N = int(input())
cards = Counter(list(map(int, input().split())))
M = int(input())
query = list(map(int, input().split()))

for q in query:
    try:
        print(cards[q], end = ' ')
    except:
        print(0, end = ' ')