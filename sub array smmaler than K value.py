"""Given an integer array and an integer K, find the number of sub arrays in which all elements are less than K.
local
"""

import random
import itertools


def randf (start, end, num): #create random list, item numbers="num"
    rlist=[]
    global K
    K=random.randint(start,end)
    for x in range(num):
        rlist.append(random.randint(start,end))
        
    return rlist,K
    
def largest_sub(ls,k): # find the largest list smaller than K value
    lar_sub=[]
    for x in range(len(ls)):
        if ls[x]<k:
            lar_sub.append(ls[x]) #append all items smaller than K
    return lar_sub
    
def all_sub (largest_sub): #find all sub arrays in the list. 
    len_of_list = len(largest_sub)
    
    all_sub_arrays=[]
    
    if len_of_list >= 1:
        for i in range(1,len_of_list):
            all_sub_arrays.append(list(itertools.combinations(largest_sub,i)))
    else:
        print('list is empty')
    return all_sub_arrays
     


def fac_cal(length_of_list): #calculate factorial
    sz=1
    for fx in range(1,length_of_list+1):
        sz*=fx
    return sz
    
        
def comb_size(n,r): # combination of n with r elements in collection
    nr_fac=fac_cal(n)/fac_cal(n-r)/fac_cal(r) #__n!/((n-r)!*r!)__#
    return nr_fac
   
start=10
end=100
num=5

random_list_res=randf(start, end, num)
random_list=random_list_res[0]

KK=random_list_res[1]


ordered_list=sorted(random_list)

largest_sub_return=largest_sub(ordered_list,KK)
largest_sub_return_size=len(largest_sub_return)
all_sub_return=all_sub(largest_sub_return)

final_sub_size=0

for x in range(1,largest_sub_return_size): # sum of all sub arrays
    
    final_sub_size+=comb_size(largest_sub_return_size,x)
    

print('initial list = ', random_list,'\n', 'K = ',KK, '\n','List element smaller than K = ',largest_sub_return)
print('final_sub_size =',final_sub_size)  
print('all_sub_lists = ', all_sub_return)





