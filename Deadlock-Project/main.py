from operator import add

def detect(process, allocation, request, work):
	    
        length = len(process)
        temp_list = []
        check = [False] * length
       
        for i in range(length):       
                if all([work[idx] >= request[i][idx] for idx in range(len(work))]):
                    work = work[0] + allocation[i][0], work[1] + allocation[i][1], work[2] + allocation[i][2]
                    check[i] = True
                else:
                    temp_list.append(i)
                        
        for i in temp_list:
            if all([work[idx] >= request[i][idx] for idx in range(len(work))]):
                work = work[0] + allocation[i][0], work[1] + allocation[i][1], work[2] + allocation[i][2]
                check[i] = True
		temp_list.remove(i)
	
	print("#"*50 + "\n\n")   
        if not temp_list:
	  print("System is not in the deadlock state") 
	  print("\n\n" + "#"*50) 
        else:
	  print("the system is in the deadlock state ")
          print("The Processes in the deadlock are : ")
	  
	  for i in temp_list:
            print(f"Process {process[i]}")
	print("\n\n" + "#"*50)   
            
if __name__=='__main__':
    
    process=[0, 1, 2, 3, 4]
    allocation=[[0, 1, 0], [2, 0, 0], [3, 0, 3], [2, 1, 1], [0, 0, 2]]
    request=[[0, 0, 0], [2, 0, 2], [0, 0, 0], [1, 0, 0], [0, 0, 2]]
    available=[0, 0, 0]
    
    detect(process, allocation, request, available)
  
