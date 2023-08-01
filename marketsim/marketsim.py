""""""  		  	   		  	  		  		  		    	 		 		   		 		  
"""MC2-P1: Market simulator.  		  	   		  	  		  		  		    	 		 		   		 		  
  		  	   		  	  		  		  		    	 		 		   		 		  
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		  	  		  		  		    	 		 		   		 		  
Atlanta, Georgia 30332  		  	   		  	  		  		  		    	 		 		   		 		  
All Rights Reserved  		  	   		  	  		  		  		    	 		 		   		 		  
  		  	   		  	  		  		  		    	 		 		   		 		  
Template code for CS 4646/7646  		  	   		  	  		  		  		    	 		 		   		 		  
  		  	   		  	  		  		  		    	 		 		   		 		  
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		  	  		  		  		    	 		 		   		 		  
works, including solutions to the projects assigned in this course. Students  		  	   		  	  		  		  		    	 		 		   		 		  
and other users of this template code are advised not to share it with others  		  	   		  	  		  		  		    	 		 		   		 		  
or to make it available on publicly viewable websites including repositories  		  	   		  	  		  		  		    	 		 		   		 		  
such as github and gitlab.  This copyright statement should not be removed  		  	   		  	  		  		  		    	 		 		   		 		  
or edited.  		  	   		  	  		  		  		    	 		 		   		 		  
  		  	   		  	  		  		  		    	 		 		   		 		  
We do grant permission to share solutions privately with non-students such  		  	   		  	  		  		  		    	 		 		   		 		  
as potential employers. However, sharing with other current or future  		  	   		  	  		  		  		    	 		 		   		 		  
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		  	  		  		  		    	 		 		   		 		  
GT honor code violation.  		  	   		  	  		  		  		    	 		 		   		 		  
  		  	   		  	  		  		  		    	 		 		   		 		  
-----do not edit anything above this line---  		  	   		  	  		  		  		    	 		 		   		 		  
  		  	   		  	  		  		  		    	 		 		   		 		  
Student Name: Yingjie Qiu (replace with your name)  		  	   		  	  		  		  		    	 		 		   		 		  
GT User ID: yqiu322 (replace with your User ID)  		  	   		  	  		  		  		    	 		 		   		 		  
GT ID: 900897987 (replace with your GT ID)  		  	   		  	  		  		  		    	 		 		   		 		  
"""  		  	   		  	  		  		  		    	 		 		   		 		  
  		  	   		  	  		  		  		    	 		 		   		 		  
import datetime as dt  		  	   		  	  		  		  		    	 		 		   		 		  
import os  		  	   		  	  		  		  		    	 		 		   		 		  
  		  	   		  	  		  		  		    	 		 		   		 		  
import numpy as np  		  	   		  	  		  		  		    	 		 		   		 		  
  		  	   		  	  		  		  		    	 		 		   		 		  
import pandas as pd  		  	   		  	  		  		  		    	 		 		   		 		  
from util import get_data, plot_data  		  	   		  	  		  		  		    	 		 		   		 		  
  		  	   		  	  		  		  		    	 		 		   		 		  
  		  	   		  	  		  		  		    	 		 		   		 		  
def update (sym,ord,sha,money_curr,own_share,sym_t,date_c,end_date, com, imp):
    if sym not in sym_t:
        sym_dat = get_data([sym],pd.date_range(date_c,end_date),addSPY=True, colname='Adj Close')
        sym_dat = sym_dat.ffill()
        sym_dat = sym_dat.bfill()
        sym_t[sym] = sym_dat

    if ord == 'SELL':
        ch_share = -sha
        ch_money = sym_t[sym].loc[date_c].loc[sym]
        ch_money = ch_money * (1 - imp) * sha
    elif ord == 'BUY':
        ch_share = sha
        ch_money = -sym_t[sym].loc[date_c].loc[sym]
        ch_money = ch_money * (1 + imp) * sha

    own_share[sym] = own_share.get(sym,0) + ch_share
    money_curr = money_curr + ch_money - com
    return  money_curr, own_share, sym_t






