from src.app import App
import time

app = App()

while True:
    app.start_routine()
    time.sleep(1)