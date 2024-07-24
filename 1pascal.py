def pascal(row):
    
    array_2d = [[0 for _ in range(row*2 +1)] for _ in range(row)]
    print(array_2d)
    array_2d[0][(row*2 +1)//2]=1
    print(array_2d)
    for i in range(0,row-1):
        roww=array_2d[i]
        print(roww)
        for j in range(1,row*2):
            left=roww[j-1]
            right = roww[j+1]
            print("left",left)
            print("right",right)
            array_2d[i+1][j]=(left+right)
            
     
  
            
    
    
    
    print(array_2d)
            
            
        

            
        
        
        
        
        
pascal(3)
