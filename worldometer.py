import pandas as pd
import requests
url = "https://www.worldometers.info/world-population/population-by-country/"
tbls_r = requests.get(url)
tbls = pd.read_html(tbls_r.text)
tbl = tbls[0]
# print(tbl)
tbl.loc[0:, "Urban Pop %"] = tbl.loc[0:, "Urban Pop %"].str.strip("% ")
tbl.dropna(inplace=True)
tbl.loc[0:, "Urban Pop %"] = pd.to_numeric(tbl.loc[0:,"Urban Pop %"], errors='coerce')
# tbl_sorted = tbl.sort_values("Urban Pop %", ascending=False)
# print(tbl_sorted.to_string())

# tbl_sort_fert = tbl.sort_values("Fert. Rate", ascending=False)
# print(tbl_sort_fert.head(20).to_string())

tbl_d = tbl.sort_values("Density (P/Km²)", ascending=False)
# print(tbl_d.to_string())
num = (tbl_d["Country (or dependency)"] == "Macao").argmax() + 1
print(num)