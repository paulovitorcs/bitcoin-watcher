from src.bitcoin import Bitcoin

class TestBitcoin:
    def test_get_values_from_api(self):
        """
        test a correct get values from api with default data
        """
        response = Bitcoin.get_values_from_api()

        assert type(response) == dict
        assert response['currency'] == 'BRLXBTC'
        assert response['exchange'] == 'Foxbit'
        assert 'lastVariation' in response.keys()
        assert 'buyPrice' in response.keys()
        assert 'sellPrice' in response.keys()

    def test_bitcoin_values(self):
        """
        test bitcoin values and properties
        """
        bitcoin = Bitcoin()

        assert hasattr(bitcoin, 'last_variation')
        assert hasattr(bitcoin, 'buy_price')
        assert hasattr(bitcoin, 'sell_price')
