#!/usr/bin/env python
# coding: utf-8

# In[14]:


def digonally(array,array_len):
    i=0
    j=0
    output_str=''
    row=0
    column=0
    while True:
        output_str+=array[i][j]+' '
        i+=1
        j-=1
        
        if i>=len(array) or j<0:
            print(output_str.strip())
            output_str=''
            if column<array_len-1:
                column+=1
            else:
                if row < array_len-1:
                    row+=1
                else:
                    break
            i=row
            j=column


# In[15]:


def fill_matrix(array,array_len):
    matrix=[]
    i=0
    while True:
        if i>=array_len*array_len:
            break
        else:
            matrix.append(array[i:i+array_len])
            i+=array_len
                
    return matrix

def main():
    test_cases=int(input())
    
    for t in range(test_cases):
        array_len=int(input())
        array=input().split()
        matrix=fill_matrix(array,array_len)
        print(matrix)
        digonally(matrix,array_len)
if __name__=='__main__':
    main()


# In[ ]:




