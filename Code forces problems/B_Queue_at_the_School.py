# n, t = map(int, input().split())

# children = input()
# childrenq = list(children)

# for i in range(t):
#     i = 0
#     while i < len(children)-1:
#         if childrenq[i] == "B" and childrenq[i+1] == "G":
#             childrenq[i], childrenq[i+1] = childrenq[i+1], childrenq[i]
#             i +=2
#         else:
#             i += 1
# print("".join(childrenq))

n, t = map(int, input().split())
children = list(input())

for _ in range(t):
    swaps = []
    for i in range(len(children) - 1):
        if children[i] == "B" and children[i+1] == "G":
            swaps.append(i)
    for i in swaps:
        children[i], children[i+1] = children[i+1], children[i]

print("".join(children))