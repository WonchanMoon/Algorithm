L = int(input())
code = input()
r = 31
M = 1234567891

atoi = dict()

alps = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
      "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

for index, alp in enumerate(alps):
    atoi[alp] = index + 1

H = 0
for index, alp in enumerate(code):
    H += atoi[alp] * (r**index)

print(H%M)
    