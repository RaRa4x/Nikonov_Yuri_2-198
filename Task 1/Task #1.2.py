def merge_sort(x):  # 1.2 Megre sort
    if len(x) <= 1:
        return x

    mid = len(x) // 2
    left = merge_sort(x[:mid])
    right = merge_sort(x[mid:])

    return merge(left, right)


def merge(l, r):
    result = []
    i = j = 0

    while len(l) > i and len(r) > j:
        if l[i] <= r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1

    result.extend(l[i:])
    result.extend(r[j:])

    return result


test = [1, 6, 2, 5, 9, 3, 5, 3, 6, 7, 4, 8, 1]
print(merge_sort(test))
