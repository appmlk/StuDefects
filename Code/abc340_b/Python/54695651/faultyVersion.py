Q = int(input())
A = []
for _ in range(Q):
  t, k = map(int, input().split())
  if t == 1:
    A.append(t)
  else:
    print(A[-k])