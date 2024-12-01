class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BST:
    def __init__(self):
        self.root = None
        
    def insert(self, value):
        def _insert(root, value):
            if not root:
                return TreeNode(value)
            if value < root.value:
                root.left = _insert(root.left, value)
            else:
                root.right = _insert(root.right, value)
            return root
        self.root = _insert(self.root, value)

    def search(self, value):
        def _search(root, value):
            if not root or root.value == value:
                return root is not None
            if value < root.value:
                return _search(root.left, value)
            else:
                return _search(root.right, value)
        return _search(self.root, value)



# Create the BST from the example

bst_tree = BST()
bst_tree.insert(5)
bst_tree.insert(3)
bst_tree.insert(8)
bst_tree.insert(1)
bst_tree.insert(4)
bst_tree.insert(7)
bst_tree.insert(10)

# Insert the new node with data = 6
bst_tree.insert(6)

print('-----yes-----')