def differenceOfPairs(li):
    c = 0
    for i in range(len(li)-1):
        for j in range(i+1,len(li)):
            d=abs(li[i]-li[j])
            if d not in li:
                li.append(d)
                differenceOfPairs(li)
                c=c+1
                
    return li  
def kthLargestofDeiffrencePairs(li,k):
    li2 = differenceOfPairs(li)
    print(li2)
    li2 = sorted(li2,reverse = True)
    highest = li2[k-1]
    print(highest)
kthLargestofDeiffrencePairs([1,9],4)