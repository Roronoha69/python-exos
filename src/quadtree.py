from __future__ import annotations
import json
import tkinter as tk

class QuadTree:
    """Représente un arbre quadtree."""
    
    NB_NODES : int = 4

    def __init__(self, hg: bool | QuadTree, hd: bool | QuadTree, bd: bool | QuadTree,bg: bool | QuadTree):
        """
        Initialise un nœud quadtree avec ses quatre sous-arbres.

        """
        self.hg = hg
        self.hd = hd
        self.bd = bd
        self.bg = bg
        

    @staticmethod
    def fromFile(filename: str) -> list:
        """
        Charge un quadtree depuis un fichier txt.
        Le mettre en json.

        Args:
        - filename (str): Chemin vers le fichier JSON.

        Returns:
        - list: Liste représentant le quadtree.
        """
        file = open(filename)
        easyQuad = file.read()
        liste = json.loads(easyQuad)
        tableau = list(liste)
        
        return tableau


    @staticmethod
    def fromList(data: list) -> QuadTree:
        """
        Construit un quadtree à partir d'une liste.

        Args:
        - data (list): Liste représentant le quadtree.

        Returns:
        - QuadTree: Instance du quadtree.
        """
        if len(data) == 0:
            return QuadTree(None, None, None, None)
        else:
            self.hg = QuadTree.fromList(data[0])
            self.hd = QuadTree.fromList(data[1])
            self.bg = QuadTree.fromList(data[2])
            self.bd = QuadTree.fromList(data[3])
            return QuadTree(hg, hd, bg, bd)


    def depth(self, data) -> int:
        """
        Calcule la profondeur du quadtree.

        Args:
        - data: Données du quadtree.

        Returns:
        - int: Profondeur du quadtree.
        """
        count = 0
        stack_items = [data]
        stack_depths = [0]
        
        while stack_items:
            current_item = stack_items.pop() # Retire le dernier élément pour boucler sur toute la liste
            current_depth = stack_depths.pop()

            if isinstance(current_item, list):
                for nestedArray in current_item:
                    stack_items.append(nestedArray) # Le dernier élément devient nested array, donc on va reboucler à l'intérieur jusqu'à avoir trouvé tous les éléments imbriqués
                    stack_depths.append(current_depth + 1)

            count = current_depth if count < current_depth else count

        return count


class TkQuadTree(QuadTree):
    pass
    
#     def paint(self):
        
#         pass 


# def draw_square(canvas, color):
#     # Remettre ma boucle while avec sa logique ici
#     canvas.create_rectangle(50, 50, 150, 150, fill=color)

# root = tk.Tk()
# root.title("Carré Noir")

# canvas = tk.Canvas(root, width=600, height=600)
# canvas.pack()

# # Passer le Quadtreee
# draw_square(canvas, "black")

# root.mainloop()
