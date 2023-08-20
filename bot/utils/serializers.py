from database.models import Bank

class Serialiser:

    def __init__(self, data):
        self.data: list[Bank] = data
    
    def to_text(self):
        self.data = sorted(self.data, key=lambda item: item.buy_currency)
        text = "\n\n".join([f"{index+1}. 🏦<u>{bank.name}</u>:\n💲➡️🇧🇾Pass - <b>{bank.surrender_currency}</b> BYN\n🇧🇾➡️💲Buy - <b>{bank.buy_currency}</b> BYN" for index, bank in enumerate(self.data)])
        return "Sort by buy currency\n\n"+text

