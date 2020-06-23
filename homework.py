import datetime as dt


class Record:
    def __init__(self, amount, comment, date = dt.date.today()):
        self.amount = amount
        self.comment = comment
        if date != dt.date.today():
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
        else:
            self.date = dt.date.today()


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, Record):
        self.records.append(Record)
    
    def get_today_stats(self):
        spent = 0
        for i in self.records:
            if i.date == dt.date.today():
                spent += i.amount
        return spent

    def get_week_stats(self):
        spent = 0
        dates = []
        for i in range(0, 7):
            dates.append((dt.date.today() - dt.timedelta(days=i)))
        for i in self.records:
            if i.date in dates:
                spent += i.amount
        return spent


class CashCalculator(Calculator):
    USD_RATE = 68.69
    EURO_RATE = 77.83

    def get_today_cash_remained(self, currency):
        if currency == 'rub':
            result = str(abs(self.limit - self.get_today_stats())) + ' руб'
        elif currency == 'usd':
            result = str(abs(round((self.limit - self.get_today_stats())/self.USD_RATE, 2))) + ' USD'
        elif currency == 'eur':
            result = str(abs(round((self.limit - self.get_today_stats())/self.EURO_RATE, 2))) + ' Euro'

        if (self.limit - self.get_today_stats()) > 0:
            return f'На сегодня осталось {result}'
        elif (self.limit - self.get_today_stats()) == 0:
            return f'Денег нет, держись'

        return f'Денег нет, держись: твой долг - {result}'


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        result = self.limit - self.get_today_stats()
        if result > 0:
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {result} кКал'
        
<<<<<<< HEAD
        return 'Хватит есть!'

if __name__ == '__main__':
    pass
=======
        return 'Хватит есть!'
>>>>>>> 735abdb7f967dedcdd50b9a2bd129189c2925771
