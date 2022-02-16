import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols


tot_rv = pd.read_csv("RV_table.csv", index_col="date")
bvol = pd.read_csv("BITMEX_BVOL24H, 1D_close.csv", index_col="date")

df_comp = pd.concat([tot_rv["TOT_RV"], bvol],axis=1)

plt.rcParams["figure.figsize"] = (14,8)
# plt.rcParams['font.size'] = 16
plt.rcParams['lines.linewidth'] = 1
plt.rcParams["axes.grid"] = True
df_comp = df_comp.dropna()
df_comp.plot()
plt.show()

res = ols('bvol ~ TOT_RV', data=df_comp).fit()
print(res.summary())

print("Correlation")
print(df_comp.corr())

