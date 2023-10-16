from __future__ import annotations

class QuadTree:
    NB_NODES : int = 4
    def __init__(self, hg: bool | QuadTree, hd: bool | QuadTree, bd: bool | QuadTree,bg: bool | QuadTree):
        self.hg = hg
        self.hd = hd
        self.bg = bg
        self.bd = bd

    @property
    def depth(self) -> int:
        """ Recursion depth of the quadtree"""
        return 1

    @staticmethod
    def fromFile(filename: str) -> QuadTree:
        """ Open a given file, containing a textual representation of a list"""
        data = []
        with open(filename) as f:
            lines = f.read()
            data = eval(lines)
        print(data)
        return QuadTree.fromList(data)

    @staticmethod
    def fromList(data: list) -> QuadTree:
        """ Generates a Quadtree from a list representation"""
        if isinstance(data, int):
            return data
        if len(data) == QuadTree.NB_NODES:
            q = QuadTree(
                QuadTree.fromList(data[0]),
                QuadTree.fromList(data[1]),
                QuadTree.fromList(data[2]),
                QuadTree.fromList(data[3])
            )
            return q

def test_sample():
    filename = "../files/quadtree.txt"
    q = QuadTree.fromFile(filename)
    assert q.depth == 4

def test_single():
    filename = "../files/quadtree_easy.txt"
    q = QuadTree.fromFile(filename)
    assert q.depth == 1