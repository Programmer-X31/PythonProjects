import requests
import pyperclip
import pyinputplus

print("Loading...")

def initiate_program():
    currency_keys = list(requests.get("https://free.currconv.com/api/v7/currencies?apiKey=f97208f085855f51e65c").json()['results'].keys())
    print("Enter the currency you want to convert FROM:")
    currency_from = pyinputplus.inputChoice(currency_keys, limit=2, prompt="")
    
    print("Enter the currency you want to convert TO:")
    currency_to = pyinputplus.inputChoice(currency_keys, prompt="", limit=2)
    
    print(f"Enter the  Number of {currency_from.upper()}")
    currency_num = pyinputplus.inputInt(limit=2, prompt="")
    
    current_value_of_money = get_data(currency_from, currency_to)
    converted_value = currency_num * current_value_of_money 
    
    # print(pprint.pprint(response.json()))
    print(f"The Converted Value:\n{converted_value}")
    pyperclip.copy(converted_value)
    print("\nConverted value copied to clipboard")

def get_data(currency_f, currency_t):
    value = requests.get(f"https://free.currconv.com/api/v7/convert?q={currency_f}_{currency_t}&compact=ultra&apiKey=f97208f085855f51e65c").json()
    return list(value.values())[0]
initiate_program()
