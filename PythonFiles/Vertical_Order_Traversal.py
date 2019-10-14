
# coding: utf-8

# In[11]:


#create binary tree class
class Binary_Tree():
    
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.position=0 # give position to each node......node' position equals its root nodes position-1 
                        #if it is left child of root else it is root node's position +1
                        # All with same position are in same verticle line


# In[43]:


def vertical_order_traversal(root):
    queue=[]
    queue.append(root)
    start=0
    end=1
    diction={}
    while start<end:
        
        #pop element and update start
        element=queue[start]
        start+=1
        
        #update position dictionary
        if element.position in diction:
            diction[element.position].add(element.data)
        else:
            s=set()
            s.add(element.data)
            diction[element.position]=s
        
        #add childerns of popped element in queue and update their position
        if element.left!=None:
            element.left.position=element.position-1
            queue.append(element.left)
            end+=1
        if element.right!=None:
            element.right.position=element.position+1
            queue.append(element.right)
            end+=1
    
    #iterate map and print values on seperate line to get vertical order travsersal
    for key, value in diction.items():
        print(value)
        
        
        


# In[55]:


from IPython.display import Image
print('Example Tree')
Image("tree_vertical_order_traversal.png")


# In[44]:


bt=Binary_Tree(1)
bt.left=Binary_Tree(2)
bt.right=Binary_Tree(3)
bt.left.left=Binary_Tree(4)
bt.left.right=Binary_Tree(5)
bt.right.left=Binary_Tree(6)
bt.right.right=Binary_Tree(7)
bt.right.left.right=Binary_Tree(8)
bt.right.right.right=Binary_Tree(9)


# In[45]:


vertical_order_traversal(bt)

