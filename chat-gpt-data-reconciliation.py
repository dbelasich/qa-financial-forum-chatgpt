import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI()

data_set_1 = [
    {
        "Security": {
            "AssetType": "Equity",
            "Symbol": "MSFT"
        },
        "QuantityTraded": 800,
        "ExecutionPrice": 210.35,
        "LastPrice": 215.70,
        "OptionType": None,
        "Underlier": None,
        "OptionPremium": None,
        "ExpirationDate": None,
        "PercentageChange": 2.55,
        "MarketValue": 172560.0,
        "DayPnL": 4280.0,
        "ProfitLossPercentage": 2.03
    },
    {
        "Security": {
            "AssetType": "Equity",
            "Symbol": "NFLX"
        },
        "QuantityTraded": 300,
        "ExecutionPrice": 545.80,
        "LastPrice": 550.25,
        "OptionType": None,
        "Underlier": None,
        "OptionPremium": None,
        "ExpirationDate": None,
        "PercentageChange": 0.82,
        "MarketValue": 165075.0,
        "DayPnL": 1335.0,
        "ProfitLossPercentage": 0.82
    },
    {
        "Security": {
            "AssetType": "Option",
            "Symbol": "TSLA 08/15/25 C650"
        },
        "QuantityTraded": 200,
        "ExecutionPrice": 650.00,
        "LastPrice": 680.25,
        "OptionType": "Call",
        "Underlier": "TSLA",
        "OptionPremium": 20,
        "ExpirationDate": "08/15/25",
        "PercentageChange": 4.66,
        "MarketValue": 136050.0,
        "DayPnL": 6050.0,
        "ProfitLossPercentage": 9.23
    },
    {
        "Security": {
            "AssetType": "Option",
            "Symbol": "AMZN 09/21/24 P4000"
        },
        "QuantityTraded": 150,
        "ExecutionPrice": 4000.00,
        "LastPrice": 3970.75,
        "OptionType": "Put",
        "Underlier": "AMZN",
        "OptionPremium": 35,
        "ExpirationDate": "09/21/24",
        "PercentageChange": -0.74,
        "MarketValue": 595612.5,
        "DayPnL": -4462.5,
        "ProfitLossPercentage": -0.11
    },
    {
        "Security": {
            "AssetType": "Equity",
            "Symbol": "AAPL"
        },
        "QuantityTraded": 400,
        "ExecutionPrice": 145.20,
        "LastPrice": 143.55,
        "OptionType": None,
        "Underlier": None,
        "OptionPremium": None,
        "ExpirationDate": None,
        "PercentageChange": -1.14,
        "MarketValue": 57420.0,
        "DayPnL": -660.0,
        "ProfitLossPercentage": -0.45
    },
    {
        "Security": {
            "AssetType": "Option",
            "Symbol": "NVDA 11/19/25 C800"
        },
        "QuantityTraded": 100,
        "ExecutionPrice": 800.00,
        "LastPrice": 820.45,
        "OptionType": "Call",
        "Underlier": "NVDA",
        "OptionPremium": 25,
        "ExpirationDate": "11/19/25",
        "PercentageChange": 2.56,
        "MarketValue": 82045.0,
        "DayPnL": 2045.0,
        "ProfitLossPercentage": 5.15
    },
    {
        "Security": {
            "AssetType": "Equity",
            "Symbol": "GOOGL"
        },
        "QuantityTraded": 600,
        "ExecutionPrice": 2525.75,
        "LastPrice": 2543.20,
        "OptionType": None,
        "Underlier": None,
        "OptionPremium": None,
        "ExpirationDate": None,
        "PercentageChange": 0.69,
        "MarketValue": 1525920.0,
        "DayPnL": 10450.0,
        "ProfitLossPercentage": 0.69
    },
    {
        "Security": {
            "AssetType": "Option",
            "Symbol": "FB 10/15/24 P350"
        },
        "QuantityTraded": 200,
        "ExecutionPrice": 350.00,
        "LastPrice": 335.75,
        "OptionType": "Put",
        "Underlier": "FB",
        "OptionPremium": 15,
        "ExpirationDate": "10/15/24",
        "PercentageChange": -4.07,
        "MarketValue": 67150.0,
        "DayPnL": -3025.0,
        "ProfitLossPercentage": -8.65
    },
    {
        "Security": {
            "AssetType": "Equity",
            "Symbol": "T"
        },
        "QuantityTraded": 1000,
        "ExecutionPrice": 30.45,
        "LastPrice": 31.20,
        "OptionType": None,
        "Underlier": None,
        "OptionPremium": None,
        "ExpirationDate": None,
        "PercentageChange": 2.46,
        "MarketValue": 31200.0,
        "DayPnL": 750.0,
        "ProfitLossPercentage": 2.46
    },
    {
        "Security": {
            "AssetType": "Option",
            "Symbol": "INTC 07/11/24 C65"
        },
        "QuantityTraded": 300,
        "ExecutionPrice": 65.00,
        "LastPrice": 69.85,
        "OptionType": "Call",
        "Underlier": "INTC",
        "OptionPremium": 5,
        "ExpirationDate": "07/11/24",
        "PercentageChange": 7.46,
        "MarketValue": 209550.0,
        "DayPnL": 14550.0,
        "ProfitLossPercentage": 22.38
    }
]

