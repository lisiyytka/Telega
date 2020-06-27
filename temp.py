import requests
from bs4 import BeautifulSoup as BS
import re
def temp(city):
    req = requests.get('https://sinoptik.com.ru/погода-'+city.lower())
    html = BS(req.content, 'html.parser')
    temper = html.select(".weather__content_tab-temperature")

    t_min = temper[0].select('.min')[0].text
    t_min = t_min.replace('\n', ' ')
    t_max = temper[0].text.split('\n')[5]
    temp = t_min + 'макс.  ' + t_max

    day = html.select(".weather__content_tab-day")
    day = day[0].text.replace('\n', '')

    text = req.text
    char = re.findall(r'<p class="weather__content_tab-date day_red">\w+', text)
    char = char[0].split('>')[1]
    month = re.findall(r'<p class="weather__content_tab-month">\w+', text)
    month = month[0].split('>')[1]
    data = day + ' ' + char + ' ' + month
    temp = data + '\n' + temp
    return str(temp)
