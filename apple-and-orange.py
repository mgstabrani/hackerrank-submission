st = input().split(" ")
s = int(st[0])
t = int(st[1])
ab = input().split(" ")
a = int(ab[0])
b = int(ab[1])
mn = input().split(" ")
m = int(mn[0])
n = int(mn[1])
apples = list(map(int, input().split(" ")))
oranges = list(map(int, input().split(" ")))
countapples = 0
countoranges = 0
for i in range(m):
    apples[i] = a + apples[i]
    if(apples[i] >= s and apples[i] <= t):
        countapples += 1
for i in range(n):
    oranges[i] = b + oranges[i]
    if(oranges[i] >= s and oranges[i] <= t):
        countoranges += 1
print(countapples)
print(countoranges)


