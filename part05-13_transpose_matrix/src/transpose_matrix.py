# Write your solution here
def transpose(matrix: list):
    for x in range(len(matrix)):
        for y in range(x, len(matrix)):
            temp = matrix[x][y]
            matrix[x][y] = matrix[y][x]
            matrix[y][x] = temp
    

if __name__ == "__main__":
    matrix = [[1, 2], [1, 2]]
    print(matrix)
    transpose(matrix)
    print(matrix)