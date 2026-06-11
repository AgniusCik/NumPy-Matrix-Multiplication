import numpy as np

def multiply(matrix1, matrix2):
    if (matrix1.shape[1] != matrix2.shape[0]):
        print("The number of columns in first matrix is not equal to number of rows in second matrix")
        return
    
    result = np.zeros((matrix1.shape[0], matrix2.shape[1])) # creating an empty matrix with the num of rows of matrix 1 and num of columns of matrix 2
    for rows in range(0, result.shape[0]):
        for cols in range(0, result.shape[1]):
            result[rows, cols] = np.sum(matrix1[rows, :] * matrix2[:, cols])
    
    return result


m1 = np.array([[1, 2, 6], 
               [11, 44, 9], 
               [12, 3, 8]])

m2 = np.array([[7, 4, 6], 
               [22, 1, 9], 
               [11, 1, 1]])

m3 = np.array([[1, 2], [3, 4]])

m4 = np.array([[22, 2], 
              [4, 88], 
              [102, 66]])

print(multiply(m1, m2))
multiply(m1, m3)
print(multiply(m2, m4))