def process_deposit(account_name: str, *amounts, **details):
    total = sum(amounts)
    print(f"account name is: {account_name}")
    print(f"deposits: {amounts}")
    print(f"total deposit is: {total}")

    print("additional details:")
    print(details)
    print(details['state'])

    for key, value in details.items():
        print(f"{key}: {value}")


process_deposit("harrison", 100, 450, 980, 1500, method="online", currency="USD", branch="Dallas", state="TX")

def deposit_v1(account_name: str, amounts: list, details: dict):
    pass


deposit_v1("george", [100, 450, 980, 1500], {'method': 'online', 'currency': 'USD', 'branch': 'Dallas', 'state': 'TX'})
deposit_v1(account_name="george", amounts=[100, 450, 980, 1500], details={'method': 'online', 'currency': 'USD', 'branch': 'Dallas', 'state': 'TX'})



def deposit_v2(account_name: str, amounts: list, method: str, currency: str, branch: str, state: str):
    pass


deposit_v2(account_name="Alex", amounts=[100, 450, 980, 1500], method="online", currency="USD", branch="Dallas", state="TX")
deposit_v2("Alex", [100, 450, 980, 1500], "online", "USD", "Dallas", "TX")