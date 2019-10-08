#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Binary_Tree import Binary_Tree


# In[3]:


root=Binary_Tree(1,None,None)
root.create_tree()


# In[4]:


root.inorder_traversal()


# In[5]:


def create_mirror(root):
    
    if root==None:
        return None
    
    left_mirrored=create_mirror(root.left)
    right_mirrored=create_mirror(root.right)
    
    root.left=right_mirrored
    root.right=left_mirrored
    
    return root


# In[6]:


mirrored_tree_root=create_mirror(root)


# In[7]:


mirrored_tree_root.inorder_traversal()


# In[ ]:




