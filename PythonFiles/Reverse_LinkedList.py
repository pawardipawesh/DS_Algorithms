#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Reverse a Linked List without using any auxiliary space
class LinkedList:
    def __init__(self,data):
            self.data=data
            self.next=None
            
    def reverse(list_head):
        previous_node=None
        next_node=list_head.next
        
        while next_node!=None:
            list_head.next=previous_node
            previous_node=list_head
            list_head=next_node
            next_node=next_node.next
        list_head.next=previous_node
        return list_head
    
    def traverse(list_head):
        temp=list_head
        while temp!=None:
            print(temp.data)
            temp=temp.next


# In[12]:


#create list
list_head=LinkedList(1)
list_head.next=LinkedList(2)
list_head.next.next=LinkedList(3)
list_head.next.next.next=LinkedList(4)


# In[13]:


LinkedList.traverse(list_head)


# In[14]:


list_head=LinkedList.reverse(list_head)


# In[15]:


LinkedList.traverse(list_head)


# In[ ]:




