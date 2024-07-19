n = int(input())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))

X_levels = set(X[1:])
Y_levels = set(Y[1:])

all_levels = X_levels | Y_levels

if all(level in all_levels for level in range(1, n+1)):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")


# Wrong answer
# n = int(input())
# X = list(map(int,input().split()))
# Y = list(map(int, input().split()))

# p = X[0]
# q = Y[0]

# X = X[1:]
# Y = Y[1:]

# newlist = X + Y
# newlist.sort()
# newlist = set(newlist)
# newlist = list(newlist)

# nums = []
# for i in range(n):
#     nums.append(i+1)

# if newlist == nums:
#     print("I become the guy.")
# else:
#     print("Oh, my keyboard!")
