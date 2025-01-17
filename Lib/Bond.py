
import pandas as pd
from datetime import date, timedelta as td

####################################
#           Bond Class             #
####################################

#@Aim: Represent a short term or a long term bon with specifics criteria
#@Initialize_date: 16-02-2017
#@Updates:  - [18-02-2017]: Added profit attribute to classes ShortTerm and LongTerm
#           - [22-02-2017]: Attributes updates + add compoundedInterest() + Draw a plot for a bond
#           - [23-02-2017]: Add function getMinAmount() + whoIAm()
#           - [25-02-2017]: Use of dataframe instead of list
#           - [27-02-2017]: Clean the code and add comment
#TODO: - Check the minimum Amount and Term


class Bond(object):
    def __init__(self, amount, start_date, end_date):
        self._amount = amount
        self._start_date = start_date
        self._end_date = end_date
        self._mTerm = 0
        self._mAmount = 0
        self._interest = 0

        self.checkValue() # Check the minimum value f


    # @FunctionName: checkValue()
    # @Goal: Check the amount value
    # @Parameters: - self, class instance
    # @Return: None
    def checkValue(self):
        if(self._amount < self._mAmount):
            self._amount = self._mAmount



    # @FunctionName: interestSeriesComplete()
    # @Goal: Return the dataframe for a bond with the interest value
    # @Parameters:  - self, class instance
    # @Return:  A pandas Dataframe with an index and interest column
    def interestSeriesComplete(self):
        Dates = []
        Interest = []

        date_start = str.split(self._start_date, '/')
        date_start = date(int(date_start[2]), int(date_start[1]), int(date_start[0]))

        date_end = str.split(self._end_date, '/')
        date_end = date(int(date_end[2]), int(date_end[1]), int(date_end[0]))

        delta = date_end - date_start
        for i in range(delta.days + 1):
            current_date = date_start + td(days=i)
            Dates.append(current_date)
            Interest.append(self.coumpoundedInterest(i, (1 / 365)))

        seriesI = pd.DataFrame(data= Interest, columns=['Interest'], index=Dates)

        return seriesI

    # @FunctionName: coumpoundedInterest()
    # @Goal:  Compute the coumpounded interest
    # @Parameters: - time, an integer value of the current period
    #              - n, value of the type period (e.g. 1/12, monthly coumpounded)
    # @Return:
    def coumpoundedInterest(self, time, n=1):
        return self._amount * ( 1 + self._interest)**(time * n)



    # GETTER & SETTER

    # @FunctionName: getMinAmount()
    # @Goal:  Get the value of the minimum value required for the bond
    # @Parameters:  Self, class instance
    # @Return:  An integer, amount of the minimum value required
    def getMinAmount(self):
        return self._mAmount

    # @FunctionName: whoIAm()
    # @Goal: Return the name of class type
    # @Parameters: Self, class instance
    # @Return: A string name of the class
    def whoIAm(self):
        return 'bond'

#------

# Short Term Bond, extends Bond

class ShortTerm(Bond):
    def __init__(self, amount, start_date, end_date):
        super(ShortTerm, self).__init__(amount, start_date, end_date)
        self._mTerm = 2          # in years
        self._mAmount = 1000
        self._interest = 0.01


# Long Term Bond, extends Bond

class LongTerm(Bond):
    def __init__(self, amount, start_date, end_date):
        super(LongTerm, self).__init__(amount, start_date, end_date)
        self._mTerm = 5          # in years
        self._mAmount = 3000
        self._interest = 0.03


