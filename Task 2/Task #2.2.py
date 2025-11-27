# 2.2 Shift
S = input()
T = input()

if len(S) != len(T):
    print("-1")
elif S == T:
    print("0")
else:
    double_S = S + S
    if double_S.find(T) != -1:
        print(len(S) - double_S.find(T))
    else:
        print("-1")
