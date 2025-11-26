import pandas as pd

url = "https://www.moneycontrol.com/mutual-funds/bandhan-sterling-value-fund-direct-plan-growth/portfolio-holdings/MAG735"

tables = pd.read_html(url)

# yaha par bas vo table number dalna hai jis mai sara data hai 
df = tables[3]

df.to_csv("Bandhan_Value_Fund_Holdings.csv", index=False, encoding="utf-8")

print("Scraping completed! CSV saved as Bandhan_Value_Fund_Holdings.csv")
