def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    # transpose a matrix 
    # take rows and cols 
    # flip the numbers 

    a_rows = len(a)
    a_cols = len(a[0])
    
    t_a_rows = a_cols
    t_a_cols = a_rows
    t_a = [[0 for _ in range(t_a_cols)] for _ in range(t_a_rows)]

    for i in range(a_rows):
        for j in range(a_cols):
            t_a[j][i] = a[i][j]
    return t_a
    