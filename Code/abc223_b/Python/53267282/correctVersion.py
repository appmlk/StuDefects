s = input()
min_,max_ = s,s
for i in range(1,len(s)):
  if min_>s[i:]+s[:i]:
    min_ = s[i:]+s[:i]
  if max_<s[i:]+s[:i]:
    max_ = s[i:]+s[:i]
print(min_)
print(max_)