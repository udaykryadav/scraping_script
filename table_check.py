import pandas as pd

url = "https://www.moneycontrol.com/mutual-funds/bandhan-sterling-value-fund-direct-plan-growth/portfolio-holdings/MAG735"

tables = pd.read_html(url)

for i, table in enumerate(tables):
    print(f"\n---- TABLE {i} ----")
    print(table.head())
