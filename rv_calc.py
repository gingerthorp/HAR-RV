import sqlite3
import pandas as pd
import numpy as np


def rv(freq):
    conn = sqlite3.connect(f"coin_{freq}.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    coin_list = cursor.fetchall()

    coin_table = [table[0] for table in coin_list]

    RV_table = pd.DataFrame()
    for coin in coin_table:
        sql = f"SELECT * FROM {coin} ORDER BY 'Open time'"

        df = pd.read_sql(sql, conn)
        if len(df) > 0:
            df["RT"] = df["Close"].pct_change() ** 2
            df["date"] = df["Open time"].str.slice(start=0, stop=10)
            df_date = df.groupby("date").sum() ** 0.5 * 100
            RV = pd.DataFrame()
            RV[f"{coin[:-3]}"] = df_date["RT"]
            RV_table = pd.concat([RV_table, RV], axis=1)
    print(RV_table)
    RV_table["TOT_RV"] = RV_table.mean(axis=1)
    RV_table.to_csv(f"RV_table.csv")


if __name__ == '__main__':
    freq = "5m"
    rv(freq)

