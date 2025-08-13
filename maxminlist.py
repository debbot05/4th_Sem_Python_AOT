def max_min_list():
    li=list(map(int,input("Enter a list:").split()))
    maxi=max(li)
    mini=min(li)
    max_index=li.index(maxi)
    min_index=li.index(mini)
    return(maxi,max_index,mini,min_index)
    
ans=max_min_list()
print("The maximum element is:",ans[0],"and its index is:",ans[1])
print("The minimum element is:",ans[2],"and its index is:",ans[3])
