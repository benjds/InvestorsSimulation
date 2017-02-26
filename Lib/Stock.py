import pandas_datareader.data as web
import datetime
from matplotlib import style
import matplotlib.pyplot as plt


####################################
#           Stock Class            #
####################################

#@Aim: Represent a stock on a market
#@Initialize_date: 16-02-2017
#@Updates:      - [22-02-2017] : Manage the datas get back and draw plot
#               - [23-02-2017]: add functions => selectDayPrice(), maxStockAvailable(), amountInvest(), setNumberB()
#               - [25-02-2017]: load the data just once
#               - [25-02-2017]: Optimize the dataframe managing



start = datetime.datetime(2005, 1, 1)
end = datetime.datetime(2016, 1, 1)

options = {'AAPL' : web.DataReader('AAPL', 'google', start, end),
           'GOOGL' : web.DataReader('GOOGL', 'google', start, end),
           'YHOO' : web.DataReader('YHOO', 'google', start, end),
           'AXP' : web.DataReader('AXP', 'google', start, end),
           'XOM' : web.DataReader('XOM', 'google', start, end),
           'KO' : web.DataReader('KO', 'google', start, end),
           'NOK' : web.DataReader('NOK', 'google', start, end),
           'MS' : web.DataReader('MS', 'google', start, end),
           'IBM' : web.DataReader('IBM', 'google', start, end),
           'FDX' : web.DataReader('FDX', 'google', start, end)
}

print("Stock data imported !")

class Stock(object):

    def __init__(self, ticker, numberB, startDate, endDate):
        self.sTicker = ticker           # Stock Name, ex: GOOGL
        self.sNumberB = numberB         # Number of stocks bought
        self.sStartDate = startDate     # Date when they bought the stock
        self.sEndDate = endDate

        self.sDate = str.split(startDate,'/')
        self.eDate = str.split(endDate, '/')

        self.start = datetime.datetime(int(self.sDate[2]), int(self.sDate[1]), int(self.sDate[0]))
        self.end = datetime.datetime(int(self.eDate[2]), int(self.eDate[1]), int(self.eDate[0]))

        #self.data = web.DataReader(ticker, 'google', self.start, self.end)
        self.data = options[ticker]
        self.data = self.data.truncate(self.start, self.end)


    def whoIAm(self):
        return 'stock'



    def plotStock(self):
        style.use('fivethirtyeight')
        self.data['High'].plot()
        plt.show()


    def selectDayPrice(self):
        return (self.data.loc[self.data.index[0], 'High'])



    def maxStockAvailable(self, budget):
        #First find price
        #dayPrice = self.data.ix[self.sDate[2] + '-' + self.sDate[1] + '-' + self.sDate[0]]['Close']
        dayPrice = self.selectDayPrice()
        #print('day price = '+ str(dayPrice))

        return int(budget/dayPrice)


    def amountInvest(self):
        return self.sNumberB * self.selectDayPrice()

    def interestSeriesByTime(self):

        self.data['Interest'] = self.data['High'] * self.sNumberB

    def setNumberB(self, value):
        self.sNumberB = value

    def interestSeriesComplete(self):
        return self.data