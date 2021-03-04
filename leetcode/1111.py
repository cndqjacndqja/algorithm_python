def maxDepthAfterSplit(seq):
    stack = []
    ans = [0 for _ in range(len(seq))]
    for i in range(len(seq)):
        c = seq[i]

        if c == '(':
            if len(stack) == 0:
                stack.append(0)
            else:
                stack.append(1 - stack[-1])
                ans[i] = stack[-1]
                print(stack)
        else:
            ans[i] = stack[-1]
            stack.pop()
    return ans

#
# [0,1,1,1,1,0]
print(maxDepthAfterSplit("(()())"))
