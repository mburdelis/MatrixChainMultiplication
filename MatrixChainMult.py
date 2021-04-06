# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 14:40:24 2021

@author: Mauricio
"""

import itertools

class Solution(object):
    def calcNumComp(self, my_list, my_order):
        temp_list = my_list.copy()
        order = list(my_order)
        num_comp = 0
        #count_loops = 0
        #print("\n Now calculating with permutation:", order)
        #print("my_list is:", my_list)
        #print("temp_list is:", temp_list)
        for i in range(len(order)):
            #print("i is:", i)
            #print("order[i] is:", order[i])
            #order[i] -= count_loops
            #if order[i]<0:
            #    order[i] = 0
            #print("count_loops is:", count_loops)
            #print("now order[i] is:", order[i])
            num_comp += temp_list[order[i]]*temp_list[order[i]+1]*temp_list[order[i]+2]
            #print("num_comp:", num_comp)
            #print("temp_list was:", temp_list)
            temp_list.pop(order[i]+1)
            #print("now temp_list is:", temp_list)
            for j in range(i, len(order)):
                if order[j] > order[i]:
                    order[j] -= 1
            #print("now order is:", order)
            #count_loops += 1
            #print("ended one iteration")
        return num_comp
        
    
    def findMinNumComp(self, my_list):
        self.l = len(my_list)
        self.adjs = [i for i in range(self.l-2)]
        self.perms = list(itertools.permutations(self.adjs))
        if self.l < 3:
            return 0
        self.min = float('inf')
        for p in self.perms:
            num_comp = self.calcNumComp(my_list, p)
            if num_comp < self.min:
                self.min = num_comp
        return self.min
        

test_list = [40, 20, 30, 10, 30]
print(Solution().findMinNumComp(test_list))



