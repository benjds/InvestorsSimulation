from Lib import Investor
import plotly
import plotly.graph_objs as go
from plotly import tools
import os
import plotly.plotly as py
from Lib import Stock

###########################################
#           Part 4: Simulations           #
###########################################


Numbers_of_investors = 100
Budget = 10000
Years = ['2005','2006','2007','2008','2009','2010','2011','2012','2013','2014']
#Years = ['2005']




### FOR EACH YEAR #####

fig = tools.make_subplots(rows=10, cols=3,
                          print_grid=False,
                          subplot_titles=("Defensive investors","Aggressive investors", "Mixed investors"))

for x in range(0, len(Years)):
    start = '01/01/' + Years[x]
    end = '31/12/' + Years[x]

    defensive_investors = []

    #create the 1000 defensive investor
    for i in range(0,Numbers_of_investors):
        new_Investor = Investor.Defensive_Investor(Budget, start, end)
        new_Investor.invest()
        defensive_investors.append(new_Investor)


    model_defensive_investor_series = Investor.mergeInvestorsSeries_Dataframe(defensive_investors,Numbers_of_investors)

    ####

    aggressive_investors = []

    for j in range(0,Numbers_of_investors):
        new_Investor = Investor.Aggressive_Investor(Budget, start, end)
        new_Investor.invest()
        aggressive_investors.append(new_Investor)


    model_aggressive_investor_series = Investor.mergeInvestorsSeries_Dataframe(aggressive_investors,Numbers_of_investors)

    ####
    mixed_investors = []

    for k in range(0, Numbers_of_investors):
        new_Investor = Investor.Mixed_Investor(Budget, start, end)
        new_Investor.invest()
        mixed_investors.append(new_Investor)

    model_mixed_investor_series = Investor.mergeInvestorsSeries_Dataframe(mixed_investors, Numbers_of_investors)

    #data = []

    #data.append(go.Scatter(y=model_defensive_investor_series['Interest'], x=model_defensive_investor_series.index,
    #                      name='Investor Defensive (' + str(Numbers_of_investors) + ')'))
    #data.append(go.Scatter(y=model_aggressive_investor_series['Interest'], x=model_aggressive_investor_series.index,
    #                       name='Investor Aggressive (' + str(Numbers_of_investors) + ')'))
    #data.append(go.Scatter(y=model_mixed_investor_series['Interest'], x=model_mixed_investor_series.index,
    #                       name='Investor Mixed (' + str(Numbers_of_investors) + ')'))

    fig.append_trace(go.Scatter(y=model_defensive_investor_series['Interest'], x=model_defensive_investor_series.index,
                          name='Investor Defensive (' + str(Numbers_of_investors) + ')'), (x + 1), 1)
    fig.append_trace(go.Scatter(y=model_aggressive_investor_series['Interest'], x=model_aggressive_investor_series.index,
                           name='Investor Aggressive (' + str(Numbers_of_investors) + ')'), (x + 1), 2)
    fig.append_trace(go.Scatter(y=model_mixed_investor_series['Interest'], x=model_mixed_investor_series.index,
                           name='Investor Mixed (' + str(Numbers_of_investors) + ')'), (x + 1), 3)

    #plotpath = os.path.abspath("../Results/Invest_modelling_for_"+Years[x]+".html")

    # Draw the graph
    #fig = go.Figure(data=data)
    #plotly.offline.plot(fig, filename=plotpath)


plotpath = os.path.abspath("../Results/Invest_modelling_by_year.html")
# Draw the graph
plotly.offline.plot(fig, filename=plotpath)
#py.iplot(fig)


### BEST STOCK IN 2007 #####


list_stock = []


Start = '01/01/2007'
End = '31/12/2007'

# Create a list of stock
#AAPL, GOOGL, YHOO, AXP, XOM, KO, NOK, MS, IBM and FDX
list_stock.append(Stock.Stock('GOOGL', 1, Start, End))
list_stock.append(Stock.Stock('AAPL', 1, Start, End))
list_stock.append(Stock.Stock('YHOO', 1, Start, End))
list_stock.append(Stock.Stock('AXP', 1, Start, End))
list_stock.append(Stock.Stock('XOM', 1, Start, End))
list_stock.append(Stock.Stock('KO', 1, Start, End))
list_stock.append(Stock.Stock('NOK', 1, Start, End))
list_stock.append(Stock.Stock('MS', 1, Start, End))
list_stock.append(Stock.Stock('IBM', 1, Start, End))
list_stock.append(Stock.Stock('FDX', 1, Start, End))


ticker = []
value = []

#add stock into a graph object
for i in range(0,9):
    list_stock[i].interestSeriesByTime()
    ticker.append(list_stock[i].sTicker)
    value.append(list_stock[i].periodInterest())


data = [go.Bar( x=ticker, y=value)]
plotpath = os.path.abspath("../Results/2007_stocks.html")

layout = go.Layout(
    title='Best stock in 2007',
)
#Draw the graph
fig = go.Figure(data=data, layout= layout)
plotly.offline.plot(fig, filename=plotpath)


