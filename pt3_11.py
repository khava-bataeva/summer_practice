a = "n h f y e a n f h n"
n = {}
for k in a.split():
    n[k] = n.setdefault(k, 0) + 1
print(n)
