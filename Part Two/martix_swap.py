import numpy as np

def swap_rows(M, a, b):
    if(a > len(M) or b > len(M)):
        print("invalid indices")
        return None
    M[[a, b]] = M[[b, a]]
    return M

M = np.array([[1,1,1], [2,2,2], [3,3,3]])

print(swap_rows(M, 1, 2))

def swap_cols(M, a, b):
    if(a > len(M) or b > len(M)):
        print("invalid indices")
        return None
    M[:, [a, b]] = M[:, [b, a]]
    return M

N = np.array([[1,2,3], [1,2,3], [1,2,3]])

print(swap_cols(N, 1, 2))