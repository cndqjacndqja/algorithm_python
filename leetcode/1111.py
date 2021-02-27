def maxDepthAfterSplit(seq):
    print(seq)
    a = []
    ans = [0 for _ in range(len(seq))]
    for i in range(len(seq)):
        c = seq[i]

        if c == '(':
            if len(a) == 0:
                a.append(0)
            else:
                a.append(1 - a[-1])
                ans[i] = a[-1]
                print(a)
        else:
            ans[i] = a[-1]
            a.pop()
    return ans

#
# [0,1,1,1,1,0]
print(maxDepthAfterSplit("(()())"))
