from inquirer.themes import GreenPassion
import MetaTrader5 as mt5
import os
from datetime import datetime
from pathlib import Path
import sys
# import pytz module for working with time zone
import pytz

sys.path.append(os.path.realpath("."))
import inquirer  # noqa

question = [
    inquirer.List("timeframe",
                  message="Choose the time frame to load data",
                  choices=["M1", "M5", "M15", "M30", "H1", "H4", "D"]),
    inquirer.List("pair",
                  message="Choose the pair to load data",
                  choices=["AUDCAD", "AUDCHF", "AUDJPY", "AUDNZD", "AUDUSD",
                           "CADCHF", "CADJPY",
                           "CHFJPY",
                           "EURAUD", "EURCAD", "EURCHF", "EURGBP", "EURJPY", "EURNZD", "EURUSD",
                           "GBPAUD", "GBPCAD", "GBPCHF", "GBPJPY", "GBPNZD", "GBPUSD",
                           "NZDCAD", 'NZDCHF', 'NZDJPY', 'NZDUSD',
                           'USDCAD', 'USDCHF', 'USDJPY']),
    inquirer.Text('start_year', message='Please input start year'),
    inquirer.Text('start_month', message='Please input start month'),
    inquirer.Text('start_day', message='Please input start day'),
    inquirer.Text('end_year', message='Please input end year'),
    inquirer.Text('end_month', message='Please input end month'),
    inquirer.Text('end_day', message='Please input end day'),
]


def get_timeframe_from_mt5(arg):
    switch = {
        'M1': mt5.TIMEFRAME_M1,
        'M5': mt5.TIMEFRAME_M5,
        'M15': mt5.TIMEFRAME_M15,
        'M30': mt5.TIMEFRAME_M30,
        'H1': mt5.TIMEFRAME_H1,
        'H4': mt5.TIMEFRAME_H4,
        'D': mt5.TIMEFRAME_D1,
    }
    return switch.get(arg)


def date_validation(start_date, end_date):
    if datetime.strptime(start_date, '%Y-%m-%d') and datetime.strptime(end_date, '%Y-%m-%d') and datetime.strptime(start_date, '%Y-%m-%d') < datetime.strptime(end_date, '%Y-%m-%d'):
        return True
    else:
        return False


def get_data_from_mt5():
    answers = inquirer.prompt(question, theme=GreenPassion())

    if date_validation(f"{answers['start_year']}-{answers['start_month']}-{answers['start_day']}", f"{answers['end_year']}-{answers['end_month']}-{answers['end_day']}"):
        # connect to MetaTrader 5
        if not mt5.initialize():
            print("initialize() failed")
            mt5.shutdown()

        # request connection status and parameters
        print(mt5.terminal_info())
        # get data on MetaTrader 5 version
        print(mt5.version())

        # set time zone to UTC
        timezone = pytz.timezone("Etc/UTC")
        # create 'datetime' objects in UTC time zone to avoid the implementation of a local time zone offset
        utc_from = datetime(int(answers['start_year']),
                            int(answers['start_month']),
                            int(answers['start_day']),
                            tzinfo=timezone)
        utc_to = datetime(int(answers['end_year']),
                          int(answers['end_month']),
                          int(answers['end_day']),
                          tzinfo=timezone)

        # get bars from USDJPY M5 within the interval of from - to in UTC time zone
        rates = mt5.copy_rates_range(
            answers['pair'], get_timeframe_from_mt5(answers['timeframe']), utc_from, utc_to)

        # shut down connection to MetaTrader 5
        mt5.shutdown()
        file_path = f"{Path(os.getcwd()).parent.absolute()}\data\{answers['pair']}_{answers['timeframe']}_{answers['start_year']}-{answers['start_month']}-{answers['start_day']}_{answers['end_year']}-{answers['end_month']}-{answers['end_day']}.csv"
        with open(file_path, 'w') as fp:
            fp.write('datetime,open,high,low,close,\n')
            for rate in rates:
                fp.write(
                    f"{datetime.utcfromtimestamp(int(rate[0])).strftime('%Y.%m.%d %H:%M:%S')},{rate[1]},{rate[2]},{rate[3]},{rate[4]},\n")
    else:
        print('Invalid value date time, Please choose again')
        get_data_from_mt5()


if __name__ == '__main__':
    get_data_from_mt5()
