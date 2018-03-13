class MatrixManager(object):
    """
    The matrix manager is used ti
    """
    matrix = {}
    vertices = []

    def __init__(self, matrix):
        self.matrix = matrix
        self.vertices = self.gen_combinations()
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

    def gen_combinations(self):
        """
        Generates combinations of strings, based on the provided matrix
        """
        import itertools

        matrix = self.get_matrix()

        names = sorted(matrix)  # The "Headings" of each matrix item

        combinations = itertools.product(*(matrix[name] for name in names))
        jobs = []

        for c in combinations:
            d = {}
            for i in range(len(names)):
                d.update({names[i]: c[i]})
            jobs.append(d)

        return jobs
