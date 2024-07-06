n = int(input())

# my_list = []
# for i in range(1, n+1):
#     my_list.append(i)

my_list = [i for i in range(1, n+1)]

if n % 2 != 0:
    print(-1)
else:
    for i in range(0, len(my_list) ,2):
        my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
    print(*my_list) # unpacking the list and separate with space


# n = int(input())
# def perfect_permutation(n):
    
#     my_list = [i for i in range(1, n+1)]
#     if n % 2 != 0:
#         print(-1)
#         return
    
#     for i in range(0, len(my_list) ,2):
#         my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
#     print(*my_list)

# perfect_permutation(n)