data_set_2 = [
    {
        "Security": {
            "AssetType": "Equity",
            "Symbol": "MSFT"
        },
        "QuantityTraded": 800,
        "ExecutionPrice": 210.35,
        "LastPrice": 215.70,
        "OptionType": None,
        "Underlier": None,
        "OptionPremium": None,
        "ExpirationDate": None,
        "PercentageChange": 2.55,
        "MarketValue": 172560.0,
        "DayPnL": 5678.0,
        "ProfitLossPercentage": 2.03
    },
    {
        "Security": {
            "AssetType": "Equity",
            "Symbol": "NFLX"
        },
        "QuantityTraded": 300,
        "ExecutionPrice": 545.80,
        "LastPrice": 550.25,
        "OptionType": None,
        "Underlier": None,
        "OptionPremium": None,
        "ExpirationDate": None,
        "PercentageChange": 0.82,
        "MarketValue": 165075.0,
        "DayPnL": 1335.0,
        "ProfitLossPercentage": 0.82
    },
    {
        "Security": {
            "AssetType": "Option",
            "Symbol": "TSLA 08/15/25 C650"
        },
        "QuantityTraded": 200,
        "ExecutionPrice": 650.00,
        "LastPrice": 680.25,
        "OptionType": "Call",
        "Underlier": "TSLA",
        "OptionPremium": 20,
        "ExpirationDate": "08/15/25",
        "PercentageChange": 4.66,
        "MarketValue": 136050.0,
        "DayPnL": 6050.0,
        "ProfitLossPercentage": 12.23
    },
    {
        "Security": {
            "AssetType": "Option",
            "Symbol": "AMZN 09/21/24 P4000"
        },
        "QuantityTraded": 150,
        "ExecutionPrice": 4000.00,
        "LastPrice": 3970.75,
        "OptionType": "Put",
        "Underlier": "AMZN",
        "OptionPremium": 35,
        "ExpirationDate": "09/21/24",
        "PercentageChange": -0.74,
        "MarketValue": 595612.5,
        "DayPnL": -4462.5,
        "ProfitLossPercentage": -0.11
    },
    {
        "Security": {
            "AssetType": "Equity",
            "Symbol": "AAPL"
        },
        "QuantityTraded": 400,
        "ExecutionPrice": 145.20,
        "LastPrice": 143.55,
        "OptionType": None,
        "Underlier": None,
        "OptionPremium": None,
        "ExpirationDate": None,
        "PercentageChange": -1.14,
        "MarketValue": 57420.0,
        "DayPnL": -660.0,
        "ProfitLossPercentage": -0.46
    },
    {
        "Security": {
            "AssetType": "Option",
            "Symbol": "NVDA 11/19/25 C800"
        },
        "QuantityTraded": 100,
        "ExecutionPrice": 800.00,
        "LastPrice": 820.45,
        "OptionType": "Call",
        "Underlier": "NVDA",
        "OptionPremium": 25,
        "ExpirationDate": "11/19/25",
        "PercentageChange": 2.57,
        "MarketValue": 82045.0,
        "DayPnL": 2045.0,
        "ProfitLossPercentage": 5.15
    },
    {
        "Security": {
            "AssetType": "Equity",
            "Symbol": "GOOGL"
        },
        "QuantityTraded": 600,
        "ExecutionPrice": 2525.75,
        "LastPrice": 2543.20,
        "OptionType": None,
        "Underlier": None,
        "OptionPremium": None,
        "ExpirationDate": None,
        "PercentageChange": 0.69,
        "MarketValue": 1525920.0,
        "DayPnL": 10450.0,
        "ProfitLossPercentage": 0.69
    },
    {
        "Security": {
            "AssetType": "Option",
            "Symbol": "FB 10/15/24 P350"
        },
        "QuantityTraded": 200,
        "ExecutionPrice": 350.00,
        "LastPrice": 335.75,
        "OptionType": "Put",
        "Underlier": "FB",
        "OptionPremium": 15,
        "ExpirationDate": "10/15/24",
        "PercentageChange": -4.07,
        "MarketValue": 67150.0,
        "DayPnL": -3025.1,
        "ProfitLossPercentage": -11.65
    },
    {
        "Security": {
            "AssetType": "Equity",
            "Symbol": "T"
        },
        "QuantityTraded": 1000,
        "ExecutionPrice": 30.45,
        "LastPrice": 31.20,
        "OptionType": None,
        "Underlier": None,
        "OptionPremium": None,
        "ExpirationDate": None,
        "PercentageChange": 5.46,
        "MarketValue": 31200.0,
        "DayPnL": 750.0,
        "ProfitLossPercentage": 2.46
    },
    {
        "Security": {
            "AssetType": "Option",
            "Symbol": "INTC 07/11/24 C65"
        },
        "QuantityTraded": 300,
        "ExecutionPrice": 65.00,
        "LastPrice": 69.85,
        "OptionType": "Call",
        "Underlier": "INTC",
        "OptionPremium": 5,
        "ExpirationDate": "07/11/24",
        "PercentageChange": 7.46,
        "MarketValue": 209550.0,
        "DayPnL": 14550.0,
        "ProfitLossPercentage": 22.38
    }
]


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message.content


def calculate():
    prompt = f"""
        Your task is the following:
        1. Compare the following two JSON datasets that are delimited by triple backticks and identify all 
            discrepancies between the two datasets.  
        2. Use the Security.AssetType and Security.Symbol fields as a key for comparison between each data set.  
        3. Return the results in a tabular format and include all columns from both datasets. 
        4. Security.AssetType and Security.Symbol should be the first two columns, and the remaining columns should be 
            in alphabetical order.
            a. Add the suffixes '_set1' and '_set2' accordingly to each column, but do not add suffixes for 
                Security.AssetType and Security.Symbol
            b. A single row should contain values from both data sets
        ```{data_set_1, data_set_2}```
        """
    response = get_completion(prompt)
    print(response)


if __name__ == "__main__":
    calculate()
