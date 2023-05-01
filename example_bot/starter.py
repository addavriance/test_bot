import threading
from bot.bot import start_bot
from listener.listener import start_parse


def start_all():
    thread1 = threading.Thread(target=start_bot)
    thread2 = threading.Thread(target=start_parse)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()


if __name__ == '__main__':
    start_all()
