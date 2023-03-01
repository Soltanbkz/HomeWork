dict = {}
u = int(input())
while len(dict) != u:
    x, y = input().split()
    dict.update({x: y})
    if u == "Stop":
        break


print(dict.keys(), "-", dict.values() )
