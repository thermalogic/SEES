import matplotlib.pyplot as plt
import numpy as np

#Page 224, Figure 16.1
def plotHousing(impression):
    """Assumes impression a str.  Must be one of 'flat',
         'volatile,' and 'fair'
       Produce bar chart of housing prices over time"""
    f = open('midWestHousingPrices.txt', 'r')
    #Each line of file contains year quarter price
    #for Midwest region of U.S.
    labels, prices = ([], [])
    for line in f:
        year, quarter, price = line.split()
        label = year[2:4] + '\n Q' + quarter[1]
        labels.append(label)
        prices.append(float(price)/1000)
    quarters = np.arange(len(labels)) #x coords of bars
    width = 0.8 #Width of bars
    if impression == 'flat':
        plt.semilogy()
    plt.bar(quarters, prices, width)
    plt.xticks(quarters+width/2.0, labels)
    plt.title('Housing Prices in U.S. Midwest')
    plt.xlabel('Quarter')
    plt.ylabel('Average Price ($1,000\'s)')
    if impression == 'flat':
        plt.ylim(10, 10**3)
    elif impression == 'volatile':
        plt.ylim(180, 220)
    elif impression == 'fair':
        plt.ylim(150, 250)
    else:
        raise ValueError

plotHousing('flat')
plt.figure()
plotHousing('volatile')
plt.figure()
plotHousing('fair')
plt.show()

