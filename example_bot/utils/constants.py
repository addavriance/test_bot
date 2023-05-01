URL = 'https://1xstavka.ru/LiveFeed/Get1x2_VZip'

COOKIES = {
    'dnb': '1',
    'auid': 'WNT5lGRM8UtA1zabUhMyAg==',
    'SESSION': 'a4d41cae4435cc6bce79f100154badfe',
    'visit': '1-caff18685e2697ecd0842cd51da309dd',
    'fast_coupon': 'true',
    'v3fr': '1',
    'lng': 'ru',
    'flaglng': 'ru',
    'typeBetNames': 'short',
    'coefview': '0',
    'tzo': '3',
    'completed_user_settings': 'true',
    '_ym_uid': '1682764106222434339',
    '_ym_d': '1682764106',
    '_ym_isad': '1',
    'sh.session': 'b8a9cc86-1afd-403a-87b0-e48f3a887bb3',
    'pushfree_status': 'canceled',
    'right_side': 'right',
    '_glhf': '1682783984',
    'ggru': '139',
}

HEADERS = {
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,es;q=0.6',
    'Connection': 'keep-alive',
    'Referer': 'https://1xstavka.ru/live/basketball',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

PARAMS = {
    'sports': '3',
    'count': '500',
    'antisports': '188',
    'mode': '4',
    'country': '1',
    'partner': '51',
    'getEmpty': 'true',
    'noFilterBlockEvent': 'true',
}

def GET_PARAMS(id_m: int) -> dict:
    params = {
        'sports': '3',
        'count': '50',
        'antisports': '188',
        'mode': '4',
        'subGames': f'{id_m}',
        'country': '1',
        'partner': '51',
        'getEmpty': 'true',
        'noFilterBlockEvent': 'true',
    }
    return params