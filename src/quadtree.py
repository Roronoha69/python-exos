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
            hg = QuadTree.fromList(data[0])
            hd = QuadTree.fromList(data[1])
            bg = QuadTree.fromList(data[2])
            bd = QuadTree.fromList(data[3])
            return QuadTree(hg, hd, bg, bd)


    def depth(data) -> int:
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
            # Selectionne le derniers élément de la list pour voir s'il contients des arrays imbriqués
            # L'element est en meme temps retirer de la liste pour qu'on puisse reboucler jusqu'a la fin de la liste
            current_item = stack_items.pop() 
            current_depth = stack_depths.pop()

            if isinstance(current_item, list):
                for nestedArray in current_item:
                    # Le dernier élément devient nested array, donc on va reboucler à l'intérieur jusqu'à avoir trouvé tous les éléments imbriqués
                    stack_items.append(nestedArray) 
                    stack_depths.append(current_depth + 1)

            count = current_depth if count < current_depth else count

        return count
    


filename = "../files/quadtree.txt"
q = QuadTree.fromFile(filename)
depth = QuadTree.depth(q)
print(f"Profondeur du quadtree : {depth}")





class TkQuadTree():
    pass
    
def draw_four_squares(canvas):
    q = QuadTree.fromFile("../files/quadtree_easy.txt")
    size = 150
    
    # hg
    canvas.create_rectangle(0, 0, size, size, fill="white" if q[0] == 1 else "black")
    
    # hd
    canvas.create_rectangle(size, 0, size * 2, size, fill="white" if q[1] == 1 else "black")

    # bd
    canvas.create_rectangle(size, size, size * 2, size * 2, fill="white" if q[2] == 1 else "black")
    
    # bg
    canvas.create_rectangle(0, size, size, size * 2, fill="white" if q[3] == 1 else "black")


def initCanva():
    
    root = tk.Tk()
    root.title("Quadtree")

    canvas = tk.Canvas(root, width=300, height=300)
    canvas.pack()

    # Appelle la fonction pour dessiner les quatre carrés sur le canvas
    draw_four_squares(canvas)

    # Affiche un bouton Quit pour fermer la fenêtre
    tk.Button(root, text="Quit", command=root.destroy).pack()

    root.mainloop()

initCanva()


