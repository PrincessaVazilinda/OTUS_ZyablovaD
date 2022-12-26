from currency import currency_rate
from db import save_rate
# from db.operations import save_rate
from helpers import say_hello


def main():
    print('started')
    say_hello()
    currency = 'USD'
    today_rate = currency_rate(currency)
    print(f'rate is {today_rate}')
    save_rate(currency, today_rate)
    print('finished')


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
        exit(1)