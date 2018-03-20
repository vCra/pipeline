from itertools import product
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
        commands = {}

        def _convert(array):
            d = {}
            for i in array:
                if type(i) == dict:
                    d.update(i)
                else:
                    e = dict(x.split('=') for x in i.split(','))
                    d.update(e)
            return d

        for setting in matrix:
            commands.update({setting: []})
            pprint(setting)
            dicts = matrix[setting]
            try:
                dicts = _convert(dicts)
                a = ((dict(zip(dicts, x)) for x in product(*dicts.values())))
                for i in a:
                    commands.get(setting).append(i)
            except:
                e = matrix[setting]
                if type(e) == list:
                    for i in e:
                        commands.get(setting).append(i)
                elif type(e) == str:
                    commands.get(setting).append(matrix[setting])
                else:
                    print(e)

        pprint(commands)
        return (dict(zip(commands, x)) for x in product(*commands.values()))
