import requests

url = "https://api.freeapi.app/api/v1/public/stocks"

def get_data():
    res = requests.get(url)
    data = res.json()

    # Check if the response is successful and contains data
    if data.get('success') and 'data' in data:
        # Loop through each stock entry if there's a list of stocks
        for stock in data['data']['data']:
            # Extract details if they exist in the stock dictionary
            Name = stock.get('Name', 'N/A')
            Symbol = stock.get('Symbol', 'N/A')
            ListingDate = stock.get('ListingDate', 'N/A')
            ISIN = stock.get('ISIN', 'N/A')
            MarketCap = stock.get('MarketCap', 'N/A')
            CurrentPrice = stock.get('CurrentPrice', 'N/A')
            HighLow = stock.get('HighLow', 'N/A')
            StockPE = stock.get('StockPE', 'N/A')
            BookValue = stock.get('BookValue', 'N/A')
            DividendYield = stock.get('DividendYield', 'N/A')
            ROCE = stock.get('ROCE', 'N/A')
            ROE = stock.get('ROE', 'N/A')
            FaceValue = stock.get('FaceValue', 'N/A')
            
            # Print stock details
            print(f"Name: {Name}")
            print(f"Symbol: {Symbol}")
            print(f"Listing Date: {ListingDate}")
            print(f"ISIN: {ISIN}")
            print(f"Market Cap: {MarketCap}")
            print(f"Current Price: {CurrentPrice}")
            print(f"High/Low: {HighLow}")
            print(f"Stock PE: {StockPE}")
            print(f"Book Value: {BookValue}")
            print(f"Dividend Yield: {DividendYield}")
            print(f"ROCE: {ROCE}")
            print(f"ROE: {ROE}")
            print(f"Face Value: {FaceValue}")
            print("\n" + "-" * 40 + "\n")

# Call the function
get_data()
