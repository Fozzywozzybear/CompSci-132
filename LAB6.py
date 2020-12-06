#Lab #6
#Due Date: 10/04/2019, 11:59PM
########################################
#
# Name: Aaron Fosmire
# Collaboration Statement:
#
########################################


## ALL FUNCTIONS MUST BE RECURSIVE IN ORDER TO GET CREDIT FOR THEM


def mulBy(num):
    '''
        >>> mulBy(5)
        15
        >>> mulBy(8)
        384
        >>> mulBy(0)
        0
        >>> mulBy(1)
        1
    '''
    # --- Your code starts here
    if num <= 2:
        return num
    else:
        return num*mulBy(num-2)



def flat(aList):
    '''
        >>> x = [3, [[5, 2]], 6, [4]]
        >>> flat(x)
        [3, 5, 2, 6, 4]
        >>> x
        [3, [[5, 2]], 6, [4]]
        >>> flat([1, 2, 3])
        [1, 2, 3]
        >>> flat([1, [], 3])
        [1, 3]
    '''
    # --- Your code starts here

    if aList==[]:
        return aList
    if isinstance(aList[0],list):#Used to check if element 0(first place in the list) in the list is a list
        return flat(aList[0])+flat(aList[1:])#Moves the values to the right of the list into the list
    return aList[:1]+flat(aList[1:])#If the value is not a list ([])Adds the values of the lists together to make the new list




def isPrime(num,factor=2):
    '''
        >>> isPrime(5)
        True
        >>> isPrime(1)
        False
        >>> isPrime(0)
        False
        >>> isPrime(85)
        False
        >>> isPrime(1019)
        True
        >>> isPrime(2654)
        False
    '''
    # --- Your code starts here
    if num<=1:
        return False
    if num == 2:
        return True
    if num%factor==0:#simple check if it is even
        return False
    if factor > num//2:#checks to see if factor is greater then half the value as this is the limit.
        return True
    return isPrime(num,factor+1)








def countPrimes(num):#I is used as a counter to see how many primes are in the number given. The one is based of if the value is greater than 2
    '''
        >>> countPrimes(0)
        0
        >>> countPrimes(6)
        3
        >>> countPrimes(2)
        1
        >>> countPrimes(60)
        17
        >>> countPrimes(100)
        25
        >>> countPrimes(500)
        95
    '''
    # --- Your code starts here
    if num == 0:#if num is 0 return 0 not I
        return 0
    if num ==1:
        return 0#adds up all the 0 and 1 for the number given.
    if isPrime(num)==True:
        return countPrimes(num-1) + 1#Returns +1 if the vlaue of the num is prime
    return countPrimes(num-1)#Returns +0 if the value is not primes
