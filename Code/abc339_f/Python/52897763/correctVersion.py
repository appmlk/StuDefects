n = int(input())
mod = 98080989074039189058908908209991
a = [int(input())%mod for _ in range(n)]
d = dict()

for i in a:
    d.setdefault(i,0)
    d[i] += 1

ans = 0
for i in a:
    for j in a:
        value = i*j%mod
        if value in d: ans += d[value%mod]

print(ans)