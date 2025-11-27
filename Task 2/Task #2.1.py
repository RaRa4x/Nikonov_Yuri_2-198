# 2.1 Find substring
Str = input()
Substr = input()

res = []
i = 0

while i < len(Str):
    index = Str.find(Substr, i)
    if index == -1:
        break
    res.append(index)
    i = index + 1

print(res)
