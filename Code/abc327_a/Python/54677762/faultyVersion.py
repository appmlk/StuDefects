N = int(input())
S = input()

f = False
for i in range(N - 1):
    if S[i] == "a" and S[i + 1] == "b":
        f = True

if f:
    print("Yes")
else:
    print("No")