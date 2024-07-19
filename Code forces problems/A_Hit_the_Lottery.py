def minimum_bills(n):
    denominations = [100, 20, 10, 5, 1]

    num_bills = 0
    
    for bill in denominations:
        if n == 0:
            break
        num_bills += n // bill
        n %= bill
    
    return num_bills

n = int(input().strip())

print(minimum_bills(n))

# wrong answer
# while n != 0:
#     if n >= 100:
#         counter +=1
#         n -= 100
#     elif n >= 20:
#         counter +=1
#         n -= 20
#     elif n >= 10:
#         counter +=1
#         n -= 10
#     elif n >= 5:
#         counter +=1
#         n -= 5
#     elif n >= 1:
#         counter +=1
#         n -= 1
# print(counter)