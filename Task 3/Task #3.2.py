n = int(input())  # 3.2 Ближайший меньший

a = input().split()
arr = [int(x) for x in a]

res = [-1] * n
stack = []

for i in range(n):
    while stack and arr[i] < arr[stack[-1]]:
        res[stack.pop()] = i
    stack.append(i)

print(res)
