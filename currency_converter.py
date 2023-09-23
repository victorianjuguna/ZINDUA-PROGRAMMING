def currency_converter(amount, from_currency, to_currency, conversion_rates):
    if from_currency in conversion_rates and to_currency in conversion_rates:
        converted_amount = amount * conversion_rates[to_currency] / conversion_rates[from_currency]
        print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")
    else:
        print("Invalid currency")

# Define conversion rates outside the function
conversion_rates = {
    "KSH": 1.0,
    "USD": 0.0069,
    "EURO": 0.0065,
    "POUND": 0.0056
}

amount = float(input("Enter the amount of money: "))
from_currency = input("From currency ('KSH', 'USD', 'EURO', 'POUND'): ")
to_currency = input("To currency ('KSH', 'USD', 'EURO', 'POUND'): ")

currency_converter(amount, from_currency, to_currency, conversion_rates)
