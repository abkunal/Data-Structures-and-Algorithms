""" Frievald's algorithm to chech matrix multiplication """

import random

def mat_mul(A, B, n):
    """
        A, B are two n*n square matrices
        Returns matrix C as the product of A and B
    """
    
    C = [[0 for i in range(n)] for j in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

    return C
    
A = [[2,3], [3,4]]
B = [[1,0], [1,2]]
n = 2
#C = [[6,5], [8,7]]
def mul_column_vector(A, B, C, r, n):
    """ outputs A.(B.r) and (C.r) """
    b = [[0] for i in range(n)]
    a = [[0] for i in range(n)]
    c = [[0] for i in range(n)]
    
    # calculates (B.r) and (C.r)
    for i in range(n):
        for k in range(n):
            b[i][0] += B[i][k] * r[k][0]
            c[i][0] += C[i][k] * r[k][0]
    
    # Calculates A.(B.r)
    for i in range(n):
        for k in range(n):
            a[i][0] += A[i][k] * b[k][0]
    
    b = [[0] for j in range(n)]
    # Calculates A.(B.r) - (C.r)
    for i in range(n):
        b[i][0] = a[i][0] - c[i][0]
        
    for i in range(n):
        if b[i][0] != 0:
            return False
    return True
    
    
def frievald(A, B, C, n):
    """ Check whether product of two square matrices A and B is correct or not. """
    # Generate a random column vector
    true = 0
    for i in range(10):
        r = [[random.randint(0,1)] for j in range(n)]
        print(r)
        if mul_column_vector(A, B, C, r, n) is True:
            true += 1
    
    if true == 10:
        print("Probability of error = 0")
    else:
        print("Probability of error: ", 1/2**10)
    #print("Correct with probability = %f", (true/30))
    
def main(A, B, n):
    """ Calculates matrix C as A x B and checks whether the multiplication is correct """
    C = mat_mul(A, B, n)
    
    frievald(A, B, C, n)
    
