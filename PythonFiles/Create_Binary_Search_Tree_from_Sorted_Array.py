class tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def create_tree(sorted_arr):
    sorted_arr_len= len(sorted_arr)
    if sorted_arr_len==0:
        return None
    
    root=tree(sorted_arr[int(sorted_arr_len/2)])
    root.left=create_tree(sorted_arr[0:int(sorted_arr_len/2)])
    root.right=create_tree(sorted_arr[int(sorted_arr_len/2)+1:])
    
    return root

def inorder_traversal(root):
    if root==None:
        return
    inorder_traversal(root.left)
    print(root.data)
    inorder_traversal(root.right)

sorted_arr=[2,4,8,10,14,24,30]
root=create_tree(sorted_arr)
inorder_traversal(root)