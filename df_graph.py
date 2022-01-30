#https://qiita.com/Nick_utuiuc/items/9bf839f5612c54606348

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 10  # 適当に必要なサイズに
plt.rcParams['xtick.direction'] = 'in'  # in or out
plt.rcParams['ytick.direction'] = 'in'
plt.rcParams['axes.xmargin'] = 0.01
plt.rcParams['axes.ymargin'] = 0.01
plt.rcParams["legend.fancybox"] = False  # 丸角OFF
plt.rcParams["legend.framealpha"] = 1  # 透明度の指定、0で塗りつぶしなし
plt.rcParams["legend.edgecolor"] = 'black'  # edgeの色を変更

plt.rcParams["mathtext.fontset"] = "stix" # stixフォントにする
plt.rcParams['mathtext.default']= 'default' # defaultテキストにする

def multiLegend(df, x, y_list):
    """
    1つのy軸に対して複数の判例を与える
    params
        df(pandas.DataFrame): 対象とするDataFrame
        x: x軸となる列名
        y_list: 描画するデータ列名リスト
    return
        None
    """
    c_list = ["k", "r", "b", "g", "c", "m", "y"]
    l_list = ["-","--","-.","."]
    fig, ax = plt.subplots(figsize=(5, 5))
    plt.subplots_adjust(top=0.95, right=0.95)
    for i in range(len(y_list)):
        y = y_list[i]
        ax.plot(df[x], df[y], linestyle=l_list[i], color=c_list[i], label=y)
    yLabel = ', '.join(y_list)
    ax.set_ylabel(yLabel)
    ax.set_xlabel(x)
    plt.legend()
    plt.show()
    return

def multiLegend2(df, x, y1_list, y2_list=None):
    """
    2つのy軸に対して複数の判例を与える
    y2_listを入れなければ2軸にならない
    params
        df(pandas.DataFrame): 対象とするDataFrame
        x: x軸となる列名
        y1_list: 左に描画するデータ列名リスト
        y2_list: 右に描画するデータ列名リスト
    return
        None
    """
    c_list = ["k", "r", "b", "g", "c", "m", "y"]
    l_list = ["-", "--", "-.", "."]
    fig, ax1 = plt.subplots(figsize=(5.5, 5))
    j = 0
    for y in y1_list:
        ax1.plot(df[x], df[y], linestyle=l_list[j],
                      color=c_list[j], label=y)
        j += 1
    ax1.legend(loc='lower left')
    ax1.set_xlabel(x)
    ax1.set_ylabel(', '.join(y1_list))
    if len(y2_list) != None:
        ax2 = ax1.twinx()
        for y in y2_list:
            ax2.plot(df[x], df[y], linestyle=l_list[j],
                         color=c_list[j], label=y)
            j += 1
        ax2.legend(loc='upper right')
        ax2.set_ylabel(', '.join(y2_list))
    plt.tight_layout()
    plt.show()
    return

def multiAxes(df, x, y_list):
    """
    3つ以上の軸に対して自動的に右に軸を追加する
    params
        df(pandas.DataFrame): 対象とするDataFrame
        x: x軸となる列名
        y_list: 描画するデータ列名リスト,2列目以降順次右に軸を追加
    return
        None
    """
    c_list = ["k", "r", "b", "g", "c", "m", "y"]
    l_list = ["-","--","-.","."]
    fig, ax0 = plt.subplots(figsize=(6, 5))
    plt.subplots_adjust(top=0.95, right=0.95-(len(y_list)-1)*0.1) #ずれたらここ調整
    axes = [ax0]  # 変数分の軸の数を作る
    p_list = []  # 変数分のplotの入れ物
    for i in range(len(y_list)):
        y = y_list[i]
        if i != 0:
            axes.append(ax0.twinx())
            axes[i].spines["right"].set_position(("axes", 1+(i-1)*0.2)) #ずれたらここ調整
        p, = axes[i].plot(df[x], df[y], linestyle=l_list[i], color=c_list[i], label=y)
        p_list.append(p)
        axes[i].set_ylabel(y_list[i], color=c_list[i])
        axes[i].yaxis.label.set_color(c_list[i])
        axes[i].spines['right'].set_color(c_list[i])
        axes[i].tick_params(axis='y', colors=c_list[i])
    axes[0].set_xlabel(x)
    plt.legend(p_list,y_list)
    plt.show()
    return

def multiPlots(df, x, y_list):
    """
    複数のArtistを縦に並べる
    params
        df(pandas.DataFrame): 対象とするDataFrame
        x: x軸となる列名
        y_list: 描画するデータ列名リスト
    return
        None
    """
    c_list = ["k", "r", "b", "g", "c", "m", "y"]
    l_list = ["-","--","-.","."]
    fig, axes = plt.subplots(len(y_list), 1, sharex="all", figsize=(4, 2*len(y_list)))
    for i in range(len(y_list)):
        y = y_list[i]
        axes[i].plot(df[x], df[y], linestyle=l_list[i], color=c_list[i], label=y)
        axes[i].set_ylabel(y_list[i], color=c_list[i])
        axes[i].yaxis.label.set_color(c_list[i])
        axes[i].spines['left'].set_color(c_list[i])
        axes[i].tick_params(axis='y', colors=c_list[i])
        if i == len(y_list)-1:
            axes[i].set_xlabel(x)
    plt.tight_layout()
    plt.show()
    return

def multiLegend_wError(df, x, y_list, y_error_list):
    """
    エラーバー付きの1軸グラフを作成する
    params
        df(pandas.DataFrame): 対象とするDataFrame
        x: x軸となる列名
        y_list: 描画するデータ列名リスト
    return
        None
    """
    c_list = ["k", "r", "b", "g", "c", "m", "y"]
    l_list = ["-", "--", "-.", "."]
    fig, ax = plt.subplots(figsize=(5, 5))
    plt.subplots_adjust(top=0.95, right=0.95)
    for i in range(len(y_list)):
        y = y_list[i]
        y_error = y_error_list[i]
        ax.plot(df[x], df[y], linestyle=l_list[i], color=c_list[i], label=y)
        ax.fill_between(df[x], df[y]+df[y_error], df[y]-df[y_error], facecolor=c_list[i], edgecolor=None, alpha=0.3)
    yLabel = ', '.join(y_list)
    ax.set_ylabel(yLabel)
    ax.set_xlabel(x)
    plt.legend()
    plt.show()
    return