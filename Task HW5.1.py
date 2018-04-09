import copy

class ErrorInMatrix(Exception):
    """This Error describes any error
    in Object Matrix"""

    pass

class Matrix:
    """Class Matrix."""
    def __init__(self,mat,mat2=''):
        """Object constructor
        :param - matrix
        :type - list
        """
        if type(mat) == list:
            self.mat = mat
            self.row = len(mat)
            self.col = len(mat[0])
            for element in mat:
                if len(element) != len(mat[0]):
                    raise ErrorInMatrix("There is no matrix here,give me better")
        elif type(mat) == int and type(mat2) == int:
            a = []
            matrix = []
            a.append(mat)
            a.append(mat2)
            matrix.append(a)
            self.mat = matrix
            self.row = len(matrix)
            self.col = len(matrix[0])



    def __eq__(self, new_mat):
        """Overriding operator =
        :param - matrix
        :type - Matrix
        :return - boolean value
        """
        return(new_mat.mat == self.mat)

    def __ne__(self, new_mat):
        """Overriding operator !=
        :param - matrix
        :type - Matrix
        :return - boolean value
        """
        return(new_mat.mat != self.mat)

    def __add__(self, new_mat):
        """Overriding operator +
        :param - matrix
        :type - Matrix
        :return - new Matrix object
        """

        if type(new_mat) == Matrix:
            if self.row != new_mat.row or self.col != new_mat.col:
                raise ErrorInMatrix('Wrong matrix size')
            result = copy.deepcopy(self.mat)
            for i in range(self.row):
                 for j in range(self.col):
                    result[i][j] += new_mat.mat[i][j]
            return Matrix(result)
        else:
            raise ErrorInMatrix('Wrong type, you need matrix type')

    def __sub__(self, new_mat):
        """Overriding operator -
        :param - matrix
        :type - Matrix
        :return - new Matrix object
        """

        if type(new_mat) == Matrix:
            if self.row != new_mat.row or self.col != new_mat.col:
                raise ErrorInMatrix('Wrong matrix size')
            result = copy.deepcopy(self.mat)
            for i in range(self.row):
                 for j in range(self.col):
                    result[i][j] -= new_mat.mat[i][j]
            return Matrix(result)
        else:
            raise ErrorInMatrix('Wrong type, you need matrix type')

    def __str__(self):
        """Print operator
        :param - matrix
        :type - Matrix
        :return - pretty matrix
        """

        s='['+'\n['.join([','.join([''+ str(item) for item in row ])+']' for row in self.mat])
        return '['+ s +']'

    def transpose(self):
        """Transpose method
        :param - matrix
        :type - Matrix
        :return - new transposed Matrix
        """

        result = []
        for i in range(self.col):
            result.append([0 for j in range(self.row)])
        for i in range(self.row):
            for j in range(self.col):
                result[j][i] = self.mat[i][j]
        return Matrix(result)

    def __mul__(self, new_mat):
        """Overriding operator *
        :param - matrix
        :type - Matrix
        :return - new Matrix object
        """

        if type(new_mat) == int or type(new_mat) == float:
            result = copy.deepcopy(self.mat)
            for i in range(self.row):
                for j in range(self.col):
                    result[i][j] *= new_mat
            return result
        elif type(new_mat) == Matrix:
            if self.col != new_mat.row:
                raise ErrorInMatrix('Wrong size of matrix')
            result = []
            for i in range(self.row):
                result.append([0 for j in range(new_mat.col)])
            for i in range(self.row):
                for j in range(new_mat.col):
                    result[i][j] = sum([item[0] * item[1] for item in zip(self.mat[i],new_mat.transpose().mat[j])])
            return Matrix(result)
        else:
            raise ErrorInMatrix('Wrong type of argument')

    def is_symmetrical(self):
        """Method which check symmetry of matrix
        Implements only for square matrix
        :param - matrix
        :type - Matrix
        :return - boolean value
        """

        if (not self.is_square()):
            raise ErrorInMatrix('This matrix is not square')
        else:
            for i in range(self.row):
                for j in range(self.col):
                    if self.mat[i][j] != self.mat[j][i]:
                        return False
                    else:
                        return True

    def is_square(self):
        """Method which check squere matrix
        :param - matrix
        :type - Matrix
        :return - boolean value
        """
        return self.row == self.col


if __name__ == "__main__":
    #a = Matrix([[1,2],[2,1],[2,2]])
    #b = Matrix([[1,2],[2,2]])
    #c = Matrix([[2,3,4],[5,6,7]])
    #d = Matrix([[1,2],[3,4],[7,6]])
    d = Matrix(2,2)
    m = Matrix(2,2)
    print(m.is_square())
    #print(a==b)
    #print(a.is_square())
    #print(a.is_symmetrical())
    #print(a!=b)
    #print(a+b)
   # print(a+'c')