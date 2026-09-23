def transpose(mat: list):
    """
    This function turns matrix m x n --> matrix n x m
    For the operation to be correct, it is necessary to enter a rectangular matrix.

    Example: [[1,2],[3,4]] --> [[1,3,[2,4]]]
    """
    if len(mat) == 0:
        return []
    l = len(mat[0])
    for i in mat:
        if len(i) != l:
            raise ValueError("Matrice isn't rectangly.")
        if type(i) != list:
            raise TypeError('The list contains elements that are not lists')
    res = []
    for i in range(l):
        new = []
        for j in range(len(mat)):
            new += [mat[j][i]]
        res.append(new)
    return res

print(transpose([[1,2,3]]))
print(transpose([[1],[2],[3]]))
print(transpose([[1,2], [3,4]]))
print(transpose([]))
print(transpose([[1,2],[3]]))


def row_sums(mat: list):
    """
    This function takes list and return list which contains row sums

    Example: [[1,2,3],[4,5,6]] --> [6,15]
    """

    res = []
    l = len(mat[0])
    for i in mat:
        if len(i) != l:
            raise ValueError("Matrice isn't rectangly.")

    for stroka in mat:
        res1 = 0
        for i in range(len(stroka)):
            if (type(stroka[i]) != int) and (type(stroka[i]) != float):
                raise TypeError('The list elements must be lists contains only int/float elemens.')
            else:
                res1 += stroka[i]
        res += [res1]
    return res

print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1,1], [10,-10]]))
print(row_sums([[0,0], [0,0]]))
print(row_sums([[1, 2], [3]]))

def col_sums(mat: list):
    '''
     This function takes list and return list which contains col sums
    
     Example: [[1,2,3],[4,5,6]] --> [5,7,9]
    '''
    res = []
    l = len(mat[0])
    for i in mat:
        if len(i) != l:
            raise ValueError("Matrice isn't rectangly.")      

    for i in range(l):
        res1 = 0
        for j in range(len(mat)):
            if (type(mat[j][i]) != int) and (type(mat[j][i]) != float):
                raise TypeError('The list elements must be lists contains only int/float elemens.')
            else:
                res1 += mat[j][i]
        res += [res1]
    return res

print(col_sums([[1, 2,3], [4,5,6]]))
print(col_sums([[-1,1], [10,-10]]))
print(col_sums([[0,0], [0,0]]))
print(col_sums([[1, 2], [3]]))