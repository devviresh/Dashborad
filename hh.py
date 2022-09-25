def isSafe(mat, visited, x, y):
    return 0 <= x < len(mat) and 0 <= y < len(mat[0]) and \
           not (mat[x][y] == 0 or visited[x][y])
 
def findLongestPath(mat, visited, i, j, dest, max_dist=0, dist=0):
 
    if mat[i][j] == 0:
        return 0
    if (i, j) == dest:
        return max(dist, max_dist)
    visited[i][j] = 1
    if isSafe(mat, visited, i + 1, j):
        max_dist = findLongestPath(mat, visited, i + 1, j, dest, max_dist, dist + 1)
    if isSafe(mat, visited, i, j + 1):
        max_dist = findLongestPath(mat, visited, i, j + 1, dest, max_dist, dist + 1)
    if isSafe(mat, visited, i - 1, j):
        max_dist = findLongestPath(mat, visited, i - 1, j, dest, max_dist, dist + 1)
    if isSafe(mat, visited, i, j - 1):
        max_dist = findLongestPath(mat, visited, i, j - 1, dest, max_dist, dist + 1)
    visited[i][j] = 0
    return max_dist
 
 
def findLongestPathLength(mat, src, dest):
    i, j = src
    x, y = dest
    if not mat or len(mat) == 0 or mat[i][j] == 0 or mat[x][y] == 0:
        return 0
    (M, N) = (len(mat), len(mat[0]))
    visited = [[0 for x in range(N)] for y in range(M)]
    return findLongestPath(mat, visited, i, j, dest)
 
 
if __name__ == '__main__':
 
    # input matrix
    mat = [
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 0, 1, 1],
        [1, 1, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 0]
    ]
 
    src = (0, 0)
    dest = (5, 7)
 
    print("The maximum length path is", findLongestPathLength(mat, src, dest))
 