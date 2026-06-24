print("Hello World"[::-1])
print(['a',1, True][::-1])

s = "Hello World"
dup = []
for i in s:
    cnt = s.count(i)

    if cnt > 1:
        dup.append(i)

print(set(dup))


arr = [1,0,9,8,0,6,0,5,0,234]

zcnt = arr.count(0)
zlist = []
for i in range(zcnt):
    arr.remove(0)
    zlist.append(0)

arr.extend(zlist)

print(arr)

