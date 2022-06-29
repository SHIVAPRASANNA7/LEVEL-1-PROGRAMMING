


test_list = [[7, 88, 99], [22, 10, 19], [15, 44, 62], [72, 83, 59]]
  

print("The original list : " + str(test_list))
  

res = {test_list[0][ele] :  test_list[ele + 1] for ele in range(len(test_list) - 1)}
  

print("The Assigned Matrix : " + str(res))
