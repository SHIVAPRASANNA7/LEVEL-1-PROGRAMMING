def dictionairy():
         
 key_value ={}   
 

 key_value[2] = 216     
 key_value[1] = 7
 key_value[5] = 78
 key_value[4] = 77
 key_value[6] = 18     
 key_value[3] = 248
 
 print ("Task 1:-\n")
 print ("Keys are")
  
 
 for i in sorted (key_value.keys()) :
     print(i, end = " ")
 
def main():
    
    dictionairy()            
     

if __name__=="__main__":     
    main()
