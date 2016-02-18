#Page 126
def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
    return False

#Page 128
def search(L, e):
    """Assumes L is a list, the elements of which are in
          ascending order.
       Returns True if e is in L and False otherwise"""
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e: 
            return False
    return False

#Page 129, Figure 10.2
def search(L, e):
    """Assumes L is a list, the elements of which are in
          ascending order.
       Returns True if e is in L and False otherwise"""
    
    def bSearch(L, e, low, high):
        #Decrements high - low
        if high == low:
            return L[low] == e
        mid = (low + high)//2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid: #nothing left to search
                return False
            else:
                return bSearch(L, e, low, mid - 1)
        else:
            return bSearch(L, e, mid + 1, high)
        
    if len(L) == 0:
        return False
    else:
        return bSearch(L, e, 0, len(L) - 1)

#Page 132, Figure 10.3
def selSort(L):
    """Assumes that L is a list of elements that can be
         compared using >.
       Sorts L in ascending order"""
    suffixStart = 0
    while suffixStart != len(L):
        #look at each element in suffix
        for i in range(suffixStart, len(L)):
            if L[i] < L[suffixStart]:
                #swap position of elements
                L[suffixStart], L[i] = L[i], L[suffixStart]
        suffixStart += 1

#Page 134, Figure 10.4
def merge(left, right, compare):
    """Assumes left and right are sorted lists and
         compare defines an ordering on the elements.
       Returns a new sorted (by compare) list containing the
         same elements as (left + right) would contain."""
    
    result = []
    i,j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result

import operator

def mergeSort(L, compare = operator.lt):
    """Assumes L is a list, compare defines an ordering
         on elements of L
       Returns a new sorted list containing the same elements as L"""
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = mergeSort(L[:middle], compare)
        right = mergeSort(L[middle:], compare)
        return merge(left, right, compare)

#Page 135, Figure 10.5
def lastNameFirstName(name1, name2):
 
    name1 = name1.split(' ')
    name2 = name2.split(' ')
    if name1[1] != name2[1]:
        return name1[1] < name2[1]
    else: #last names the same, sort by first name
        return name1[0] < name2[0]

def firstNameLastName(name1, name2):
    name1 = name1.split()
    name2 = name2.split()
    if name1[0] != name2[0]:
        return name1[0] < name2[0]
    else: #first names the same, sort by last name
        return name1[1] < name2[1]

L = ['Chris Terman', 'Tom Brady', 'Eric Grimson', 'Gisele Bundchen']
newL = mergeSort(L, lastNameFirstName)
print('Sorted by last name =', newL)
newL = mergeSort(L, firstNameLastName)
print('Sorted by first name =', newL)

#Page 136
L = [3,5,2]
D = {'a':12, 'c':5, 'b':'dog'}
print(sorted(L))
print(L)
L.sort()
print(L)
print(sorted(D))
D.sort()

L = [[1,2,3], (3,2,1,0), 'abc']
print sorted(L, key = len, reverse = True)

#Page 139, Figure 10.6
class intDict(object):
    """A dictionary with integer keys"""
    
    def __init__(self, numBuckets):
        """Create an empty dictionary"""
        self.buckets = []
        self.numBuckets = numBuckets
        for i in range(numBuckets):
            self.buckets.append([])
            
    def addEntry(self, dictKey, dictVal):
        """Assumes dictKey an int.  Adds an entry."""
        hashBucket = self.buckets[dictKey%self.numBuckets]
        for i in range(len(hashBucket)):
            if hashBucket[i][0] == dictKey:
                hashBucket[i] = (dictKey, dictVal)
                return
        hashBucket.append((dictKey, dictVal))
        
    def getValue(self, dictKey):
        """Assumes dictKey an int.  Returns entry associated
           with the key dictKey"""
        hashBucket = self.buckets[dictKey%self.numBuckets]
        for e in hashBucket:
            if e[0] == dictKey:
                return e[1]
        return None
    
    def __str__(self):
        result = '{'
        for b in self.buckets:
            for e in b:
                result = result + str(e[0]) + ':' + str(e[1]) + ','
        return result[:-1] + '}' #result[:-1] omits the last comma

#Page 139
import random #a standard library module

D = intDict(29)
random.seed(1)
for i in range(20):
    #choose a random int between 0 and 10**5
    key = random.randint(0, 10**5)
    D.addEntry(key, i)
print('The value of the intDict is:')
print(D)
print('\n', 'The buckets are:')
for hashBucket in D.buckets: #violates abstraction barrier
    print('  ', hashBucket)