def compute_portvals(
    orders_file="./orders/orders.csv",  		  	   		  	  		  		  		    	 		 		   		 		  
    start_val=1000000,  		  	   		  	  		  		  		    	 		 		   		 		  
    commission=9.95,  		  	   		  	  		  		  		    	 		 		   		 		  
    impact=0.005,  		  	   		  	  		  		  		    	 		 		   		 		  
):  		  	   		  	  		  		  		    	 		 		   		 		  
    """  		  	   		  	  		  		  		    	 		 		   		 		  
    Computes the portfolio values.  		  	   		  	  		  		  		    	 		 		   		 		  
  		  	   		  	  		  		  		    	 		 		   		 		  
    :param orders_file: Path of the order file or the file object  		  	   		  	  		  		  		    	 		 		   		 		  
    :type orders_file: str or file object  		  	   		  	  		  		  		    	 		 		   		 		  
    :param start_val: The starting value of the portfolio  		  	   		  	  		  		  		    	 		 		   		 		  
    :type start_val: int  		  	   		  	  		  		  		    	 		 		   		 		  
    :param commission: The fixed amount in dollars charged for each transaction (both entry and exit)  		  	   		  	  		  		  		    	 		 		   		 		  
    :type commission: float  		  	   		  	  		  		  		    	 		 		   		 		  
    :param impact: The amount the price moves against the trader compared to the historical data at each transaction  		  	   		  	  		  		  		    	 		 		   		 		  
    :type impact: float  		  	   		  	  		  		  		    	 		 		   		 		  
    :return: the result (portvals) as a single-column dataframe, containing the value of the portfolio for each trading day in the first column from start_date to end_date, inclusive.  		  	   		  	  		  		  		    	 		 		   		 		  
    :rtype: pandas.DataFrame  		  	   		  	  		  		  		    	 		 		   		 		  
    """  		  	   		  	  		  		  		    	 		 		   		 		  
    # this is the function the autograder will call to test your code  		  	   		  	  		  		  		    	 		 		   		 		  
    # NOTE: orders_file may be a string, or it may be a file object. Your  		  	   		  	  		  		  		    	 		 		   		 		  
    # code should work correctly with either input  		  	   		  	  		  		  		    	 		 		   		 		  
    # TODO: Your code here
    ### read data
    dat = pd.read_csv(orders_file, index_col='Date', parse_dates=True, na_values=['nan'])
    order_date = dat.index
    start_date = dat.index[0]
    end_date = dat.index [-1]
    price = get_data(['SPY'], pd.date_range(start_date, end_date), addSPY=True, colname = 'Adj Close')
    prices = price.rename(columns={'SPY': 'value'})
    money_curr = start_val
    own_share = {}
    sym_t = {}
    dates = prices.index
    for i in dates:
        if i in order_date:
            index = dat.loc[i]
            if isinstance(index,pd.DataFrame):
                for _, each in index.iterrows():
                    ord = each.loc['Order']
                    sha = each.loc['Shares']
                    sym = each.loc['Symbol']
                    money_curr, own_share, sym_t = update(sym,ord,sha,money_curr,own_share,sym_t,i,end_date,commission,impact)
            else:
                sym = index.loc['Symbol']
                ord = index.loc['Order']
                sha = index.loc['Shares']
                money_curr, own_share, sym_t = update(sym,ord,sha,money_curr,own_share,sym_t,i,end_date,commission,impact)
        share_in = 0
        for j in own_share:
            share_in = share_in + sym_t[j].loc[i].loc[j]*own_share[j]
        prices.loc[i].loc['value'] = money_curr+share_in

    return prices



  		  	   		  	  		  		  		    	 		 		   		 		  
def test_code():  		  	   		  	  		  		  		    	 		 		   		 		  
    """  		  	   		  	  		  		  		    	 		 		   		 		  
    Helper function to test code  		  	   		  	  		  		  		    	 		 		   		 		  
    """  		  	   		  	  		  		  		    	 		 		   		 		  
    # this is a helper function you can use to test your code  		  	   		  	  		  		  		    	 		 		   		 		  
    # note that during autograding his function will not be called.  		  	   		  	  		  		  		    	 		 		   		 		  
    # Define input parameters  		  	   		  	  		  		  		    	 		 		   		 		  
  		  	   		  	  		  		  		    	 		 		   		 		  
    of = "./orders/orders-02.csv"
    sv = 1000000  		  	   		  	  		  		  		    	 		 		   		 		  
  		  	   		  	  		  		  		    	 		 		   		 		  
    # Process orders  		  	   		  	  		  		  		    	 		 		   		 		  
    portvals = compute_portvals(orders_file=of, start_val=sv)  		  	   		  	  		  		  		    	 		 		   		 		  
    if isinstance(portvals, pd.DataFrame):  		  	   		  	  		  		  		    	 		 		   		 		  
        portvals = portvals[portvals.columns[0]]  # just get the first column  		  	   		  	  		  		  		    	 		 		   		 		  
    else:  		  	   		  	  		  		  		    	 		 		   		 		  
        "warning, code did not return a DataFrame"  		  	   		  	  		  		  		    	 		 		   		 		  


def author():
  return 'yqiu322'
  		  	   		  	  		  		  		    	 		 		   		 		  
if __name__ == "__main__":  		  	   		  	  		  		  		    	 		 		   		 		  
    test_code()  		  	   		  	  		  		  		    	 		 		   		 		  
