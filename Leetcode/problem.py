def twoSums(nums,target):
    x = nums
    for i in range(0,len(x)):
        for j in range(0,len(nums)):
            #x[i] will stay x[0] until all interations have gone
            
            if x[i] == nums[j] and i == j:
                j = j + 1
            elif x[i] != nums[j]:
                if x[i]+nums[j] == target:
                    return i,j
            elif(x[i]==x[j]):
                if x[i]+nums[j] == target:
                    return i,j



print(twoSums([2,7,11,15],9))
print(twoSums([3,2,4],6))
print(twoSums([3,3],6))


