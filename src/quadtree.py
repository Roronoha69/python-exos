from __future__ import annotations
import json

class QuadTree:
    NB_NODES : int = 4

    def __init__(self, hg: bool | QuadTree, hd: bool | QuadTree, bd: bool | QuadTree,bg: bool | QuadTree):
        self.hg = hg
        self.hd = hd
        self.bd = bd
        self.bg = bg
        

    @staticmethod
    def fromFile(filename: str) -> QuadTree:
        #""" Ouvrir un fichier donné contenant une représentation textuelle d'une liste """
        # Lire le fichier et faire une liste
        file = open(filename)
        easyQaud = file.read()
        liste = json.loads(easyQaud)
        tableau = list(liste)
        #print(tableau)
        
        return tableau


    @staticmethod
    def fromList(data: list) -> QuadTree:
        #""" Génère un Quadtree à partir d'une représentation sous forme de liste """
        # Reprendre la boucle depth modifié pour créer un 
        pass

    def depth(self, data) -> int:
        #""" Profondeur de récursion du quadtree """
        count = 0
        stack_items = [data]
        stack_depths = [0]
        
        while stack_items:
            current_item = stack_items.pop() # Retire le dernier element pour boulcer sur toute la liste
            current_depth = stack_depths.pop()

            if isinstance(current_item, list):
                for nestedArray in current_item:
                    stack_items.append(nestedArray) # le dernier element devient nested array donc on vas reboucler a l'interieure jusqu'a avoir trouver tou les nested elemeent 
                    stack_depths.append(current_depth + 1)
                    print(nestedArray)

            count = current_depth if count < current_depth else count

        print("final", count)
        return count

p = QuadTree
tableau = p.fromFile("../files/quadtree.txt")
p.__init__(p, tableau[0], tableau[1], tableau[2], tableau[3])
p.depth(p, tableau)


class TkQuadTree(QuadTree):
    def paint(self):
        """ Représentation TK d'un Quadtree """
        pass 