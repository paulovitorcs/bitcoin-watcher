import locale
import logging
from requests import get
from .config import env

class Bitcoin:
    API_URL = 'http://watcher.foxbit.com.br/api/Ticker'
    values = None

    @classmethod
    def get_values_from_api(cls):
        """
        do get to api
        """
        params = {
            'exchange': env.EXCHANGE,
            'pair': env.CURRENCY,
        }

        logging.info('Getting Bitcoin Data from Foxbit Watcher API')
        response = get(cls.API_URL, params)
        return response.json()

    def __init__(self):
        """
        init bitcoin class
        """
        self.set_values()

    def set_values(self):
        """
        set class values
        """
        response = self.get_values_from_api()
        self.values = response

    @property
    def last_variation(self):
        """
        bitcoin last variation
        """
        return self.values['lastVariation']

    @property
    def buy_price(self):
        """
        bitcoin buy price
        """
        buy_price = self.values['buyPrice']
        buy_price = locale.currency(buy_price, grouping=True, symbol=None)

        return buy_price

    @property
    def sell_price(self):
        """
        bit coin sell price
        """
        sell_price = self.values['sellPrice']
        buy_price = locale.currency(buy_price, grouping=True, symbol=None)

        return sell_price
