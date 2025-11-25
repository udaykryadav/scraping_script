import pandas as pd

url = "https://www.moneycontrol.com/mutual-funds/performance-tracker/returns/value-fund.html"

tables = pd.read_html(url)

for i, table in enumerate(tables):
    print(f"\n---- TABLE {i} ----")
    print(table.head())
