import pandas as pd

# saari rows 
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

url = "https://www.moneycontrol.com/mutual-funds/bandhan-sterling-value-fund-direct-plan-growth/portfolio-holdings/MAG735"

tables = pd.read_html(url)

for i, table in enumerate(tables):
    print(f"\n---- FULL TABLE {i} ----")
    print(table)
