#!/usr/bin/env python
# coding: utf-8

# ### Following code expects elements to be present in tree.....otherwise results are not correct

# In[1]:


from Binary_Tree import Binary_Tree


# In[2]:


def find_LCA(root,element1,element2):
    if root==None:
        return None
    
    if root.data==element1 or root.data==element2:
        return root
    
    left=find_LCA(root.left,element1,element2)
    right=find_LCA(root.right,element1,element2)
    
    if left and right:
        return root
    
    if left:
        return left
    
    if right:
        return right


# In[3]:


root=Binary_Tree(1,None,None)
root.create_tree()


# In[14]:


root.preorder_traversal()


# In[13]:


find_LCA(root,3,14).data


# In[ ]:




