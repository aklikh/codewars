def pick_peaks(arr):
    ans = {'pos':[], 'peaks':[]}
       
    if len(arr) <= 2:
         return ans
           
    candidate = None    
    for i in range(1,len(arr)-1):
        if arr[i-1] < arr[i] > arr[i+1]:
            ans['pos'].append(i)
            ans['peaks'].append(arr[i])
            
        elif arr[i-1] < arr[i] and arr[i] == arr[i+1]:
            candidate = i
        
        elif arr[i] > arr[i+1] and candidate != None:
            ans['pos'].append(candidate)
            ans['peaks'].append(arr[candidate])
            candidate = None
            
        elif arr[i] < arr[i+1] and candidate != None:
            candidate = None       
        
    return ans


print(pick_peaks([1,2,5,4,3,2,3,6,4,1,2,3,3,4,5,3,2,1,2,3,5,5,4,3]))
#{"pos":[2,7,14,20], "peaks":[5,6,5,5]}