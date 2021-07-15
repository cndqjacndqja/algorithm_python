a, b, c, d, e, f = map(int, input().split())

# x = (f/e-c/b) / (d/e-a/b)
# y = (c - a*x)/b

x = (c*e-b*f)//(a*e-b*d)
y = (c*d-a*f)//(b*d-a*e)

print(x, y)
