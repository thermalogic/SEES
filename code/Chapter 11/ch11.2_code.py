import pylab

#Following function is defined in Chapter 8, and used here
def findPayment(loan, r, m):
    """Assumes: loan and r are floats, m an int
       Returns the monthly payment for a mortgage of size
       loan at a monthly rate of r for m months"""
    return loan*((r*(1+r)**m)/((1+r)**m - 1))

#Page 147, Figure 11.1
class Mortgage(object):
    """Abstract class for building different kinds of mortgages"""
    
    def __init__(self, loan, annRate, months):
        """Create a new mortgage"""
        self.loan = loan
        self.rate = annRate/12.0
        self.months = months
        self.paid = [0.0] 
        self.owed = [loan]
        self.payment = findPayment(loan, self.rate, months)
        self.legend = None #description of mortgage
        
    def makePayment(self):
        """Make a payment"""
        self.paid.append(self.payment)
        reduction = self.payment - self.owed[-1]*self.rate
        self.owed.append(self.owed[-1] - reduction)
        
    def getTotalPaid(self):
        """Return the total amount paid so far"""
        return sum(self.paid)
    
    def __str__(self):
        return self.legend

    def plotPayments(self, style):
        pylab.plot(self.paid[1:], style, label = self.legend)
    
    def plotBalance(self, style):
        pylab.plot(self.owed, style, label = self.legend)
        
    def plotTotPd(self, style):
        """Plot the cumulative total of the payments made"""
        totPd = [self.paid[0]]
        for i in range(1, len(self.paid)):
            totPd.append(totPd[-1] + self.paid[i])
        pylab.plot(totPd, style, label = self.legend)
    
    def plotNet(self, style):
        """Plot an approximation to the total cost of the mortgage
           over time by plotting the cash expended minus the equity
           acquired by paying off part of the loan"""
        totPd = [self.paid[0]]
        for i in range(1, len(self.paid)):
            totPd.append(totPd[-1] + self.paid[i])
        #Equity acquired through payments is amount of original loan
        #  paid to date, which is amount of loan minus what is still owed
        equityAcquired = pylab.array([self.loan]*len(self.owed))
        equityAcquired = equityAcquired - pylab.array(self.owed)
        net = pylab.array(totPd) - equityAcquired
        pylab.plot(net, style, label = self.legend)

#Page 149, Figure 11.2
class Fixed(Mortgage):
    def __init__(self, loan, r, months):
        Mortgage.__init__(self, loan, r, months)
        self.legend = 'Fixed, ' + str(r*100) + '%' 

class FixedWithPts(Mortgage):
    def __init__(self, loan, r, months, pts):
        Mortgage.__init__(self, loan, r, months)
        self.pts = pts
        self.paid = [loan*(pts/100.0)]
        self.legend =('Fixed, ' + str(r*100) + '%, '
                   + str(pts) + ' points')

class TwoRate(Mortgage):
    def __init__(self, loan, r, months, teaserRate, teaserMonths):
        Mortgage.__init__(self, loan, teaserRate, months)
        self.teaserMonths = teaserMonths
        self.teaserRate = teaserRate
        self.nextRate = r/12.0
        self.legend = (str(teaserRate*100)
                      + '% for ' + str(self.teaserMonths)
                      + ' months, then ' + str(r*100) + '%')

    def makePayment(self):
        if len(self.paid) == self.teaserMonths + 1:
            self.rate = self.nextRate
            self.payment = findPayment(self.owed[-1], self.rate,
                                       self.months - self.teaserMonths)
        Mortgage.makePayment(self)

#Page 150, Figure 11.3
def plotMortgages(morts, amt):
    styles = ['b-', 'b-.', 'b:']
    #Give names to figure numbers
    payments = 0
    cost = 1
    balance = 2
    netCost = 3
  
    pylab.figure(payments)
    pylab.title('Monthly Payments of Different $' + str(amt)
                + ' Mortgages')
    pylab.xlabel('Months')
    pylab.ylabel('Monthly Payments')
    pylab.figure(cost)
    pylab.title('Cash Outlay of Different $' + str(amt) + ' Mortgages')
    pylab.xlabel('Months')
    pylab.ylabel('Total Payments')
    pylab.figure(balance)
    pylab.title('Balance Remaining of $' + str(amt) + ' Mortgages')
    pylab.xlabel('Months')
    pylab.ylabel('Remaining Loan Balance of $')
    pylab.figure(netCost)
    pylab.title('Net Cost of $' + str(amt) + ' Mortgages')
    pylab.xlabel('Months')
    pylab.ylabel('Payments - Equity $')

    for i in range(len(morts)):
        pylab.figure(payments)
        morts[i].plotPayments(styles[i])
        pylab.figure(cost)
        morts[i].plotTotPd(styles[i])
        pylab.figure(balance)
        morts[i].plotBalance(styles[i])
        pylab.figure(netCost)
        morts[i].plotNet(styles[i])
        
    pylab.figure(payments)
    pylab.legend(loc = 'upper center')
    pylab.figure(cost)
    pylab.legend(loc = 'best')
    pylab.figure(balance)
    pylab.legend(loc = 'best')

    pylab.show()
  
def compareMortgages(amt, years, fixedRate, pts, ptsRate,
                    varRate1, varRate2, varMonths):
    totMonths = years*12
    fixed1 = Fixed(amt, fixedRate, totMonths)
    fixed2 = FixedWithPts(amt, ptsRate, totMonths, pts)
    twoRate = TwoRate(amt, varRate2, totMonths, varRate1, varMonths)
    morts = [fixed1, fixed2, twoRate]
    for m in range(totMonths):
        for mort in morts:
            mort.makePayment()
  
    plotMortgages(morts, amt)

#Page 150
compareMortgages(amt=200000, years=30, fixedRate=0.07,
                 pts = 3.25, ptsRate=0.05,
                 varRate1=0.045, varRate2=0.095, varMonths=48)
