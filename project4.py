import requests

def get_exchange_rate(base_currency, target_currency):
    api_url = f'https://open.er-api.com/v6/latest/{base_currency}'
    response = requests.get(api_url)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch exchange rates. Status code: {response.status_code}")

    data = response.json()
    rates = data.get('rates')

    if not rates or target_currency not in rates:
        raise Exception(f"Exchange rate for {target_currency} not available")

    return rates[target_currency]

def convert_currency(amount, exchange_rate):
    return amount * exchange_rate

def currency_converter():
    try:
        base_currency = input("Enter the source currency code (e.g., USD): ").upper()
        target_currency = input("Enter the target currency code (e.g., EUR): ").upper()
        amount = float(input("Enter the amount to convert: "))

        exchange_rate = get_exchange_rate(base_currency, target_currency)
        converted_amount = convert_currency(amount, exchange_rate)

        print(f"\n{amount} {base_currency} is equal to {converted_amount:.2f} {target_currency}")
        print(f"Exchange rate used: 1 {base_currency} = {exchange_rate:.4f} {target_currency}")

    except ValueError:
        print("Invalid input. Please enter a valid numeric value.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    currency_converter()
