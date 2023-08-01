import datetime as dt
import os
import numpy as np
import pandas as pd
import copy
import matplotlib.pyplot as plt
from util import get_data, plot_data

def author():
	return 'yqiu322'


def normal_dat(df):
	return df / df.iloc[0, :]


def get_graph(opt, ben):
	fig, ax = plt.subplots(figsize=(10, 8))
	ax.plot(normal_dat(opt), color='red')
	ax.plot(normal_dat(ben), color='blue')
	ax.tick_params(axis='x', rotation=20)
	plt.xlabel("Date")
	plt.ylabel("Normalized Portfolio Values")
	plt.legend(['Optimal Strategy', "Benchmark"])
	plt.title("Theoretically Optimal Strategy vs Benchmark Strategy")
	plt.savefig("tos.png")


def analyze(dt1, dt2):
    df1 = normal_dat(dt1)
    end1 = df1.iloc[-1][0]
    first1 = df1.iloc[0][0]
    c1 = (end1/ first1) - 1

    df2 = normal_dat(dt2)
    end2 = df2.iloc[-1][0]
    first2 = df2.iloc[0][0]
    c2 = (end2 / first2) - 1

    print('cumulative return')
    print(c1, c2)
    dr1 = df1.pct_change(1)
    dr2 = df2.pct_change(1)
    std1 = dr1.std()
    std2 = dr2.std()
    print('standard deviation')
    print(std1, std2)
    mean1 = dr1.mean()
    mean2 = dr2.mean()
    print('mean')
    print(mean1, mean2)

def buy_stock(stock, num_shares, act_dict, date, impact, commission) -> dict:
    stock_price = get_stock(stock, date)
    cost = stock_price * num_shares * (1 + impact)
    act_dict['cash'] -= cost + commission
    if stock in act_dict:
        act_dict[stock] = act_dict[stock] + num_shares
    else:
        act_dict[stock] = num_shares
    return act_dict


def sell_stock(stock, num_shares, act_dict, date, impact, commission) -> dict:
    stock_price = get_stock(stock, date)
    cost = stock_price * num_shares * (1 - impact)
    act_dict['cash'] += cost - commission
    if stock in act_dict:
        act_dict[stock] = act_dict[stock] - num_shares
    else:
        act_dict[stock] = (-1) * num_shares
    return act_dict


def get_stock(stock, date) -> float:
    temp_dates = pd.date_range(date, date)
    adj_close = get_data([stock], temp_dates, False)
    adj_dat = adj_close.loc[date][0]
    return  adj_dat


def get_act_value(act_dict, date) -> float:
    val = 0
    for i in act_dict:
        if i == 'cash':
            val = val + act_dict[i]
        else:
            stock_price = get_stock(i, date)
            val = val + act_dict[i] * stock_price
    return val





def is_trading_day(date) -> bool:
    return not pd.isna(get_stock('$SPX', date))


def compute_port(orders_dat, start_date, end_date, stock="JPM", start_val=1000000, commission=9.95, impact=0.005):
    dates = pd.date_range(start_date, end_date)
    portfolios = pd.DataFrame(index=dates)
    leng_earray = len(portfolios)
    empty_array = np.zeros(leng_earray)
    zero_dat = pd.DataFrame(empty_array)
    portfolios= portfolios.join(zero_dat)
    dfSPY = get_data(['$SPX'], dates, False, colname='Adj Close')
    dfSPY = dfSPY.dropna()

    portfolios = portfolios.join(dfSPY, how='inner')
    portfolios = portfolios.drop(columns=['$SPX'])

    act = {'cash': start_val}
    portfolio_stocks = {start_date: act}

    for index, row in orders_dat.iterrows():

        order = row[0]
        num_shares = abs(order)
        date = index
        sell = order < 0
        buy = order > 0


        if sell:
            account = sell_stock(stock, num_shares, act, date, impact, commission)
            value = get_act_value(account, date)
            portfolios.loc[date][0] = value
            portfolio_stocks[date] = copy.deepcopy(account)

        elif buy:
            account = buy_stock(stock, num_shares, act, date, impact, commission)
            value = get_act_value(account, date)
            portfolios.loc[date][0] = value
            portfolio_stocks[date] = copy.deepcopy(account)

    cur_portfolio = {'cash': start_val}
    for j in portfolios.index:
        value = portfolios.loc[j][0]

        if pd.isna(value) and is_trading_day(j):
            val = get_act_value(cur_portfolio, j)
            portfolios.loc[j][0] = val
        else:
            cur_portfolio = portfolio_stocks[j]

    return portfolios

def testPolicy(symbol="JPM", sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009, 12, 31), sv=100000):
    commission = 0
    impact = 0
    dates = pd.date_range(sd, ed)
    dfPrice = get_data([symbol], dates, True, colname='Adj Close').drop(columns=['SPY'])
    dfPrice.sort_index()
    df_Trades = dfPrice.copy()
    upp = df_Trades.shift(-1) - df_Trades
    low = abs(df_Trades.shift(-1) - df_Trades)
    dfTrades = (upp/low) * 1000
    dfTrades = dfTrades.fillna(0)
    Past_dfTrades = (dfTrades.shift(1)).fillna(0)
    opt_ord = dfTrades - Past_dfTrades
    benchmark_ord = 0 * opt_ord
    benchmark_ord.iloc[0][0] = 1000
    optimal_portfolio = compute_port(opt_ord, sd, ed, symbol, sv, commission, impact)
    benchmark_portfolio = compute_port(benchmark_ord, sd, ed, symbol, sv, commission, impact)
    get_graph(optimal_portfolio, benchmark_portfolio)
    analyze(optimal_portfolio, benchmark_portfolio)
    return opt_ord



if __name__ == "__main__":

	df_trades = testPolicy()