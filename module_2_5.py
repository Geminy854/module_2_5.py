def get_matrix(n, m, value):
    matrix =[]
    for i in range(n):
        list = []
        matrix.append(list)
        for j in range(m):
            list.append(value)
    return matrix

res_1 = get_matrix(2,2,10)
res_2 = get_matrix(3,5,42)
res_3 = get_matrix(4,2,13)

print(res_1)
print(res_2)
print(res_3)


