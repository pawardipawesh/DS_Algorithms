#!/usr/bin/env python
# coding: utf-8

# In[17]:


#code

def sub_array_with_sum(array, in_sum):
    from_index=0
    to_index=0
    sum_till_now=0
    for i,e in enumerate(array):
        #print(str(i)+str(e))
        sum_till_now+=int(array[i])
        to_index=i
        
        if sum_till_now==in_sum:
            return str(from_index+1)+' '+str(to_index+1)
        
        if sum_till_now<in_sum:
            
            continue
        else:
            sum_till_now-=int(array[from_index])
            from_index+=1
            while sum_till_now>=in_sum:
                if sum_till_now==in_sum:
                    return str(from_index+1)+' '+str(to_index+1)
                else:
                    sum_till_now-=int(array[from_index])
                    from_index+=1
                
    return str(-1)
                
def main():
    no_test_cases=input()
    for test_case in no_test_cases:
        inp=input()
        inp_arr=inp.split()
        array_len=inp_arr[0]
        in_sum=inp_arr[1]
        array=input()
        #print(str(array)+str(in_sum))
        output_str=sub_array_with_sum(array.split(), int(in_sum))
        print(output_str)


# In[18]:


main()


# In[ ]:




