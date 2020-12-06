#LAB 11
#Due Date: 11/22/2019, 11:59PM
########################################
#
# Name: Aaron
# Collaboration Statement: Divyesh
#
########################################


def selectionSort(numList):
    '''
        Takes a list and returns 2 values
        1st returned value: a dictionary with the state of the list after each complete pass of selection sort
        2nd returned value: the sorted list

        >>> selectionSort([9,3,5,4,1,78,67])
        ({1: [9, 3, 5, 4, 1, 78, 67], 2: [1, 3, 5, 4, 9, 78, 67], 3: [1, 3, 5, 4, 9, 78, 67], 4: [1, 3, 4, 5, 9, 78, 67], 5: [1, 3, 4, 5, 9, 78, 67], 6: [1, 3, 4, 5, 9, 78, 67], 7: [1, 3, 4, 5, 9, 67, 78]}, [1, 3, 4, 5, 9, 67, 78])
    '''
    # YOUR CODE STARTS HERE
    thedict={}
    for i in range(0,len(numList)-1):
        minIndex=i#0=9
        for x in range (i+1,len(numList)):
            if numList[x]<numList[minIndex]:
                minIndex=x
        thedict[i+1]=list(numList)
        if minIndex!=i:
            numList[minIndex],numList[i]=numList[i],numList[minIndex]
    thedict[len(numList)]=list(numList)
    return thedict,numList





'thedict[i] = numList'
