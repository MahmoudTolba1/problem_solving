# for i in range(5):
#     matrix = [*map(int,input().split())]
#     index = 0
#     for i in range(len(matrix)):
#         if matrix[i] == 1:
#             index = i
# print(index)

def creat_matrix():
    rows= 5
    cols = 5
    matrix = []
    for i in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix

def index_of_one(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                return [i,j]

matrix = creat_matrix()
one_index = index_of_one(matrix)

perfect_pos = [2,2]

counter = 0
for i in range(len(perfect_pos)):
    counter += abs(perfect_pos[i] - one_index[i])
print(counter)