from pprint import pprint


class MatrixManager(object):
    """
    The matrix manager is used ti
    """
    matrix = {}
    vertices = []

    def __init__(self, matrix):
        self.matrix = matrix
        self.vertices = self.gen_combinations(self.matrix)
        super(MatrixManager, self).__init__()

    def get_matrix(self):
        """
        :return: the local matrix
        """
        return self.matrix

    def get_vertices(self):
        """
        :return: the local vertices
        """
        return self.vertices

    def in_use(self):
        """
        Is this matrix being used (i.e. it has values)
        :return: True if in use
        """
        return len(self.vertices) > 0


    def gen_combinations(self, matrix):
        """
        Generates combinations of strings, based on the provided matrix
        """

        def get_kv_pairs(dic):
            d = []
            for prop in dic:
                for item in dic[prop]:
                    if type(item) == dict:
                        d.append({prop: get_kv_pairs(item)})
                    else:
                        d.append({prop: item})
            return d

        import itertools


        pprint(get_kv_pairs(matrix))


