def merge_array(nums1,nums2,result):
    l=len(nums1)
    r=len(nums2)
    i,j=0,0

    while(i<l and j<r):
        if nums1[i]<nums2[j]:
            if len(result)==0 or nums1[i]!=result[-1]:
                result.append(nums1[i])
            i+=1    
        else: 
            if len(result)==0 or nums2[j]!=result[-1]:
                result.append(nums2[j])
            j+=1    
    while(i<l):
        if len(result)==0 or nums1[i]!=result[-1]:
                result.append(nums1[i])
        i+=1  
    while(j<r):
        if len(result)==0 or nums2[j]!=result[-1]:
                result.append(nums2[j])
        j+=1 

    return result


nums1=[1,1,1,2,4,6,7]
nums2=[1,2,3,6,7,8,9,10]
result=[]

print(merge_array(nums1,nums2,result))

