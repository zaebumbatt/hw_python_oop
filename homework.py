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
        return sum([i.amount for i in self.records if i.date == date])

    def get_week_stats(self):
        date = dt.date.today()
        date_week_ago = dt.date.today() - dt.timedelta(days=7)
        return sum([i.amount for i in self.records if date_week_ago <= i.date <= date])

    def remaining(self):
        remaining = self.limit - self.get_today_stats()
        return remaining


class CashCalculator(Calculator):
    USD_RATE = 68.69
    EURO_RATE = 77.83
        
    def get_today_cash_remained(self, currency):
        if (self.remaining()) == 0:
            return f'Денег нет, держись'

        result = {
            'rub': str(abs(self.remaining())) + ' руб',
            'usd': str(abs(round((self.remaining())/self.USD_RATE, 2))) + ' USD',
            'eur': str(abs(round((self.remaining())/self.EURO_RATE, 2))) + ' Euro'
        }
        
        if (self.remaining()) > 0:
            return f'На сегодня осталось {result[currency]}'
        
        return f'Денег нет, держись: твой долг - {result[currency]}'


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        if self.remaining() > 0:
            return f'Сегодня можно съесть что-нибудь ещё,' + \
                   f' но с общей калорийностью не более {self.remaining()} кКал'
        
        return 'Хватит есть!'
