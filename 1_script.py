import pandas as pd

url = "https://www.moneycontrol.com/mutual-funds/performance-tracker/returns/value-fund.html"

tables = pd.read_html(url)   

df = tables[0]               

df.to_csv("moneycontrol_value_funds.csv", index=False, encoding="utf-8")

print("Scraping completed! CSV saved as moneycontrol_value_funds.csv")




