from SmallWorldGraph import Graph

class Test_UF(object):

    @classmethod
    def setup_class(klass):
        print("\n#####  Start Function Tests   #####\n")

    def test_one(self):
        pass
    def test_two(self):
        expected = (1, 2, 3)
        actual = (1, 2, 3)
        assert expected == actual
    def test_graphVertices(self):
        g = Graph(9)
        actual = g.V
        expected = 9

        assert expected == actual
    def test_graph(self):
        g = Graph(9)
        g.edges = [[0, 1, 0, 0, 0, 0, 0, 1, 0],
         [1, 0, 1, 0, 0, 0, 0, 1, 0],
         [0, 1, 0, 1, 0, 1, 0, 0, 1],
         [0, 0, 1, 0, 1, 1, 0, 0, 0],
         [0, 0, 0, 1, 0, 1, 0, 0, 0],
         [0, 0, 1, 1, 1, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 1, 1],
         [1, 1, 0, 0, 0, 0, 1, 0, 1],
         [0, 0, 1, 0, 0, 0, 1, 1, 0]
         ]
        expected = [[0, 1, 0, 0, 0, 0, 0, 1, 0],
         [1, 0, 1, 0, 0, 0, 0, 1, 0],
         [0, 1, 0, 1, 0, 1, 0, 0, 1],
         [0, 0, 1, 0, 1, 1, 0, 0, 0],
         [0, 0, 0, 1, 0, 1, 0, 0, 0],
         [0, 0, 1, 1, 1, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 1, 1],
         [1, 1, 0, 0, 0, 0, 1, 0, 1],
         [0, 0, 1, 0, 0, 0, 1, 1, 0]
         ]
        actual = g.edges

        assert expected == actual
    def test_driver(self):
        g = Graph(9)
        edges = [[] for i in range(9)]
        g.addEdge(0, 1)
        g.addEdge(0, 7)
        g.addEdge(1, 7)
        g.addEdge(1, 2)
        g.addEdge(2, 3)
        g.addEdge(2, 5)
        g.addEdge(2, 8)
        g.addEdge(3, 4)
        g.addEdge(3, 5)
        g.addEdge(4, 5)
        g.addEdge(5, 6)
        g.addEdge(6, 7)
        g.addEdge(7, 8)

        actual = g.minDistBFS(5,1)
        expected = 2

        assert expected == actual