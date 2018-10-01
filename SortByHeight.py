    minusOne = [ i for i in range(len(a)) if a[i] == -1 ] #-1가 들어가는 곳
    
    sortA = sorted(a) #내림차순 정렬
    
    for i in range(len(sortA)) : #-1제거
        if sortA[0] == -1 :
            del sortA[0]
            
    for j in minusOne : #-1추가
        sortA.insert(j,-1)
            
    return sortA
