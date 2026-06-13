
nums = [1,2,3,4,5,6,7]

x = 3
lam = lambda x: x * 2

print(lam(x))

lamlist = list(map(lambda num : num * num , nums))

print(lamlist)

evennums = list(filter(lambda num : num%2 == 0, lamlist))

print(evennums)
