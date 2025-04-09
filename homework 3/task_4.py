
def transpon(matrix):
    lines = len(matrix)
    columns = len(matrix[0])
    
    new_matrix = []
    for i in range (columns):
        new_line = []
        for j in range (lines):
            new_line.append(matrix[j][i])
        new_matrix.append(new_line)
    return new_matrix

#example
matrix = [[1,2,3],[4,5,6]]
new_matrix = transpon(matrix)
print(new_matrix)