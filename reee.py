lst1=[1,3,5,8]
lst2=[2,4,6,7]

def sort(lst1,lst2):
     if len(lst1)==1:
         if lst1[0]<=lst2[0]:
              return [lst1[0]]+[lst2[0]]
         else:
              return [lst2[0]]+[lst1[0]]

     else:
         if lst1[0]<=lst2[0]:
             return [lst1[0]]+[lst2[0]]+ sort(lst1[1:],lst2[1:])

         if lst1[0]>=lst2[0]:
             return [lst2[0]]+[lst1[0]]+sort(lst1[1:],lst2[1:])
print(sort(lst1,lst2))
