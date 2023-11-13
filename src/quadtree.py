from __future__ import annotations
import json
import tkinter as tk

class QuadTree:
    NB_NODES : int = 4

    def __init__(self, hg: bool | QuadTree, hd: bool | QuadTree, bd: bool | QuadTree,bg: bool | QuadTree):
        self.hg = hg
        self.hd = hd
        self.bd = bd
        self.bg = bg
        

    @staticmethod
    def fromFile(filename: str) -> list:
        # str) -> QuadTree: wtf pourquoi 2 fonction retournerai un quadtree ? go retourner une list
        file = open(filename)
        easyQaud = file.read()
        liste = json.loads(easyQaud)
        tableau = list(liste)
        
        return tableau


    @staticmethod
    def fromList(data: list) -> QuadTree:
        if len(data) == 0:
            return QuadTree(None, None, None, None)
        else:
            self.hg = QuadTree.fromList(data[0])
            self.hd = QuadTree.fromList(data[1])
            self.bg = QuadTree.fromList(data[2])
            self.bd = QuadTree.fromList(data[3])
            return QuadTree(hg, hd, bg, bd)


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

def draw_square(canvas, color):
    # Remettre ma boucle while avec sa logique ici ?
    canvas.create_rectangle(50, 50, 150, 150, fill=color)

root = tk.Tk()
root.title("Carré Noir")

canvas = tk.Canvas(root, width=600, height=600)
canvas.pack()

# Passer le Quadtreee
draw_square(canvas, "black")

root.mainloop()