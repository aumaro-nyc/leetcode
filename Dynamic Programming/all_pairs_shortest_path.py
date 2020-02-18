# All pairs shortest path DP

def all_pairs(input_matrix, n):
    """ Returns an adjacency matrix containing the shortest path between
        all nodes.

    @param: input_matrix: n+1 x n+1 matrix with edge weights (A0[])
    @param: n: number of nodes in the graph
    @rtype -> n+1 x n+1 modified matrix containing shortes paths
    """
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                input_matrix[i][j] = min(input_matrix[i][j], input_matrix[i][k] + input_matrix[k][j])
    return input_matrix


INF = float('inf')
_input = [
    [0,0,0,0,0],
    [0,0,3,INF,7],
    [0,8,0,2,INF],
    [0,5,INF,0,1],
    [0,2,INF,INF,0]
]

output = all_pairs(_input, 4)
for row in output:
    print(row)
