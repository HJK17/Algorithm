# 使用a,b两个list来模拟链表，可以看出交叉点是 7这个节点
a = [1, 2, 3, 7, 9, 1, 5]  # 7
b = [4, 5, 7, 9, 1, 5]  # 6

for i in range(1, min(len(a), len(b))):
    if i == 1 and (a[-1] != b[-1]):
        print("No")
        break
    else:
        if a[-i] != b[-i]:
            print("交叉节点：", a[-i + 1])
            break
        else:
            pass
