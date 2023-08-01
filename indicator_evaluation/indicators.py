import datetime as dt

import pandas as pd

import matplotlib.pyplot as plt
from util import get_data, plot_data


def author():
    return 'yqiu322'

def get_sma(df, lookback):
    sma = df.rolling(window=lookback, min_periods=lookback).mean()
    return sma

def get_price_per_sma(df, sma):
    return df / sma

def get_momentum(df, lookback):
    return df.pct_change(lookback)

def get_ema(df, lookback):
    return df.ewm(span=lookback).mean()

def get_BB(df, lookback, sma, std):
    top_band = sma + (2 * std)
    bottom_band = sma - (2 * std)
    return (df - bottom_band) / (top_band - bottom_band), top_band, bottom_band

def get_std(df, lookback):
    return df.rolling(window=lookback, min_periods=lookback).std()


def get_macd(df,sd):
    ema_12 = df.ewm(span=12, adjust=False).mean()
    ema_26 = df.ewm(span=26, adjust=False).mean()
    macd_raw = ema_12 - ema_26
    macd_signal = macd_raw.ewm(span=9, adjust=False).mean()
    macd_raw = macd_raw.truncate(before=sd)
    macd_signal = macd_signal.truncate(before=sd)
    return macd_raw, macd_signal


def plot_macd(macd_raw, macd_signal):
    fig, ax = plt.subplots(figsize=(8, 6))
    plt.suptitle("MACD")
    ax.plot(macd_raw, label="MACD", color="orange")
    ax.plot(macd_signal, label="MACD Signal", color="red")
    plt.xlabel("Date")
    ax.legend()
    fig.autofmt_xdate()
    plt.savefig("macd.png")




def plot_BB(df, top, bottom):
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(top, color='red')
    ax.plot(bottom, color='green')
    ax.plot(df, color='blue')
    ax.tick_params(axis='x', rotation=20)
    plt.xlabel("Date")
    plt.ylabel("Normalized Price")
    plt.legend(["Upper Band", "Lower Band", "Price"])
    plt.title("Normalized Stock Price vs Date with Bollinger Bands")
    plt.savefig("bollinger.png")

def plot_sma(df, sma, sma_per_price):
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(df, color='blue', alpha=0.8)
    ax.plot(sma, color='red')
    ax.plot(sma_per_price, color='darkgreen', alpha=0.7)
    ax.tick_params(axis='x', rotation=20)
    plt.xlabel("Date")
    plt.ylabel("Normalized Price")
    plt.legend(["Price", "SMA", "Price / SMA"])
    plt.title("14 Day Simple Moving Average vs Date")
    plt.savefig("sma.png")

def plot_momentum(df, momentum):
    fig, ax = plt.subplots(2, figsize=(8, 6))
    fig.suptitle('14 Day Momentum vs Date')
    plt.subplot(2, 1, 1)
    plt.ylabel("JPM Normalized Price")
    plt.plot(df, color='green', label="price")
    plt.legend(["Price"])

    plt.subplot(2, 1, 2)
    plt.ylabel("Momentum")
    plt.plot(momentum, color='red', label="std")
    plt.tick_params(axis='x', rotation=20)
    plt.legend(["Momentum"])

    for ax in fig.get_axes():
        ax.label_outer()
    plt.xlabel("Date")

    plt.savefig("momentum.png")

def plot_ema(df, ema):
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(ema, color='navy')
    ax.plot(df, color='r', alpha=0.4)
    ax.tick_params(axis='x', rotation=20)
    plt.xlabel("Date")
    plt.ylabel("Exponential Moving Average")
    plt.legend(["EMA", 'Price'])
    plt.title("14 Day Exponential Moving Average vs Date")
    plt.savefig("ema.png")

def generate_indicators(stock='JPM', lookback=14, start_date=dt.datetime(2008, 1, 1), end_date=dt.datetime(2009, 12, 31)):

    dates = pd.date_range(start_date, end_date)
    df = get_data([stock], dates, True, colname='Adj Close').drop(columns=['SPY'])
    df_norm = df / df.iloc[0, :]

    # generate dataframes from technical indicators
    std = get_std(df_norm, lookback)
    sma = get_sma(df_norm, lookback)
    price_per_sma = get_price_per_sma(df_norm, sma)
    momentum = get_momentum(df_norm, lookback)
    ema = get_ema(df_norm, lookback)
    bbp, top_band, bottom_band = get_BB(df_norm, lookback, sma, std)
    macd_raw, macd_signal = get_macd(df,start_date)

    # generate plots
    plot_BB(df_norm, top_band, bottom_band)
    plot_sma(df_norm, sma, price_per_sma)
    plot_momentum(df_norm, momentum)
    plot_ema(df_norm, ema)
    plot_macd(macd_raw,macd_signal)


if __name__ == "__main__":
    generate_indicators()