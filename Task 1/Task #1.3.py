import random


def quick(x):  # 1.3 Quick sort
    if len(x) <= 1:
        return x
    piv = random.choice(x)
    l = [i for i in x if i < piv]
    m = [i for i in x if i == piv]
    r = [i for i in x if i > piv]

    return quick(l) + m + quick(r)


test = [1, 6, 2, 5, 9, 3, 5, 3, 6, 7, 4, 8, 1]
print(quick(test))
