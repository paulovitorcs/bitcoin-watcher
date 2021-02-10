import schedule
import logging

from .bitcoin import Bitcoin
from .pushover import Pushover
from .config import env

class App:
    bitcoin = None

    def __init__(self):
        """
        init app
        """
        self.schedule_routine()

    def start_routine(self):
        """
        start routine
        """
        schedule.run_pending()

    def schedule_routine(self):
        """
        set app routine
        """
        routine = self.build_routine
        schedule.every(env.INTERVAL).minutes.do(routine)

    def build_routine(self):
        """
        build app routine
        """
        logging.info('Running app routine')
        self.set_bitcoin_data()

        if self.has_pushover():
            self.send_pushover_notification()

    def set_bitcoin_data(self):
        """
        set bitcoin data
        """
        logging.info('Setting bitcoin data')
        self.bitcoin = Bitcoin()

    def has_pushover(self):
        """
        check if has pushover functionality
        """
        is_active = env.HAS_PUSHOVER
        has_pushover_token = env.PUSHOVER_TOKEN
        has_pushover_user = env.PUSHOVER_USER

        return is_active and has_pushover_token and has_pushover_user

    def get_message(self):
        """
        get app message
        """
        message = {
            'title': '$$ Chama no Bitcoin $$',
            'text': '1 Bitcoin está valendo R$' + str(self.bitcoin.buy_price) + '!! Variação de ' + str(self.bitcoin.last_variation) + '%'
        }

        return message

    def send_pushover_notification(self):
        """
        send pushover notification message
        """
        logging.info('Sending Pushover Notification')
        message = self.get_message()
        Pushover.send_notification(message['title'], message['text'])
