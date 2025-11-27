st = input()  # 3.1 Получение ПСП
rem = 0
opened = 0

for s in st:
    if s == "(":
        opened += 1
    else:
        if opened > 0:
            opened -= 1
        else:
            rem += 1

rem += opened

print(rem)
