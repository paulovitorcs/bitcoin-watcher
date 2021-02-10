import logging
import time

from src.app import App

class Setup:
    def __init__(self):
        self.set_logging()

    def set_logging(self):
        logging.basicConfig(filename='debug.log', level=logging.DEBUG)
        logging.Formatter("%(asctime)s;%(levelname)s;%(message)s")

    def init_app(self):
        app = App()

        while True:
            app.start_routine()
            time.sleep(1)