


lst=[1,3,-2,-5,-1]
def neg(lst):
    if len(lst)==1:
        return lst
        # if lst[0]<1:
        #     return [lst[0]]
        # else:
        #     return
    else:
        if lst[0]<0:
            return [lst[0]] + neg(lst[1:])
        if lst[0]>0:
            return neg(lst[1:])







def sumlist(lst):
    if len(lst)==1:
        return lst[0]
    else:
        return lst[0]+sumlist(lst[1:])
print(sumlist([1,2,3,4,5]))
print(neg(lst))
