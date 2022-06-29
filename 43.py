

from itertools import groupby
  

test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  
 
print("The original list : " + str(test_list))
  

res = [list(val) for key, val in groupby(sorted(test_list))]  
          
 
print("Matrix after grouping : " + str(res))
