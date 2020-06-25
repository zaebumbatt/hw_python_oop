import datetime as dt


class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        date = dt.date.today()
        return sum(i.amount for i in self.records if i.date == date)

    def get_week_stats(self):
        date = dt.date.today()
        date_week_ago = dt.date.today() - dt.timedelta(days=7)
        return sum(i.amount for i in self.records
                   if date_week_ago <= i.date <= date)

    def remaining(self):
        remaining = self.limit - self.get_today_stats()
        return remaining


class CashCalculator(Calculator):
    USD_RATE = 68.69
    EURO_RATE = 77.83

    def get_today_cash_remained(self, currency):
        remains = self.remaining()

        if remains == 0:
            return 'Денег нет, держись'

        convert = {
            'rub': (1, ' руб'),
            'usd': (self.USD_RATE, ' USD'),
            'eur': (self.EURO_RATE, ' Euro')
        }

        if currency not in convert:
            raise ValueError('Неверная валюта, должна быть rub, usd или eur')

        currency_rate, currency_name = convert[currency]
        number = abs(round(remains / currency_rate, 2))
        result = str(number) + currency_name

        if remains > 0:
            return f'На сегодня осталось {result}'

        return f'Денег нет, держись: твой долг - {result}'


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        remains = self.remaining()

        if remains > 0:
            return ('Сегодня можно съесть что-нибудь ещё, ' +
                    f'но с общей калорийностью не более {remains} кКал')

        return 'Хватит есть!'
