import requests
from bs4 import BeautifulSoup


def search_scores(name: str) -> dict:
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


if __name__ == '__main__':
    result = search_scores('Романов Александр Дмитриевич')
    for i, j in result.items():
        print(f"{i}: {j}")

