#This class will a base class for creating binary tree and traversing it.
class Binary_Tree():
    def __init__(self,data,left,right):
        self.data=data
        self.left=left
        self.right=right
    

    def create_tree(self):
        
        self.left=Binary_Tree(2,None,None)
        self.right=Binary_Tree(3,None,None)
        self.left.left=Binary_Tree(4,None,None)
        self.left.right=Binary_Tree(5,None,None)
        self.right.left=Binary_Tree(6,None,None)
        self.right.right=Binary_Tree(7,None,None)
        self.left.left.left=Binary_Tree(8,None,None)
        self.left.left.right=Binary_Tree(9,None,None)
        self.left.right.left=Binary_Tree(10,None,None)
        self.left.right.right=Binary_Tree(11,None,None)
        self.right.left.left=Binary_Tree(12,None,None)
        self.right.left.right=Binary_Tree(13,None,None)
        self.right.right.left=Binary_Tree(14,None,None)
        self.right.right.right=Binary_Tree(15,None,None)
    
    def inorder_traversal(self):
        if self.left!=None:
            self.left.inorder_traversal()
        print(self.data)
        if self.right!=None:
            self.right.inorder_traversal()
    
    def preorder_traversal(self):
        print(self.data)
        if self.left!=None:
            self.left.preorder_traversal()
        if self.right!=None:
            self.right.preorder_traversal()
            
    def postorder_traversal(self):
        if self.left!=None:
            self.left.postorder_traversal()
        if self.right!=None:
            self.right.postorder_traversal()
        print(self.data)
