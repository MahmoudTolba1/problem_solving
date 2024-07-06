# words,shorts = [],[]
# for i in range(int(input())):
#     words.append(input())
# for i in words:
#     if len(i) <= 10:
#         print(i)
#     else:
#         # print(f"{i[0]}{len(i[:-2])}{i[-1]}")
#         print(i[0] + str(len(i[:-2])) + i[-1])
#         # word = i[0] + str(len(i[:-2])) + i[-1]
#         # print(word)
# [print(x) for x in words]


words = [input() for _ in range(int(input()))]
for word in words:
    print(word if len(word) <= 10 else word[0] + str(len(word) - 2) + word[-1])


# [print(word if len(word) <= 10 else word[0] + str(len(word) - 2) + word[-1]) for word in [input() for _ in range(int(input()))]]

# def simplify_word(word):
#     if len(word) <= 10:
#         return word
#     else:
#         return word[0] + str(len(word) - 2) + word[-1]

# num_words = int(input())
# words = [input() for _ in range(num_words)]
# for word in words:
#     print(simplify_word(word))