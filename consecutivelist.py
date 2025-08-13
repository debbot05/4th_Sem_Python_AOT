def consecutive_list(x):
    li=[]
    for i in range(0,10):
        li.append(x)
        x=x+1
        return li

y=int(input("Enter a number:"))
print(consecutive_list(y))