import yfinance as yf
import ta
import pandas as pd
import math
# Creating a Series
# s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
# print(s)
# s.info()

def get_symbol_matches(symbol):
    pd.set_option('display.max_rows', None)
    data=yf.download(symbol,start="2023-12-31", end="2025-04-20")
    data['ma50'] = ta.trend.sma_indicator(data[data.columns[0]], window=50)
    data['ma10'] = ta.trend.sma_indicator(data[data.columns[0]], window=10)

    match_list=pd.DataFrame(columns=["Close", "ma50", "ma10"])
    matches=[]
    for idx,i in data.iterrows():
        if (pd.isna(i["ma50"]) is not True) and idx.year in [2025]:
            indx=data["ma50"].index.get_loc(idx)
            indxc = data["Close"].index.get_loc(idx)
            if i.isna().any()!=True:
                if math.isclose(i["ma50"],i["ma10"],rel_tol=0.01) and data["ma10"].iloc[indx-5:indx].diff().gt(0).any():
                    if (float(data["Close"].iloc[indxc:indxc+5].mean()) > float(data["ma10"].iloc[indx]))==True:
                        matches.append(i)
                        # print(i[["Close", "ma50", "ma10"]])
                        # print(data["ma10"].iloc[indx-5:indx])
                        # print("Buy Signal")
    print(f"{symbol} done")
    return matches

cdrs = [
    "MMMM", "AXP", "BKNG", "CRWD", "F", "GE", "ISRG", "MU", "QCOM", "TXN", "SMCI",
    "BLK", "STZ", "DEER", "LULU", "PANW", "NOWS", "TMO", "ADBE", "AVGO", "CATR",
    "LLY", "JNJ", "RTX", "BA", "CHEV", "CITI", "XOM", "INTC", "UBER", "HON", "ABBV",
    "PG", "CVS", "UPS", "VZ", "UNH", "SBUX", "NKE", "MCDS", "COLA", "CSCO", "BOFA",
    "GS", "HD", "NVDA", "WMT", "COST", "CRM", "AMD", "PFE", "MA", "BRK", "JPM", "IBM",
    "DIS", "META", "MSFT", "PYPL", "VISA", "AAPL", "NFLX", "GOOG", "TSLA", "AMZN"
]


betapro = [
    "CNDU", "CNDD", "CNDI",
    "SPXU", "SPXD", "SPXI",
    "QQU", "QQD",
    "CFOU", "CFOD",
    "ATMU", "ATMD",
    "RITU", "RITD",
    "GDXU", "GDXD",
    "NRGU", "NRGD",
    "HOU", "HOD",
    "HNU", "HND",
    "GLDU", "GLDD",
    "SLVU", "SLVD"
]
junior_miners= [
    "K.TO", "AGI.TO", "OR.TO", "IMG.TO",
    "BTO.TO", "ELD.TO", "EQX.TO", "LUG.TO",
    "NGD.TO", "OGC.TO", "TXG.TO", "DPM.TO",
    "SSRM.TO", "KNT.TO", "CXB.TO", "SSL.TO",
    "WDO.TO", "OLA.TO", "CG.TO", "TFPM.TO",
    "SEA.TO", "SKE.TO", "ARIS.TO", "IAU.TO",
    "VGCX.TO"
]
xgd = ["NEM", "AEM", "WPM", "ABX", "FNV", "GFI", "K", "AU", "AGI", "RGLD"]

slv=tickers = ["WPM", "PAAS", "CDE", "BVN", "OR.TO", "HL", "SSRM", "AG.TO", "FVI.TO", "MAG.TO", "TFPM.TO", "EXK", "AYA.TO"]
bear_etfs = [
    "AAPD", "AMDD", "AMZD", "AVS", "BRKD", "GGLS", "METD", "MSFD", "MUD", "NFXS",
    "NVDD", "PLTD", "TSLS", "TSMZ", "SPDN", "REKT", "QQQD", "AIBD", "ERY", "DUST",
    "JDST", "DRIP", "TMV", "TYO", "YANG", "EDZ", "SPXS", "TZA", "WEBS", "FAZ",
    "DRV", "HIBS", "LABD", "SOXS", "TECS"
]
list_of_leveraged_shares= [
    "MIDU", "SPXL", "SPXS", "TNA", "TZA", "EDC", "EDZ", "EURL", "KORU", "MEXX",
    "YINN", "YANG", "TYD", "TYO", "TMF", "TMV", "CURE", "DFEN", "DPST", "DRN",
    "DRV", "DUSL", "FAS", "FAZ", "HIBL", "HIBS", "LABU", "LABD", "NAIL", "PILL",
    "RETL", "SOXL", "SOXS", "TECL", "TECS", "TPOR", "UTSL", "WANT", "WEBL", "WEBS",
    "AIBU", "AIBD", "BRZU", "CHAU", "CLDL", "CWEB", "ERX", "ERY", "EVAV", "FNGG",
    "GUSH", "DRIP", "INDL", "JNUG", "JDST", "LMBO", "NUGT", "DUST", "OOTO", "QQQU",
    "SPUU", "UBOT", "URAA", "XXCH", "QQQD", "REKT", "SPDN", "AAPU", "AAPD", "AMUU",
    "AMDD", "AMZU", "AMZD", "AVL", "AVS", "BRKU", "BRKD", "GGLL", "GGLS", "METU",
    "METD", "MSFU", "MSFD", "MUU", "MUD", "NFXL", "NFXS", "NVDU", "NVDD", "PLTU",
    "PLTD", "TSLL", "TSLS", "TSMX", "TSMZ"
]


list_ofSnP500_companies = []
SnP500wiki = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
nasdaq = "https://en.wikipedia.org/wiki/Nasdaq-100#Components"
tables = pd.read_html(SnP500wiki)
Snptable = tables[0]


list_of_tsx60_companies=[]
tsx60wiki="https://en.wikipedia.org/wiki/S%26P/TSX_60"
tables_tsx60=pd.read_html(tsx60wiki)
tsx60table=tables_tsx60[1]

# nasdaqtable = tables[4]
k = 0
# for ticker in tsx60table["Symbol"]:
#     list_ofSnP500_companies.append(ticker)
#     k += 1
ma_dict={}
for i in ["TSLZ","PLTD"]:
    ma_dict[str(i)]=get_symbol_matches(f"{i}")
breakpoint()
for i in ma_dict.keys():
    if len(ma_dict[i])>0:
        print(ma_dict[i][-1])
    else:
        print(f"No matches in {i}")
# print(data[['Close', 'ma50','ma10']])

breakpoint()