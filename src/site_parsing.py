import json
import requests
from bs4 import BeautifulSoup


def search_scores(name: str = 'Романов Александр Дмитриевич') -> dict:
    r = requests.get(
        'https://rating.unecon.ru/index.php?&y=2020&k=1&f=1&up=12475&s=3&uy=2&g=all&upp=all&ball=hide&sort=fio')

    soup = BeautifulSoup(r.text, 'html.parser')
    temp = soup.find('main').find('div').find('table')
    stud_list = temp.find('tbody').find_all('tr')
    score_list = temp.find('thead').find_all('tr')[1].find_all('th')
    score_list = list(map(lambda x: x.attrs['title'], score_list))
    res = -1
    for i in stud_list:
        if i.find(class_="align_left").text == name:
            res = i
            break
    if res != -1:
        temp_l = list(map(lambda x: int(x.text) if len(x.text) else 0, res.find_all(class_='w50 no_mobile')))
        return dict(zip(score_list, temp_l))
    return dict()


def create_json():
    data = search_scores()
    with open("data_file.json", "w") as write_file:
        json.dump(data, write_file)


def update_json(data):
    with open("data_file.json", "w") as write_file:
        json.dump(data, write_file)


def check_and_update():
    new_data = search_scores()
    with open("data_file.json") as write_file:
        data = json.load(write_file)
        res = []
        for i in data:
            if data[i] != new_data[i]:
                res.append(i+f": {data[i]} -> {new_data[i]}")
        if not res:
            res.append('nothing')
        else:
            update_json(new_data)
    return res

if __name__ == '__main__':
    print(check_and_update())
