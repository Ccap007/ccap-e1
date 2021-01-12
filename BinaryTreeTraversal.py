class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, "")

        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False

    def preorder_print(self, start, traversal):
        """Root->Left->Right"""
        if start:
            # this takes traversal and adds to it the string value of start, 
            # along with dash separator 
            # seems that using the variable in a call of itself is recursion
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal
    
    def inorder_print(self, start, traversal):
        """Leftmost->Root->Right"""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        """Left->Right->Root"""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal = self.inorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

# PREORDER
# output left to right
# 1-2-4-5-3-6-7-
#
#                    1
#                 /     \
#                2        3
#               / \      / \
#              4   5    6   7  
#
# right to left 
# 1-3-7-6-2-5-4
# 
# INORDER
# 4-2-5-1-6-3-7
#
# POSTORDER
# 4-2-5-6-3-7-1
#


# Set up the tree:
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
# if there was...
#tree.root.right.right.right = Node(8) 

print(tree.print_tree("preorder"))
#print(tree.print_tree("inorder"))
#print(tree.print_tree("postorder"))
print(tree.print_tree("fake"))