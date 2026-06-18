def s(n):
    for i in range(n + 1):
        yield i * i

n = int(input())
for x in s(n):
    print(x)