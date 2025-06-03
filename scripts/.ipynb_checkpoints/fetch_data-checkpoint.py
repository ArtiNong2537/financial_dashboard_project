import requests

url = "https://raw.githubusercontent.com/datasets/s-and-p-500-companies-financials/master/data/constituents-financials.csv"
save_path = "../data/raw_financials.csv"

response = requests.get(url)
with open(save_path, "wb") as f:
    f.write(response.content)

print("Data downloaded to data/raw_financials.csv")
