#Page 56

t1 = ()
t2 = (1, 'two', 3)
print(t1)
print(t2)

t1 = (1, 'two', 3)
t2 = (t1, 3.25)
print(t2)
print((t1 + t2)) # concatenated
print(((t1 + t2)[3]))#indexed 
print(((t1 + t2)[2:5]))#sliced

#Page 57
def findDivisors (n1, n2):
    """Assumes that n1 and n2 are positive ints
       Returns a tuple containing all common divisors of n1 & n2"""
    divisors = () #the empty tuple
    for i in range(1, min (n1, n2) + 1):
        if n1%i == 0 and n2%i == 0:
            divisors = divisors + (i,) # Note：comma-（i,) Tuple
    return divisors

divisors = findDivisors(20, 100)
print(divisors)
total = 0
for d in divisors:
    total += d
print(total)

#Page 58
def findExtremeDivisors(n1, n2):
    """Assumes that n1 and n2 are positive ints
       Returns a tuple containing the smallest common
       divisor > 1 and the largest common divisor of n1
       and n2"""
   
    minVal, maxVal = None, None
    for i in range(2, min(n1, n2) + 1):
        if n1%i == 0 and n2%i == 0:
            if minVal == None or i < minVal:
                minVal = i
            if maxVal == None or i > maxVal:
                maxVal = i
    return (minVal, maxVal)

minDivisor, maxDivisor = findExtremeDivisors(100, 200)  #  return fixed-size sequences
print(('minDivisor=',minDivisor))
print(('maxDivisor=',maxDivisor))

L = ['I did it all', 4, 'love']
for i in range(len(L)):
    print((L[i]))

#Page 59
Techs = ['MIT', 'Caltech'] 
Ivys = ['Harvard', 'Yale', 'Brown']
Univs = [Techs, Ivys]
Univs1 = [['MIT', 'Caltech'], ['Harvard', 'Yale', 'Brown']]
print('Univs =', Univs) 
print('Univs1 =', Univs1)
print(Univs == Univs1)

#Pages 60-62
print(Univs == Univs1) #test value equality
print(id(Univs) == id(Univs1)) #test object equality
print('Id of Univs =', id(Univs))
print('Id of Univs1 =', id(Univs1))

print('Ids of Univs[0] and Univs[1]', id(Univs[0]), id(Univs[1]))
print('Ids of Univs1[0] and Univs1[1]', id(Univs1[0]), id(Univs1[1]))

Techs.append('RPI')

for e in Univs:
    print('Univs contains', e)
    print('  which contains')
    for u in e:
        print('    ', u)

L1 = [1,2,3]
L2 = [4,5,6]
L3 = L1 + L2
print('L3 =', L3)
L1.extend(L2)
print('L1 =', L1)
L1.append(L2)
print('L1 =', L1)

#Page 63-64
def removeDups(L1, L2):
    """Assumes that L1 and L2 are lists.
       Removes any element from L1 that also occurs in L2"""
    for e1 in L1:
        print(len(L1))
        if e1 in L2:
            L1.remove(e1)
L1 = [1,2,3,4]
L2 = [1,2,5,6]
removeDups(L1, L2)
print('L1 =', L1)

L = [x**2 for x in range(1,7)]
print(L)

mixed = [1, 2, 'a', 3, 4.0]
print([x**2 for x in mixed if type(x) == int])

#Page 64, Figure 5.5
from functionsFromChapter4 import *
def applyToEach(L, f):
   """Assumes L is a list, f a function
      Mutates L by replacing each element, e, of L by f(e)"""
   for i in range(len(L)):
      L[i] = f(L[i])
      
L = [1, -2, 3.33]
print('L =', L)
print('Apply abs to each element of L.')
applyToEach(L, abs)
print('L =', L)
print('Apply int to each element of', L)
applyToEach(L, int)
print('L =', L)
print('Apply factorial to each element of', L)
applyToEach(L, factR)
print('L =', L)
print('Apply Fibonnaci to each element of', L)
applyToEach(L, fib)
print('L =', L)

#Page 64
L1 = [1, 28, 36]
L2 = [2, 57, 9]
print(list(map(min, L1, L2)))

#Page 66
evenElems = []
for e in L:
    if e%2 == 0:
        evenElems.append(e)

#Page 67
monthNumbers = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5,
                1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May'}
print(('The third month is ' + monthNumbers[3]))
dist = monthNumbers['Apr'] - monthNumbers['Jan']
print(('Apr and Jan are', dist, 'months apart'))

print(list(monthNumbers.keys()))

#Page 68
keys = []
for e in monthNumbers:
    keys.append(e)
#keys.sort()
print(keys)

#Page 68, Figure 5.9

EtoF = {'bread':'pain', 'wine':'vin', 'with':'avec', 'I':'Je',
        'eat':'mange', 'drink':'bois', 'John':'Jean',
        'friends':'amis', 'and': 'et', 'of':'du','red':'rouge'}
FtoE = {'pain':'bread', 'vin':'wine', 'avec':'with', 'Je':'I',
        'mange':'eat', 'bois':'drink', 'Jean':'John',
        'amis':'friends', 'et':'and', 'du':'of', 'rouge':'red'}
dicts = {'English to French':EtoF, 'French to English':FtoE}

def translateWord(word, dictionary):
    if word in list(dictionary.keys()):
        return dictionary[word]
    elif word != '':
        return '"' + word + '"'
    return word
    
def translate(phrase, dicts, direction):
    UCLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LCLetters = 'abcdefghijklmnopqrstuvwxyz'
    letters = UCLetters + LCLetters
    dictionary = dicts[direction]
    translation = ''
    word = ''
    for c in phrase:
        if c in letters:
            word = word + c
        else:
            translation = (translation
                          + translateWord(word, dictionary) + c)
            word = ''
    return translation + ' ' + translateWord(word, dictionary)

print(translate('I drink good red wine, and eat bread.',
                dicts,'English to French'))
print(translate('Je bois du vin rouge.',
                dicts, 'French to English'))

#Page 69
FtoE['bois'] = 'wood'
print(translate('Je bois du vin rouge.', dicts, 'French to English'))

def keySearch(L, k):
    for elem in L:
        if elem[0] == k:
            return elem[1]
    return None
