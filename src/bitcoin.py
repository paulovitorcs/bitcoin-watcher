from requests import get

class Bitcoin:
    API_URL = 'http://watcher.foxbit.com.br/api/Ticker'
    values = None

    @classmethod
    def get_values_from_api(cls, currency = 'BRLXBTC'):
        """
        do get to api
        """
        params = {
            'exchange': 'Foxbit',
            'pair': currency,
        }

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
        return self.values['buyPrice']

    @property
    def sell_price(self):
        """
        bit coin sell price
        """
        return self.values['sellPrice']
