def bubble(x):  # 1.1 Bubble sort
    if len(x) <= 1:
        return x

    for i in range(len(x) - 1):
        for j in range(len(x) - 1 - i):
            if x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]
    return x


test = [1, 6, 2, 5, 9, 3, 5, 3, 6, 7, 4, 8, 1]
print(bubble(test))
