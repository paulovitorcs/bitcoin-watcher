import logging
from .config import env
from requests import post

class Pushover:
    API_URL = 'https://api.pushover.net/1/messages.json'

    @classmethod
    def do_post(cls, data: dict):
        """
        send post request to pushover app
        """
        if not type(data) == dict:
            logging.error('There is a wrong data trying to do a post')
            raise TypeError('data should be a dict')

        request_data = {
            'token': env.PUSHOVER_TOKEN,
            'user': env.PUSHOVER_USER
        }
        request_data.update(data)

        return post(cls.API_URL, data = request_data)

    @classmethod
    def send_notification(cls, title, message):
        """
        send notification to pushover app
        """
        data = {
            'title': title,
            'message': message
        }

        if cls.do_post(data).ok:
            logging.info('Notification sent to Pushover')
            return True

        logging.error('Pushover Notification did not work')
        return False
