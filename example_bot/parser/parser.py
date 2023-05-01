import requests
from pprint import pprint
from utils.constants import COOKIES, HEADERS, PARAMS, GET_PARAMS, URL
from utils.file_handler import get_data


def get_break_matches():
    response = requests.get(URL, params=PARAMS, cookies=COOKIES, headers=HEADERS)
    json_data = response.json()['Value']
    data_ids = list(get_data("blacklist")["blacklist"])
    break_matches = []
    for match in json_data:
        if not (match["I"] in data_ids) and match.get('SC', {}).get('CPS') == 'Перерыв' and match.get('SC', {}).get('TS') == 1200:
            cfs = []
            scores = match['SC']['FS']
            total_score = scores['S1'] + scores['S2']

            s1 = match['SC']['PS'][0]['Value']  # 1 четверть
            s2 = match['SC']['PS'][1]['Value']  # 2 четверть
            score_s1 = f'{s1["S1"]}:{s1["S2"]}'
            score_s2 = f'{s2["S1"]}:{s2["S2"]}'

            if 50 <= total_score <= 75:
                # pprint(match)

                match_id = match['I']
                match_data = requests.get(URL, params=GET_PARAMS(match_id)).json()['Value']
                if len(match["AE"]) > 1 and match["AE"][1]["G"] == 17:
                    cfs = match['AE'][1]['ME']

                findable_total = total_score * 2 + 15
                findable_total_2 = total_score + 15

                current_total, current_total_2, cf_1, cf_2, is_good_total, is_good_total2 = 0, 0, 0, 0, False, False

                for match_2 in match_data:  # получаем кф 2-й половины
                    if match_2['I'] == match_id:
                        data_states = match_2['SG']
                        for data_state in data_states:
                            state = data_state.get('PN', '')
                            if state == '2-я половина':
                                cfs_2 = data_state['E']
                                for cf in cfs_2:
                                    if cf['T'] == 10:
                                        current_total_2 = cf['P']
                                        cf_2 = cf['C']
                                        if current_total_2 >= findable_total_2 and cf_2 >= 1.6:
                                            is_good_total2 = True
                                            break
                                break

                for cf in cfs:  # получаем кф основы
                    if cf['T'] == 10:
                        current_total = cf['P']
                        cf_1 = cf['C']
                        if current_total >= findable_total and cf_1 >= 1.6:
                            is_good_total = True
                            break

                is_good = is_good_total2 or is_good_total
                break_matches.append(
                    {'ID': match_id, 'team1': match['O1'], 'team2': match['O2'], 'total_score': total_score,
                     'total': findable_total, 'total_2': findable_total_2, 'cur_total': current_total,
                     'cur_total2': current_total_2, 'isGood': is_good, 's1': score_s1, 's2': score_s2, 'cf1': cf_1,
                     'cf2': cf_2})
    return break_matches

# pprint(get_break_matches())
