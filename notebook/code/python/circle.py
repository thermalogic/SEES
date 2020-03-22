
pi = 3.14159  # executable statements 

def area(radius):  # function definitions.
    return pi*(radius**2)

def circumference(radius):
    return 2*pi*radius

if __name__ == '__main__':
   # execute only if run as a script
   print(area(3.2))
