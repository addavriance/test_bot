import asyncio
import datetime
import time

import requests

from bot.bot import send_signal
from parser.parser import get_break_matches
from utils.file_handler import get_data, update_data


def format_to_text(match: dict) -> str:
    text = f"Найдена подходящая игра!" \
           f"Игра: {match['team1']} / {match['team2']}" \
           f"Счет: {match['s1']} | {match['s2']} ; Всего {match['total_score']}" \
           f"Тотал основ.: ожидаемый >{match['total']}M; Текущий {match['cur_total']}M | {match['cf1']}" \
           f"Тотал втор.: ожидаемый >{match['total_2']}M; Текущий {match['cur_total_2']}M | {match['cf2']}"
    return text


def start_parse():
    while True:
        try:
            now = datetime.datetime.now()
            time_str = now.strftime("%H:%M:%S")
            matches = get_break_matches()
            for match in matches:
                if match["isGood"]:

                    data = get_data("blacklist")
                    blacklist = list(data["blacklist"])
                    blacklist.append(match["ID"])
                    data["blacklist"] = blacklist
                    update_data("blacklist", data)

                    text = format_to_text(match)

                    loop = asyncio.get_event_loop()
                    loop.run_until_complete(send_signal(text))
                else:
                    print(f"[{time_str}] No good matches. ({len(matches)} bad)")
            if len(matches) < 1:
                print(f"[{time_str}] No matches.")
            time.sleep(10)
        except requests.exceptions.RequestException:
            print("Произошла ошибка сети в потоке слушателя, поток будет активирован через 50 секунд.")
            time.sleep(50)
