#Page 84
test = [1,2,3]
#test[3]

#Page 85
numSuccesses=1
numFailures=2
successFailureRatio = numSuccesses/float(numFailures)
print('The success/failure ratio is', successFailureRatio)
print('Now here')

try:
    successFailureRatio = numSuccesses/float(numFailures)
    print('The success/failure ratio is', successFailureRatio)
except ZeroDivisionError:
    print('No failures so the success/failure ratio is undefined.')
print ('Now here')

val = int(input('Enter an integer: '))
print('The square of the number you entered is', val**2)

#Page 86
while True:
    val = input('Enter an integer: ')
    try:
        val = int(val)
        print('The square of the number you entered is', val**2)
        break #to exit the while loop
    except ValueError:
        print (val, 'is not an integer')


def readInt():
    while True:
        val = input('Enter an integer: ')
        try:
            val = int(val)
            return val
        except ValueError:
            print(val, 'is not an integer')

def readVal(valType, requestMsg, errorMsg):
  while True:
      val = input(requestMsg + ' ')
      try:
          val = valType(val)
          return val
      except ValueError:
          print(val, errorMsg)

val = readVal(int, 'Enter an integer:', 'is not an integer')

#Page 88, Figure 7.1
def getRatios(vect1, vect2):
    """Assumes: vect1 and vect2 are lists of equal length of numbers
       Returns: a list containing the meaningful values of 
             vect1[i]/vect2[i]"""
    ratios = []
    for index in range(len(vect1)):
        try:
            ratios.append(vect1[index]/vect2[index])
        except ZeroDivisionError:
            ratios.append(float('nan')) #nan = Not a Number
        except:
            raise ValueError('getRatios called with bad arguments')
    return ratios

#Page 88
try:
    print(getRatios([1.0,2.0,7.0,6.0], [1.0,2.0,0.0,3.0]))
    print(getRatios([], []))
    print(getRatios([1.0, 2.0], [3.0]))
except ValueError as msg:
    print (msg)

#Page 88, Figure 7.2
def getRatios(vect1, vect2): 
    """Assumes: vect1 and vect2 are lists of equal length of numbers
       Returns: a list containing the meaningful values of 
             vect1[i]/vect2[i]"""
    ratios = []
    if len(vect1) != len(vect2):
        raise ValueError('getRatios called with bad arguments')
    for index in range(len(vect1)):
        vect1Elem = vect1[index]
        vect2Elem = vect2[index]
        if (type(vect1Elem) not in (int, float))\
           or (type(vect2Elem) not in (int, float)):
            raise ValueError('getRatios called with bad arguments')
        if vect2Elem == 0.0:
            ratios.append(float('NaN')) #NaN = Not a Number
        else:
            ratios.append(vect1Elem/vect2Elem)
    return ratios

#Page 90, Figure 7.3
def getGrades(fname):
    try:
        gradesFile = open(fname, 'r') #open file for reading
    except IOError:
        raise ValueError('getGrades could not open ' + fname)
    grades = []
    for line in gradesFile:
        try:
            grades.append(float(line))
        except:
            raise ValueError('Unable to convert line to float')
    return grades
   
try:
   grades = getGrades('quiz1grades.txt')
   grades.sort()
   median = grades[len(grades)//2]
   print('Median grade is', median)
except ValueError as errorMsg:
   print('Whoops.', errorMsg)

