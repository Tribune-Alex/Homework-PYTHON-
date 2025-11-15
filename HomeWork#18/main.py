class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def _insert(self,node,key):
        if node is None:
            return Node(key)
        

        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right,key)

        return node
    
    def insert(self,key):
        self.root = self._insert(self.root,key)


    def _leaf_nodes(self, node):
        if node is None:
            return

        
        if node.left is None and node.right is None:
            print(node.key)
            return

        
        self._leaf_nodes(node.left)
        self._leaf_nodes(node.right)

    def print_leaf_nodes(self):
        print("Leaf nodes:")
        self._leaf_nodes(self.root)


bst= BST()

bst.insert(33)
bst.insert(11)
bst.insert(3)
bst.insert(95)
bst.insert(9)
bst.insert(15)
bst.insert(8)
bst.insert(125)
bst.insert(17)
bst.insert(49)
bst.insert(51)
bst.insert(67)

print(bst.print_leaf_nodes())




        