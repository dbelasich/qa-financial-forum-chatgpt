import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI()

data_set_1 = [
    {
        "Security":
        {
            "AssetType": "Equity",
            "Symbol": "AAPL",
        },
        "QuantityTraded": 500,
        "ExecutionPrice": 169.65,
        "LastPrice": 165.45,
        "OptionType": None,
        "Underlier": None,
        "OptionPremium": None,
        "ExpirationDate": None
    },
    {
        "Security":
        {
            "AssetType": "Equity",
            "Symbol": "GOOGL",
        },
        "QuantityTraded": 200,
        "ExecutionPrice": 154.92,
        "LastPrice": 161.89,
        "OptionType": None,
        "Underlier": None,
        "OptionPremium": None,
        "ExpirationDate": None
    },
    {
        "Security":
        {
            "AssetType": "Option",
            "Symbol": "GOOGL 06/23/24 C145",
        },
        "QuantityTraded": 100,
        "ExecutionPrice": 145,
        "LastPrice": 161.89,
        "OptionType": "Call",
        "Underlier": "GOOGL",
        "OptionPremium": 10,
        "ExpirationDate": "06/23/24"
    },
    {
        "Security":
        {
            "AssetType": "Option",
            "Symbol": "AAPL 05/07/24 P175",
        },
        "QuantityTraded": 700,
        "ExecutionPrice": 175,
        "LastPrice": 165.45,
        "OptionType": "Put",
        "Underlier": "AAPL",
        "OptionPremium": 10,
        "ExpirationDate": "05/07/24"
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
        Given the provided JSON data containing market information for securities that is delimited by triple 
        backticks, compute and add the following calculated fields to the JSON:
            Percentage change from Execution Price to Last Price.
            Market Value based on Last Price and Quantity Traded.
            Profit or Loss (P/L) for each security.
            Profit or Loss Percentage based on the Execution Price and Last Price.
        Add these fields to the JSON data with relevant column names and return the updated JSON output formatted.
        ```{data_set_1}```
        """
    response = get_completion(prompt)
    print(response)


if __name__ == "__main__":
    calculate()
