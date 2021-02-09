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

        return cls.do_post(data).ok